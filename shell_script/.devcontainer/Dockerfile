FROM ubuntu:latest

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install \
    build-essential \
    curl \
    git \
    tree \
    sudo \
    vim \
    python3

# Set up a non-root user and switch to it
# ARG USERNAME=vscode
# ARG USER_UID=1000
# ARG USER_GID=$USER_UID

# # Create user
# RUN groupadd --gid $USER_GID $USERNAME \
#     && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
#     # [Optional] Add sudo support for non-root user
#     && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
#     && chmod 0440 /etc/sudoers.d/$USERNAME

# Switch to non-root user
# USER $USERNAME

# Set the default shell to bash rather than sh
ENV SHELL /bin/bash

# Set the default work directory to /workspace
# WORKDIR /workspace