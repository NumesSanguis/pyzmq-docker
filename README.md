Attempt at Dockerizing modules who communicate over pyzmq (ZeroMQ)

stackoverflow question: https://stackoverflow.com/questions/53802691/pyzmq-dockerized-pub-sub-sub-wont-receive-messages

Dockerzing a publisher module (socket.connect(url)) to send data to a non-dockerized subscriber (socket.bind(url))