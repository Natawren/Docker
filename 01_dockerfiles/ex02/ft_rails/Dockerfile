FROM ruby

RUN apt-get -y update && apt-get upgrade -y && apt-get install -qq -y build-essential nodejs sqlite3 libpq-dev
# Copy our Rails application files from our local directory into the container
ONBUILD RUN mkdir /opt/app
ONBUILD COPY todo /opt/app
ONBUILD WORKDIR /opt/app/
ONBUILD EXPOSE 3000 
ONBUILD RUN  gem install bundler && bundle install && gem install rails
ONBUILD RUN rake db:migrate
ONBUILD RUN rake db:seed




