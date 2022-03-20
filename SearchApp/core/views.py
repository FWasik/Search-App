from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
import requests
from requests.sessions import Session
from bs4 import BeautifulSoup
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from bs4.element import Tag
from typing import List

import itertools


def home(request: WSGIRequest) -> render:
    data = None

    if "keywords" in request.GET:
        site: str = request.GET.get("site")
        content: str = get_content(request.GET.get("keywords"), site, request.GET.get("pages"))

        soup: BeautifulSoup = BeautifulSoup(content, "html.parser")

        data = List

        if site == "Lancet":
            data = scraping(
                soup,
                site,
                addr="https://www.thelancet.com",
                article_el="div",
                article_class="search__item__body",
                title_el="h4",
                title_class="meta__title",
                authors_el="ul",
                authors_class="meta__authors rlist--inline comma",
                intro_el="p",
                intro_class="meta__details",
            )

        elif site == "PubMed":
            data = scraping(
                soup,
                site,
                addr="https://pubmed.ncbi.nlm.nih.gov/",
                article_el="div",
                article_class="docsum-content",
                title_el="a",
                title_class="docsum-title",
                authors_el="span",
                authors_class="docsum-authors full-authors",
                intro_el="div",
                intro_class="full-view-snippet",
            )

        elif site == "New England Journal of Medicine":
            data = scraping(
                soup,
                site,
                addr="https://www.nejm.org",
                article_el="div",
                article_class="issue-item_left",
                title_el="h6",
                title_class="issue-item_title",
                authors_el="div",
                authors_class="issue-item_auth-cita",
                intro_el="div",
                intro_class="issue-item_text issue-item_text_free",
            )

        page = request.GET.get("page")

        paginator: Paginator = Paginator(data, 10)

        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

    return render(request, "core/home.html", {"data": data})


def get_content(keywords: str, site: str, pages: str) -> str:
    keywords = keywords.replace(" ", "+")

    USER_AGENT: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
    LANGUAGE: str = "en-US,en;q=0.5"
    session: Session = requests.Session()

    session.headers["User-Agent"] = USER_AGENT
    session.headers["Accept-Language"] = LANGUAGE
    session.headers["Content-Language"] = LANGUAGE

    html_content: str = ""
    x: int = 1

    pages: int = int(pages)

    if site == "Lancet":
        x = 0

        while x < pages:
            html_content += session.get(
                f"https://www.thelancet.com/action/doSearch?text1={keywords}&field1=AllField&startPage={x}&pageSize=25"
            ).text
            html_content += " "

            x += 1

    elif site == "PubMed":
        while x <= pages:
            html_content += session.get(
                f"https://pubmed.ncbi.nlm.nih.gov/?term={keywords}&page={x}"
            ).text
            html_content += " "

            x += 1

    elif site == "New England Journal of Medicine":
        new_keywords = keywords.replace("+", "%20")
        while x <= pages:
            html_content += session.get(
                f"https://www.nejm.org/search?q={new_keywords}&startPage={x}"
            ).text
            html_content += " "

            x += 1

    return html_content


def scraping(soup: BeautifulSoup, site: str, **kwargs) -> List:
    data = list()
    articles: list = soup.find_all(
        kwargs["article_el"], attrs={"class": kwargs["article_class"]}
    )

    for item in articles:
        title: Tag = item.find(
            kwargs["title_el"], attrs={"class": kwargs["title_class"]}
        )
        href: str = kwargs["addr"]
        authors: Tag = item.find(
            kwargs["authors_el"], attrs={"class": kwargs["authors_class"]}
        )
        intro: Tag = item.find(
            kwargs["intro_el"], attrs={"class": kwargs["intro_class"]}
        )

        if site == "Lancet":
            href += title.find("a", href=True)["href"]

            authors_final: str = ""
            intro_final: str = ""

            for comb in itertools.zip_longest(authors, intro):
                for el in comb:
                    if el is None:
                        pass

                    elif el.name == "li":
                        authors_final += el.get_text()
                        authors_final += ", "

                    elif el.name == "span":
                        intro_final += el.get_text()
                        intro_final += ", "

            data.append(
                {
                    "title": title.get_text(),
                    "href": href,
                    "authors": authors_final,
                    "intro": intro_final,
                }
            )

        elif site == "PubMed":
            href += item.find("a", href=True)["href"]

            data.append(
                {
                    "title": title.get_text(),
                    "href": href,
                    "authors": authors.get_text(),
                    "intro": intro.get_text(),
                }
            )

        elif site == "New England Journal of Medicine":
            href += item.find("a", href=True)["href"]

            authors_final: str = ""

            for el in authors:
                authors_final += el.get_text()
                authors_final += ", "

            if intro is None:
                data.append(
                    {
                        "title": title.get_text(),
                        "href": href,
                        "authors": authors_final,
                    }
                )

            else:
                data.append(
                    {
                        "title": title.get_text(),
                        "href": href,
                        "authors": authors_final,
                        "intro": intro.get_text(),
                    }
                )

    return data
