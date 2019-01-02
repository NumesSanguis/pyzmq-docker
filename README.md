# Docker & ZeroMQ
Two Python examples to make micro-services with Docker, which communicate over ZeroMQ.

Examples are using a Publisher-Subscriber pattern to communicate. This means that the pub micro-service just send messages out in the wild, without knowing who is listening and a sub micro-service receiving data, without knowning where the data comes from.

With ZeroMQ, only 1 micro-service can `socket.bind(url)` to 1 address. However, you can have unlimited micro-services `socket.connect(url)` to an address. This means that you can either have many-pub to 1-sub (examples in this Git repo) or 1-pub to many-sub on 1 ip:port.

## 1. Docker container communicate with host
Based on stackoverflow question: https://stackoverflow.com/questions/53802691/pyzmq-dockerized-pub-sub-sub-wont-receive-messages

To run this example, we use the folders `sub-no-compose` and `pub-no-compose`.

### Code instructions

1. Open a terminal and navigate to `sub-no-compose`
2. Run `python main.py`
3. Open a terminal and navigate to `pub-no-compose`
4. Find your host PC's IP
5. Open `pub/Docker`, change "your.ip" to your host PC IP and save
5. docker build . -t foo/bar
6. docker run -it foo/bar
7. Success! Your 1st terminal now should show `On topic b'foo', received data: b'test 1'`



## 2. Two Docker containers with automatic connection

Having to run multiple commands to start all docker containers and manually specify ip:port to connect them is a pain. Therefore, Docker has something called `docker-compose`.
With this, we only need 1 command to do everything!

This example is about the folders `sub` and `pub`, and the files `docker-compose.yml` and `requirements.txt`.

With `docker-compose.yml`, we call separate Docker files to make 2 micro-services in 1 go.
Two other advantages are:

1. We can now connect the `pub` micro-service to the `sub` micro-service with `tcp://sub:5550`, which Docker automatically turns into the ip of the `sub` micro-service.
2. We can include the same `requirements.txt` in both containers (normally Docker complains when you want to include a file with `../` in relation to a Docker file).

### Code instructions

1. `docker-compose up --build`


# Useful Docker commands

    sudo usermod -a -G docker $USER  # add current user to group docker on Linux systems (Ubuntu)

    docker build . -t foo/bar  # build docker image
    docker run -it foo/bar  # run build docker image and enter interactive mode
    docker run -p 5550:5550 -it foo/bar  # same as above with mapping Docker port to host
    docker-compose up  # run docker-compose.yml
    docker-compose build / docker-compose up --build  # rebuild images in docker-compose.yml

    docker image ls  # show docker images
    docker container ls  # show docker containers
    docker exec -it pyzmq-docker_pub_1  # enter bash in container
    docker attach pyzmq-docker_sub_1  # get
    docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' pyzmq-docker_sub_1  # get ip of container

    To detach the tty without exiting the shell, use the escape sequence Ctrl+p + Ctrl+q