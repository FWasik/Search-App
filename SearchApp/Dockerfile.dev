FROM python:3.11.5-alpine

WORKDIR /app/SearchApp

ARG SECRET_KEY
ENV SECRET_KEY ${SECRET_KEY}

COPY . .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]