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

import pickle


EMBEDDING_DIM = 300
MAX_SEQUENCE_LENGTH = 100
MAX_NUMBER_WORDS = 136085

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

tokenizer = None
with open('/app/conv.1.tokenizer.pkl', 'rb') as wordf:
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

x_val = data
y_val = labels

embeddings_index = {}
with open('/app/vectors-gensim.txt', 'r') as vecsf:
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
  trainable=False
))
model.add(Conv1D(100, 3, activation='relu', input_shape=(100, 300)))
model.add(Conv1D(100, 3, activation='relu'))
model.add(MaxPooling1D(3))
model.add(Conv1D(200, 3, activation='relu'))
model.add(Conv1D(200, 3, activation='relu'))
model.add(GlobalAveragePooling1D())
model.add(Dropout(0.5))
model.add(Dense(L.NUM_LABELS, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['categorical_accuracy'])

model.compile(
  loss='categorical_crossentropy', 
  optimizer=Adam(), 
  metrics=['categorical_accuracy']
)

checkpointer = ModelCheckpoint(
  filepath="/app/conv.1.model_weights.hdf5", 
  verbose=1,
  monitor="val_categorical_accuracy",
  save_best_only=True,
  mode="max"
)

with tf.Session() as sess:
  sess.run(tf.global_variables_initializer())
  try:
    model.load_weights("/app/conv.1.model_weights.hdf5")
  except IOError as ioe:
    print("no checkpoints available !")
  
  answers = model.predict(x_val, batch_size=64)

  get = lambda i: [ l[0] for l in L.LABELS.items() if l[1][0] == i ][0]

  top1 = 0
  top3 = 0
  top5 = 0
  total = 0
  for j,answer in enumerate(answers):
    goal = get(np.argmax(labels[j]))
    # print('GOAL == {}:'.format(goal))
    idx = 0
    total += 1
    for r in sorted([ (get(i), answer[i]) for i in range(0, len(answer)) ], key=lambda x: -x[1])[:5]:
      idx += 1
      # print('  {} ({:.2%})'.format(*r))
      if r[0] == goal and idx <= 1:
        top1 += 1
      if r[0] == goal and idx <= 3:
        top3 += 1
      if r[0] == goal and idx <= 5:
        top5 += 1

  print('Accuracy @1: {:.2%}'.format(float(top1)/float(total)))
  print('Accuracy @3: {:.2%}'.format(float(top3)/float(total)))
  print('Accuracy @5: {:.2%}'.format(float(top5)/float(total)))
