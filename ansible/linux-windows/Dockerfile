FROM ubuntu:latest

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install \
    build-essential \
    curl \
    software-properties-common \
    python3 \
    python3-pip \
    openssh-server \
    sshpass \
    git \
    sudo \
    unzip \
	vim \
    net-tools \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

RUN pip install ansible
RUN pip install pywinrm

# Copy dir
COPY . /tmp/linux-windows

ENV ANSIBLE_HOST_KEY_CHECKING False