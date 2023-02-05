FROM ubuntu:latest
WORKDIR /RevizServer

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Bratislava


RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y apt-utils cmake git python3-pip python3-dev postgresql postgresql-contrib build-essential musl-dev libc-dev
RUN pip install --upgrade pip
RUN git clone https://github.com/maromcik/RevizBackend.git
COPY ./requirements.txt .
RUN pip install -r requirements.txt
