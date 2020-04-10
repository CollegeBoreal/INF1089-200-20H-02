

FROM debian:9.5-slim
RUN install_packages ca-certificates curl git
RUN apt-get install -y redis-server && \
    apt-get clean

RUN mkdir /myvol
RUN echo "hello world" > /myApp/greeting
VOLUME /App

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 80

CMD ["redis-server", "--protected-mode no"]
