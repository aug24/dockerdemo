#!/bin/bash

sed -i "s/5000/$1/g" /opt/bgch-app/app-hello-world.py

# Start supervisord and services
/usr/local/bin/supervisord -n -c /etc/supervisord.conf
