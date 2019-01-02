# CC0
# Stef van der Struijk

import sys
import zmq
import time


def main(ip="*"):
    # ZMQ connection
    url = "tcp://{}:5551".format(ip)
    print("Going to connect to: {}".format(url))
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
    # pass ip argument
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main()
