FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get install -y python3-pip
COPY ./backend/requirements.txt /hf-menu-plan-challenge/backend/requirements.txt

WORKDIR /hf-menu-plan-challenge/backend

RUN pip3 install -r requirements.txt

ENV FLASK_APP="__init__.py"
ENV FLASK_ENV="development"

COPY . /hf-menu-plan-challenge

ENTRYPOINT [ "python3" ]

CMD [ "init.py" ]