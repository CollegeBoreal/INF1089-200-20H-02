

FROM debian:9.5-slim
COPY . /app 
RUN apt-get update
RUN apt-get upgrade -y 
RUN apt-get install -y python python-pip
RUN pip install -r /app/requirements.txt 
RUN cd /app ; python setup.py 
CMD python app.py 
RUN mkdir /myvol
RUN echo "hello world" > /myApp/greeting
VOLUME /App

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 80

CMD ["redis-server", "--protected-mode no"]
