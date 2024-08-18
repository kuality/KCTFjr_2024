FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update;apt install apache2 php php-iconv -y

RUN apt clean

CMD ["/bin/bash", "-c", "source /etc/apache2/envvars && exec /usr/sbin/apache2 -D FOREGROUND"]
