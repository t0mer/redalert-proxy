FROM ubuntu:24.10

LABEL maintainer="tomer.klein@gmail.com"

#install pip3
RUN apt update

RUN apt install python3-pip --yes

#install python packages

RUN  pip3 install --upgrade pip --no-cache-dir && \
     pip3 install --upgrade setuptools --no-cache-dir && \
     pip3 install flask --no-cache-dir && \
     pip3 install flask_restful --no-cache-dir && \
     pip3 install loguru --no-cache-dir && \
     pip3 install urllib3 --no-cache-dir




ENV PYTHONIOENCODING=utf-8

ENV LANG=C.UTF-8

ENV REGION = "*"

ENV LANGUAGE = "he"

EXPOSE 8080

#Create working directory
RUN mkdir /opt/redalert

COPY proxy.py /opt/redalert

ENTRYPOINT ["/usr/bin/python3", "/opt/redalert/proxy.py"]
