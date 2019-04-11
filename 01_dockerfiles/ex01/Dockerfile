FROM debian

RUN apt-get update -y && apt-get install -y \
                        bzip2 \
                        ca-certificates \
                        wget
# Download
RUN wget http://dl.4players.de/ts/releases/3.6.1/teamspeak3-server_linux_amd64-3.6.1.tar.bz2 
# All the contents will appear in teamspeak3-server_linux_amd64 directory
RUN tar -jxvf teamspeak3-server_linux_amd64-3.6.1.tar.bz2
RUN rm -rf teamspeak3-server_linux_amd64-3.6.1.tar.bz2
# Accept license
ENV TS3SERVER_LICENSE=accept

# Use the same ports as in https://docs.docker.com/samples/library/teamspeak/, 
EXPOSE 9987/udp
EXPOSE 10011
EXPOSE 30033 

CMD ["./teamspeak3-server_linux_amd64/ts3server_minimal_runscript.sh"]

# docker run -p 9987:9987/udp -p 10011:10011 -p 30033:30033 -e TS3SERVER_LICENSE=accept 
# //if you dont set accepting license and ports, you can just use this command



