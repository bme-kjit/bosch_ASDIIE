FROM ubuntu:latest
RUN apt-get update
RUN apt-get install python3 python3-pip -y
COPY requirements.txt .
RUN pip install -r requirements.txt
ENTRYPOINT [ "pip", "list" ]