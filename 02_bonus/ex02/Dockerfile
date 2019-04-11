FROM ubuntu

RUN apt-get update -y && apt-get upgrade -y && apt-get install -y -qq nodejs npm build-essential  && apt-get install -y -qq curl vim ssh git
RUN npm install yarn --global 

# docker build -t image12 .
# docker run -it -d --name im12 image12