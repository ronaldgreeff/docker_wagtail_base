#!/bin/bash

chown -R nginx:nginx /var/www/web/static /var/www/web/media;

exec "$@"
