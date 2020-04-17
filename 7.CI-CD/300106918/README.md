# python-dockerfile










#### Build your image

```
docker build -t my-b300106918:1.0.1 .
```
 ![](image/c1.png)
#### check all docker images
```
$ docker image history my-b300106918:1.0.1

```

 ![](image/c9.png)

#### Run your image
```
$ docker run -d -p 8080:8080 b300106918:1.0.1
```

 ![](image/c3.png)
You can use `docker ps` to list all running containers. 
```
$ docker ps

```
 ![](image/c4.png)


+ display logs in running container
```
$ docker logs 7a5b59d52606  

```
 ![](image/c5.png)


#### Test your application
```
$ curl http://localhost:8080
Hello World
```

 ![](image/c6.png)


#### Test
http://127.0.0.1:5000/ 

![](image/c10.png)
