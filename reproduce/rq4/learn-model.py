from numpy.random import seed

import sys

seed(1)

import numpy as np
import labels as L

import tensorflow.contrib.keras as keras
import tensorflow as tf

from keras import backend as K

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical

from keras.engine import Layer, InputSpec, InputLayer

from keras.models import Model, Sequential

from keras.layers import Dropout, Embedding, concatenate
from keras.layers import Conv1D, MaxPooling1D, GlobalMaxPooling1D, GlobalAveragePooling1D, Conv2D, MaxPool2D, ZeroPadding1D
from keras.layers import Dense, Input, Flatten, BatchNormalization
from keras.layers import Concatenate, Dot, Merge, Multiply, RepeatVector
from keras.layers import Bidirectional, TimeDistributed
from keras.layers import SimpleRNN, LSTM, GRU, Lambda, Permute
from keras.layers import merge

from keras.layers.core import Reshape, Activation
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint,EarlyStopping,TensorBoard
from keras.constraints import maxnorm
from keras.regularizers import l2
from keras.metrics import top_k_categorical_accuracy

from keras.optimizers import SGD

import keras.metrics

def top_3_accuracy(y_true, y_pred):
  return top_k_categorical_accuracy(y_true, y_pred, k=3)
keras.metrics.top_3_accuracy = top_3_accuracy

import pickle


EMBEDDING_DIM = 300
MAX_SEQUENCE_LENGTH = 100
MAX_NUMBER_WORDS = 136085
VALIDATION_SPLIT = 0.10

traces = []
with open('err-traces-shuf.txt', 'r') as tracesf:
  traces = list(tracesf.readlines())[:40000]

traces = [
  ' '.join([x.strip() for x in t.strip().split(' ')[::-1][-MAX_SEQUENCE_LENGTH:]])
  for t in traces
]

traces = [
  (' '.join(t.split(' ')[:-3]), t.split(' ')[-2])
  for t in traces
]

labels = [ L.LABELS[l][0] for (_, l) in traces ]
texts = [ t for (t, _) in traces ]

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

# split the data into a training set and a validation set
indices = np.arange(data.shape[0])
np.random.shuffle(indices)
data = data[indices]
labels = labels[indices]
nb_validation_samples = int(VALIDATION_SPLIT * data.shape[0])

x_train = data
y_train = labels

traces = []
with open('/app/dataset.txt', 'r') as tracesf:
  traces = list(tracesf.readlines())

traces = [
  (t.split('|')[1].strip(), t.split('|')[2].strip())
  for t in traces
]

labels = [ L.LABELS[t[0]][0] for t in traces ]
texts = [ t[1] for t in traces ]

for t in traces:
  assert len(t) <= MAX_SEQUENCE_LENGTH

sequences = tokenizer.texts_to_sequences(texts)

data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)

labels = to_categorical(np.asarray(labels), num_classes=L.NUM_LABELS)
print('Shape of data tensor:', data.shape)
print('Shape of label tensor:', labels.shape)

# split the data into a training set and a validation set
indices = np.arange(data.shape[0])
np.random.shuffle(indices)
data = data[indices]
labels = labels[indices]

x_val = data
y_val = labels


embeddings_index = {}
with open('vectors-gensim.txt', 'r') as vecsf:
  first = True
  for line in vecsf:
    if first:
      first = False
      continue
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    embeddings_index[word] = coefs

print('Found %s word vectors.' % len(embeddings_index))

embedding_matrix = np.zeros((len(word_index) + 1, EMBEDDING_DIM))
for word, i in word_index.items():
  embedding_vector = embeddings_index.get(word)
  if embedding_vector is not None:
    # words not found in embedding index will be all-zeros.
    embedding_matrix[i] = embedding_vector

model = Sequential()
model.add(Embedding(
  len(word_index) + 1,
  EMBEDDING_DIM,
  weights=[embedding_matrix],
  input_length=MAX_SEQUENCE_LENGTH,
  trainable=(True if sys.argv[1] == 'T' else False)
))
model.add(LSTM(25, return_sequences=True, dropout=0.25, recurrent_dropout=0.1))
model.add(GlobalMaxPooling1D())
model.add(Dense(10, activation="relu"))
model.add(Dropout(0.25))
model.add(Dense(units=L.NUM_LABELS, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              metrics=['top_3_accuracy'], optimizer='adam')

model.fit(
  x_train, y_train, 
  validation_data=(x_val, y_val),
  epochs=10, batch_size=32, shuffle=True,
  callbacks=[
    keras.callbacks.ModelCheckpoint(
      'checkpoint.{epoch:02d}-{val_top_3_accuracy:.2f}.h5', 
      monitor='val_top_3_accuracy', 
      verbose=0, 
      save_best_only=True
    )
  ]
)

model.save('{}-temp.model.h5'.format(sys.argv[2]))
