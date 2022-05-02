FROM python:3.6-alpine
ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFUERED=1

WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . /django/