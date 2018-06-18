FROM python:3

RUN apt-get update \
  && apt-get install -y lzip tar xz-utils \
  && pip install gensim

COPY ./vectors /vectors

COPY syntactic-vs-semantic.py /app/syntactic-vs-semantic.py
COPY entrypoint.sh /app/entrypoint.sh

ENTRYPOINT [ "/app/entrypoint.sh" ]