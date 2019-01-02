#pub
FROM python:3.7.1-slim

MAINTAINER foo spam <foo@spam.eggs>

RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  gcc

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY pub/main.py /app/main.py

# part of Docker network and therefore tcp://sub:5551 resolves
CMD ["python", "main.py", "sub"]
