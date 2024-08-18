FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update

RUN apt-get install python3 python3-pip -y

RUN apt-get clean

RUN pip3 install flask==2.0.3

WORKDIR /src

CMD ["python3", "app.py"]
