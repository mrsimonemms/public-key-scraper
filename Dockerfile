FROM python:2-alpine
WORKDIR /opt/app
ADD . .
ENTRYPOINT [ "python", "scraper.py" ]
