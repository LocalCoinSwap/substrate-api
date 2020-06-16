FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./requirements.txt /app/requirements.txt

RUN cd /app && pip3 install -r requirements.txt

ENV ENV_SETUP=production
COPY ./ /app
WORKDIR /app
