FROM ubuntu:14.04

MAINTAINER wayne.clancy@bgch.co.uk

# Let the conatiner know that there is no tty
ENV DEBIAN_FRONTEND noninteractive

#Set our default port
ENV port 5000

# Update System
RUN sudo apt-get clean all
RUN sudo apt-get update
#RUN apt-get -y upgrade

# Basic Requirements
RUN sudo apt-get -y install python-setuptools python-dev build-essential  wget git

# Supervisor Config
RUN /usr/bin/easy_install supervisor
RUN /usr/bin/easy_install supervisor-stdout
ADD ./testapp-hello-world.conf /etc/supervisord.conf

# Install bottle
RUN /usr/bin/easy_install bottle

# Add Python App
RUN mkdir -p /usr/lib/dockerdemo/
ADD . /usr/lib/dockerdemo/

# make start.sh executable
RUN chmod 700 /usr/lib/dockerdemo/start.sh

CMD /usr/lib/dockerdemo/start.sh
