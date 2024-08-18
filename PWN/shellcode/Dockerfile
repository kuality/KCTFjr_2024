FROM ubuntu:22.04

RUN dpkg --add-architecture i386
RUN apt -y update
RUN apt -y upgrade
RUN apt install -y socat libc6:i386
RUN groupadd -r shellcode && useradd -r -g shellcode shellcode

COPY ./server/main /home/shellcode/main
COPY ./server/flag /flag

WORKDIR /home/shellcode
RUN chmod 440 /flag
RUN chmod 550 main

RUN chown -R root:shellcode /home/shellcode
RUN chown root:shellcode /flag
USER shellcode

CMD socat TCP-L:8080,reuseaddr,fork, EXEC:"./main"
