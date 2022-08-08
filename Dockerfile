FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /django

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip3 install -r requirements.txt
