FROM python:3

RUN pip install gensim

ADD vectors-gensim.txt /vectors/
ADD *.py /app/

ENTRYPOINT [ "/app/analogies.py" ]

CMD [ "/vectors/vectors-gensim.txt", "1" ]
