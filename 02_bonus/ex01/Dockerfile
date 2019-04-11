FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT python app.py

# docker build -t image11.
# docker run -d -it -p 5000:5000 --name im11 image11