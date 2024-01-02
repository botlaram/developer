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
    unzip \
    tree \
    net-tools \
    vim \
    sudo \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

#for slave installing ansible not required
RUN pip install ansible

ENV ANSIBLE_HOST_KEY_CHECKING False