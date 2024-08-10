FROM ubuntu:24.04

ARG CACHEBUST=1

SHELL ["/bin/bash","-c"]

# Update package lists
RUN apt-get update && apt-get upgrade -y

# Install essential packages
RUN DEBIAN_FRONTEND=noninteractive  apt install -y \
    build-essential libssl-dev zlib1g-dev libbz2-dev libssl-dev \
    git \
    curl \
    wget \
    make \
    graphviz \
    locales \
    locales-all \
    make \
    nano \
    jq \
    openjdk-17-jdk \
    python3.12 python3.12-venv python3-pip-whl python3-pip

RUN mkdir -p /usr/share/plantuml
RUN wget --no-check-certificate \
    https://github.com/plantuml/plantuml/releases/download/v1.2024.5/plantuml-mit-1.2024.5.jar \
    -O /usr/share/plantuml/plantuml.jar

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 311

COPY ./uid_entrypoint /usr/local/bin/
RUN chmod 777 /usr/local/bin/uid_entrypoint

COPY requirements.txt /tmp/requirements.txt

USER ubuntu

ENTRYPOINT [ "uid_entrypoint"]
