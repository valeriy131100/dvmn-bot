FROM python:3.10.4-alpine

WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .