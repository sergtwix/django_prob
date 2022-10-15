FROM python:3.10-alpine
USER root
ENV PYTHONUNBUFFERED 1
ENV PIP_ROOT_USER_ACTION=ignore

#RUN python -m pip install --upgrade pip

#COPY requirements.txt requirements.txt
#RUN python -m pip install -r requirements.txt

#RUN mkdir /proj_prob
#WORKDIR /proj_prob

#COPY ./proj_prob /proj_prob

RUN sudo apt-get update \
    && apt-get --yes --no-install-recommends install \
        locales tzdata ca-certificates sudo \
        bash-completion iproute2 tar unzip curl rsync vim nano tree \
    && rm -rf /var/lib/apt/lists/*
ENV LANG en_US.UTF-8


# Install Python stack
RUN sudo apt-get update \
    && apt-get --yes --no-install-recommends install \
        python3 python3-dev \
        python3-pip python3-venv python3-wheel python3-setuptools \
        build-essential cmake \
        graphviz git openssh-client \
        libssl-dev libffi-dev \
    && rm -rf /var/lib/apt/lists/*


RUN mkdir /Serg_site
WORKDIR /Serg_site
COPY requirements.txt /Serg_site/

# RUN apt-get update \
#     && apt-get --yes --no-install-recommends install \
#         python3-dev default-libmysqlclient-dev build-essential \
#         mysql-client libssl-dev \


RUN pip install --upgrade pip && pip install --upgrade setuptools && pip install ez_setup && pip install -r requirements.txt
ADD . /Serg_site/