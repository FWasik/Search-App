FROM python:3.11.5-alpine

WORKDIR /app/SearchApp

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

ARG SECRET_KEY
ENV SECRET_KEY ${SECRET_KEY}

COPY . .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "SearchApp.wsgi:application"]