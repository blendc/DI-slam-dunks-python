FROM python:3.10-slim-bookworm as builder
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
RUN mkdir -p /src

COPY src/ /src/

RUN pip install -U pip
RUN pip install -e /src
WORKDIR /src
RUN ls -la

RUN apt update
RUN apt install -y supervisor postgresql-client
RUN mkdir -p /var/log/supervisord && \
    touch supervisord.log

RUN ls -la


COPY config/celery/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
