FROM ubuntu:latest
WORKDIR /Reviz

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Bratislava


RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y apt-utils cmake git python3-pip python3-dev libpq-dev postgresql postgresql-contrib build-essential ffmpeg libsm6 libxext6 musl-dev libc-dev apt-utils build-essential libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev libopenblas-dev liblapack-dev
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN python3 manage.py collectstatic
COPY . .
