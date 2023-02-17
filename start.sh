#!/bin/sh

cd /opt/app && python app.py --daemon
nginx -g "daemon off;"