# CC0
# Stef van der Struijk

import zmq
import time


def main():
    # ZMQ connection
    url = "tcp://127.0.0.1:5550"
    ctx = zmq.Context()
    socket = ctx.socket(zmq.PUB)
    socket.connect(url)  # publisher connects to subscriber
    print("Pub connected to: {}\nSending data...".format(url))

    i = 0

    while True:
        topic = 'foo'.encode('ascii')
        msg = 'test {}'.format(i).encode('ascii')
        # publish data
        socket.send_multipart([topic, msg])  # 'test'.format(i)
        print("On topic {}, send data: {}".format(topic, msg))
        time.sleep(.5)

        i += 1


if __name__ == "__main__":
    main()
