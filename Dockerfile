FROM alpine:3.2
MAINTAINER Ahmet Demir <ahmet2mir+github@gmail.com>

RUN apk add --update python openssl git
RUN wget http://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade -r /tmp/requirements.txt
RUN rm -rf /var/cache/apk/*
RUN mkdir /apps
WORKDIR /apps

CMD ["python", "/apps/main.py"]

EXPOSE 5000

ADD . /apps
