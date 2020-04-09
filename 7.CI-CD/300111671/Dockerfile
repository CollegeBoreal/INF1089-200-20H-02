FROM debian:9.5-slim

RUN mkdir /myvol
RUN echo "hello world" > /myApp/greeting
VOLUME /App

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
