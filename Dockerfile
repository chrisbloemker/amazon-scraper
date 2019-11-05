# Dockerfile for Amazon Scraper

FROM python:alpine

#RUN apk add --no-cache \

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

COPY scraper.py /usr/src/app

CMD [ "python", "./scraper.py"]