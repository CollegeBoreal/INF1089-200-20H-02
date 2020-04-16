


FROM debian:9.5-slim
COPY . /app 
RUN apt-get update
RUN apt-get upgrade -y 
RUN apt-get install -y python python-pip

CMD python app.py 
CMD ["entry.py"]
EXPOSE 5000 
WORKDIR /app 

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]


