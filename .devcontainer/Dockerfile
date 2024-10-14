FROM ubuntu:24.04

ARG PLANTUML_VERSION=1.2024.6
ARG POETRY_VERSION=1.8.3
ARG PYTHON_VERSION=3.12
ENV PLANTUML_PATH=/usr/share/plantuml/plantuml.jar

SHELL ["/bin/bash","-c"]

RUN apt-get update && apt-get upgrade -y
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

RUN mkdir -p $(dirname "${PLANTUML_PATH}")
RUN wget \
    https://github.com/plantuml/plantuml/releases/download/v${PLANTUML_VERSION}/plantuml-mit-${PLANTUML_VERSION}.jar \
    -O ${PLANTUML_PATH}

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python${PYTHON_VERSION} 311
RUN ln -s /usr/bin/python3 /usr/bin/python

ENV PIPX_HOME=/opt/pipx \
    PIPX_BIN_DIR=/usr/local/bin

RUN pipx ensurepath
RUN pipx install poetry==${POETRY_VERSION}

USER ubuntu
RUN poetry config virtualenvs.in-project true
