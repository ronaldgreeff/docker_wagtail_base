FROM nginx:1.16.1

RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /etc/nginx/nginx.conf

VOLUME /etc/nginx/conf.d

COPY site.old.conf /etc/nginx/conf.d/

WORKDIR /etc

COPY ./entrypoint.sh /etc/entrypoint.sh

ENTRYPOINT ["/etc/entrypoint.sh"]
# nginx -g 'daemon off;'
