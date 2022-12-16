FROM ubuntu
RUN apt-get update

RUN apt-get install -y python3-pip
COPY requirements.txt ./
RUN pip install -r requirements.txt
ENTRYPOINT [ "pip", "list" ]