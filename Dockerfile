# Set Ubuntu operating system image
FROM ubuntu:latest

# Install Python 3.11 and wget
RUN apt-get update && \
    apt-get install -y software-properties-common wget && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.11 python3.11-distutils && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    python3.11 get-pip.py && \
    rm get-pip.py

# Set the working directory
WORKDIR /docker-project

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN python3.11 -m pip install --no-cache-dir -r requirements.txt

# Copy main.py and other necessary files
COPY main.py .
COPY config.json .

# Set the entrypoint to run main.py
ENTRYPOINT ["python3.11", "main.py"]
