FROM python:3.7.1-slim

MAINTAINER foo bar <foo@spam.eggs>

RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  gcc

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY zmq_pub.py /app/zmq_pub.py

EXPOSE 5550

CMD ["python", "zmq_pub.py"]
