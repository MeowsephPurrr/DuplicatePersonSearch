FROM python:3.13-slim-bookworm

ENV PYTHONUNBUFFERED 1

ARG APP_PORT

RUN apt-get update

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE $APP_PORT

CMD uvicorn src.main:app --host 0.0.0.0 --port $APP_PORT --reload