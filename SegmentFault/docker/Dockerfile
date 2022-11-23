FROM python:3.8-slim

# install required packages
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir requirements.txt

