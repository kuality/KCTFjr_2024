FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update

RUN apt install python3 python3-pip -y

RUN pip3 install flask

WORKDIR /src/

CMD ["python3", "app.py"]