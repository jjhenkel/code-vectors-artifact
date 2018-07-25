FROM gw000/keras:2.1.4-py3

COPY labels.py /app/
COPY score-model.py /app/
COPY dataset.txt /app
COPY models/best-1.h5 /app
COPY assets/tokenizer.pkl /app/assets/tokenizer.pkl
COPY vectors-gensim.txt /app

CMD [ "/app/score-model.py", "best-1.h5" ]
ENTRYPOINT [ "python3" ]
