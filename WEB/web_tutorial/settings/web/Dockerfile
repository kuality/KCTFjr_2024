FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update

RUN apt-get install --fix-missing apache2=2.4.29-1ubuntu4.27\
	 php=1:7.2+60ubuntu1 php7.2-mysql=7.2.24-0ubuntu0.18.04.17 -y

RUN apt-get clean

CMD ["/bin/bash", "-c", "source /etc/apache2/envvars && exec /usr/sbin/apache2 -D FOREGROUND"]

