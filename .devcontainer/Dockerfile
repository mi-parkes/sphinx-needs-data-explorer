FROM ubuntu:24.04

ARG PLANTUML_VERSION=1.2024.6
ARG PYTHON_VERSION=3.12

SHELL ["/bin/bash","-c"]

# Update package lists
RUN apt-get update && apt-get upgrade -y

# Install essential packages
RUN DEBIAN_FRONTEND=noninteractive  apt install -y \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libssl-dev \
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
    python${PYTHON_VERSION} \
    python${PYTHON_VERSION}-venv \
    python3-pip-whl \
    python3-pip

RUN apt install -y pipx 

RUN mkdir -p /usr/share/plantuml
RUN wget  \
    https://github.com/plantuml/plantuml/releases/download/v${PLANTUML_VERSION}/plantuml-mit-${PLANTUML_VERSION}.jar \
    -O /usr/share/plantuml/plantuml.jar

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python${PYTHON_VERSION} 311
RUN ln -s /usr/bin/python3 /usr/bin/python

COPY ./uid_entrypoint /usr/local/bin/
RUN chmod 777 /usr/local/bin/uid_entrypoint

ENV PIPX_HOME=/opt/pipx \
    PIPX_BIN_DIR=/usr/local/bin

RUN pipx ensurepath
RUN pipx install poetry==1.8.3

USER ubuntu
ENTRYPOINT [ "uid_entrypoint"]
