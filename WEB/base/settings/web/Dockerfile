FROM ubuntu:20.04@sha256:0b897358ff6624825fb50d20ffb605ab0eaea77ced0adb8c6a4b756513dec6fc

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update

RUN apt-get install apache2=2.4.41-4ubuntu3.21\
	php=2:7.4+75 -y

RUN apt-get clean

COPY ./src/ /var/www/html/
RUN rm -rf /var/www/html/index.html

WORKDIR /var/www/html/

RUN mkdir /var/www/html/uploads && chmod 777 /var/www/html/uploads

CMD ["/bin/bash", "-c", "source /etc/apache2/envvars && exec /usr/sbin/apache2 -D FOREGROUND"]
