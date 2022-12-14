FROM ubuntu
RUN apt-get update && apt-get install -y python3 && apt-get install -y python3-pip
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "pip", "list" ]
