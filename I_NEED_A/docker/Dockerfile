FROM ubuntu:focal
RUN apt-get update -y && apt-get install -y \ 
    python3 \
    python3-pip
COPY I_NEED_A/. I_NEED_A
RUN pip3 install -r I_NEED_A/docker/requirements.txt
ENTRYPOINT ["pip3", "list"]
