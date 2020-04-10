

FROM debian:9.5-slim
<<<<<<< HEAD
RUN apt-get install -y redis-server && \
    apt-get clean
=======
COPY . /app 
RUN apt-get update
RUN apt-get upgrade -y 
RUN apt-get install -y python python-pip
RUN pip install -r /app/requirements.txt 
RUN cd /app ; python setup.py 
CMD python app.py 
>>>>>>> ca871955af4c3dc19f9b2aa5a4f1c683fac1fad2

RUN mkdir /myvol
RUN echo "hello world" > /myApp/greeting
VOLUME /App

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 80

CMD ["redis-server", "--protected-mode no"]
