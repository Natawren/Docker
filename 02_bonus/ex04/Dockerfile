FROM debian

RUN apt-get -y update && apt-get upgrade -y && apt-get install -qq -y telnet
ENTRYPOINT telnet towel.blinkenlights.nl

# docker build -t image14 .
# docker run -it -d --name im14 image14