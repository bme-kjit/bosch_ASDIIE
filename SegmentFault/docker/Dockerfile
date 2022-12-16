# create as base image
FROM scratch

# install python3 & python3-pip
RUN apt-get update
RUN apt-get install --no-install-recommends -y
RUN python3.8 python3-pip python3.8-dev

# install required python packages
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt