FROM python:3.7-alpine

RUN mkdir -p /app
COPY requirements.txt /app
COPY bin /app
COPY lib /app
WORKDIR /app

RUN pip install requirements.txt

ENTRYPOINT ["/app/bin/date-diff"]
