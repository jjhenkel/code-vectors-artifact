import numpy as np
import labels as L

import sys

import tensorflow.contrib.keras as keras
import tensorflow as tf

from keras import backend as K

K.set_learning_phase(0)

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical

from keras.engine import Layer, InputSpec, InputLayer

from keras.models import Model, Sequential, load_model

from keras.layers import Dropout, Embedding, concatenate
from keras.layers import Conv1D, MaxPooling1D, GlobalAveragePooling1D, Conv2D, MaxPool2D, ZeroPadding1D
from keras.layers import Dense, Input, Flatten, BatchNormalization
from keras.layers import Concatenate, Dot, Merge, Multiply, RepeatVector
from keras.layers import Bidirectional, TimeDistributed
from keras.layers import SimpleRNN, LSTM, GRU, Lambda, Permute

from keras.layers.core import Reshape, Activation
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint,EarlyStopping,TensorBoard
from keras.constraints import maxnorm
from keras.regularizers import l2
from keras.metrics import top_k_categorical_accuracy

import keras.metrics

def top_3_accuracy(y_true, y_pred):
  return top_k_categorical_accuracy(y_true, y_pred, k=3)
keras.metrics.top_3_accuracy = top_3_accuracy

import pickle


EMBEDDING_DIM = 300
MAX_SEQUENCE_LENGTH = 100
MAX_NUMBER_WORDS = 136085

traces = []
with open('/app/dataset.txt', 'r') as tracesf:
  traces = list(tracesf.readlines())

names = [ t.split('|')[0].strip() for t in traces ]

traces = [
  (t.split('|')[1].strip(), t.split('|')[2].strip(), t.split('|')[3])
  for t in traces
]

labels = [ L.LABELS[t[0]][0] for t in traces ]
texts = [ t[1] for t in traces ]
wrongs = [ t[2].strip() for t in traces ]

for t in traces:
  assert len(t) <= MAX_SEQUENCE_LENGTH

tokenizer = None
with open('/app/assets/tokenizer.pkl', 'rb') as wordf:
  tokenizer = pickle.load(wordf)
sequences = tokenizer.texts_to_sequences(texts)

word_index = tokenizer.word_index
print('Found %s unique tokens.' % len(word_index))

data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)

labels = to_categorical(np.asarray(labels), num_classes=L.NUM_LABELS)
print('Shape of data tensor:', data.shape)
print('Shape of label tensor:', labels.shape)

model = load_model('/app/{}'.format(sys.argv[1]))

answers = model.predict(data, batch_size=32)

get = lambda i: [ l[0] for l in L.LABELS.items() if l[1][0] == i ][0]

top1 = 0
top3 = 0
top5 = 0
mistakes3 = 0
mistakes5 = 0
total = 0
for j,answer in enumerate(answers):
  goal = get(np.argmax(labels[j]))
  print('GOAL == {}:'.format(goal))
  idx = 0
  total += 1
  for r in sorted([ (get(i), answer[i]) for i in range(0, len(answer)) ], key=lambda x: -x[1])[:5]:
    idx += 1
    print('  {} ({:.2%})'.format(*r))
    if r[0] == goal and idx <= 1:
      top1 += 1
    if r[0] == goal and idx <= 3:
      top3 += 1
    if r[0] == goal and idx <= 5:
      top5 += 1
    if r[0] == wrongs[j] and idx <= 3:
      mistakes3 += 1
    if r[0] == wrongs[j] and idx <= 5:
      mistakes5 += 1

print('Accuracy @3: {:.2%} ({}/{})'.format(float(top3)/float(total), top3, total))
print('Accuracy @5: {:.2%} ({}/{})'.format(float(top5)/float(total), top5, total))
print('----')
print('Mistakes @3: {:.2%} ({}/{})'.format(float(mistakes3)/float(total), mistakes3, total))
print('Mistakes @5: {:.2%} ({}/{})'.format(float(mistakes5)/float(total), mistakes5, total))