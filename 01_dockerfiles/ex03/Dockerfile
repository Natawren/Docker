FROM debian

RUN apt-get -y update && apt-get upgrade -y && apt-get install -qq -y wget openssh-server ca-certificates postfix 

RUN wget https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh && \
    chmod 777 script.deb.sh && ./script.deb.sh && apt-get install -y gitlab-ce 
RUN  rm -rf /etc/gitlab/gitlab.rb
COPY gitlab.rb /etc/gitlab/
RUN  mkdir /etc/gitlab/ssl/
COPY 192.168.99.100.key /etc/ssl/private/
COPY 192.168.99.100.key /etc/gitlab/ssl
COPY 192.168.99.100.crt /etc/ssl/certs/
COPY 192.168.99.100.crt /etc/gitlab/ssl
COPY 192.168.99.100.crt /etc/gitlab/trusted-certs/
EXPOSE 443 80 22

ENTRYPOINT service ssh restart && (/opt/gitlab/embedded/bin/runsvdir-start &) && gitlab-ctl reconfigure && tail -f /dev/null

#if you want to check ssh git clone, you should generate ssh-key with:
# docker exec -it CONTAINER bash
#ssh-keygen -t rsa -b 4096 -C "natawren@gmail.com"
#then copy public key in GUI of gitlab in Settings or copy ssh keys from mac
# mkdir /usr/local/share/ca-certificates/cacert.org && wget -P /usr/local/share/ca-certificates/cacert.org http://www.cacert.org/certs/root.crt http://www.cacert.org/certs/class3.crt &&  update-ca-certificates && git config --global http.sslCAinfo /etc/ssl/certs/ca-certificates.crt
#docker run -it --rm -p 8080:80 -p 8022:22 -p 8443:443 --privileged image

# if you want to clone with https on mac, you need to start on mac:
# git config --global http.sslVerify false 
