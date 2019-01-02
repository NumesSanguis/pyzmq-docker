#sub
FROM python:3.7.1-slim

MAINTAINER foo spam <foo@spam.eggs>

RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  gcc

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY sub/main.py /app/main.py

# allow other containers/PCs to connect; maybe not necessary
EXPOSE 5551

CMD ["python", "main.py", "*"]
