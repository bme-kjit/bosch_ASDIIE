#base image 
FROM ubuntu:focal

#python
RUN apt-get update -y && apt-get install -y \ 
    python3 \
    python3-pip

#copy code base to the image
COPY I_NEED_A/. I_NEED_A

#run the listing of packages
RUN pip3 install -r I_NEED_A/docker/requirements.txt
ENTRYPOINT ["pip3", "list"]
