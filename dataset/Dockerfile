FROM python:3

RUN apt-get update \
  && apt-get install -y lzip tar xz-utils \
  && pip install gensim

# Copy over data 
COPY kernel-traces.tar.gz /dataset/kernel-traces.tar.gz
COPY best-vectors-vmin-0.txt.tar.lz /dataset/best-vectors-vmin-0.txt.tar.lz
COPY best-vectors-vmin-1000.txt.tar.lz /dataset/best-vectors-vmin-1000.txt.tar.lz

COPY peek-traces.sh /dataset/peek-traces.sh
COPY analogies.py /dataset/analogies.py
COPY README.md /dataset/README.md

COPY entrypoint.sh /app/entrypoint.sh

ENTRYPOINT [ "/app/entrypoint.sh" ]