FROM python:3.10-slim-buster
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/src

COPY requirements.txt /tmp/
RUN  pip install -r /tmp/requirements.txt

RUN mkdir -p /src
COPY src/ /src/
RUN pip install -U pip
RUN pip install -e /src

WORKDIR /src
CMD uvicorn infrastructure.fastapi:app --host 0.0.0.0 --port 80 --reload

