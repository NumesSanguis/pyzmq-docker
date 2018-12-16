# CC0
# Stef van der Struijk

import zmq


def main():
    # ZMQ connection
    url = "tcp://127.0.0.1:5550"
    ctx = zmq.Context()
    socket = ctx.socket(zmq.SUB)
    socket.bind(url)  # subscriber creates ZeroMQ socket
    socket.setsockopt(zmq.SUBSCRIBE, ''.encode('ascii'))  # any topic
    print("Sub bound to: {}\nWaiting for data...".format(url))

    while True:
        # wait for publisher data
        topic, msg = socket.recv_multipart()
        print("On topic {}, received data: {}".format(topic, msg))


if __name__ == "__main__":
    main()
