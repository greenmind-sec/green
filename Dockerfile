FROM debian

MAINTAINER greenmind.sec@gmail.com

RUN apt-get update -y

RUN apt-get install python3 -y

RUN apt-get install python3-pip -y

RUN apt-get install python3 -y

RUN apt-get install git -y

RUN pip3 install scapy

RUN pip3 install requests

RUN pip3 install shodan

RUN pip3 install bs4

RUN pip3 install pywhatcms

RUN apt-get install tcpdump -y

WORKDIR /root

COPY ./src /root

RUN chmod +x ~/green.py

#TODO - Arrumar o uso via menu, via linha de comando funciona OK, porem o menu possui problemas.
ENTRYPOINT ["/usr/bin/python3", "/root/green.py"]
# ENTRYPOINT ["/bin/sh", "-c"]

CMD ["-h"]
