FROM python:3

RUN apt-get update \
  && apt-get install -y lzip tar xz-utils \
  && pip install gensim

COPY ./vectors /vectors

COPY ablation.py /app/ablation.py
COPY entrypoint.sh /app/entrypoint.sh

ENTRYPOINT [ "/app/entrypoint.sh" ]