FROM ubuntu

RUN apt-get -y update && apt-get upgrade -y && apt-get install -qq -y nginx \
                                                                    uwsgi  \
                                                                    python-pip \
                                                                    python-dev \
                                                                    build-essential \
                                                                    vim \
                                                                    openssl \
                                                                    ca-certificates
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt && pip install django
EXPOSE 443 80

# docker build -t image13 .
# docker run -d -it -p 8080:8080 -p 8443:8443 --name im13 image13