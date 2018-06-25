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
VALIDATION_SPLIT = 0.10

traces = []
with open('err-traces-shuf.txt', 'r') as tracesf:
  traces = list(tracesf.readlines())

traces = [
  ' '.join([x.strip() for x in t.strip().split(' ')[::-1][-MAX_SEQUENCE_LENGTH:]])
  for t in traces
]

traces = [
  (' '.join(t.split(' ')[:-3]), t.split(' ')[-2])
  for t in traces
]

labels = [ L.LABELS[t[1]][0] for t in traces ]
texts = [ t[0] for t in traces ]

traces2 = []
with open('dataset.txt', 'r') as tracesf:
  traces2 = list(tracesf.readlines())

traces2 = [
  (t.split('|')[1].strip(), t.split('|')[2].strip())
  for t in traces2
]

texts2 = [ t[1] for t in traces2 ]


for t in traces:
  assert len(t) <= MAX_SEQUENCE_LENGTH

tokenizer = Tokenizer(num_words=MAX_NUMBER_WORDS)
tokenizer.fit_on_texts(texts + texts2)

texts = [ t for t in texts if t not in texts2 ]

sequences = tokenizer.texts_to_sequences(texts)

word_index = tokenizer.word_index
with open('tokenizer.pkl', 'wb') as pf:
  pickle.dump(tokenizer, pf)
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

x_train = data[:-nb_validation_samples]
y_train = labels[:-nb_validation_samples]
x_val = data[-nb_validation_samples:]
y_val = labels[-nb_validation_samples:]

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
  trainable=False
))
model.add(Conv1D(100, 3, activation='relu', input_shape=(MAX_SEQUENCE_LENGTH, EMBEDDING_DIM)))
model.add(Conv1D(100, 3, activation='relu'))
model.add(MaxPooling1D(3))
model.add(Conv1D(100, 3, activation='relu'))
model.add(Conv1D(100, 3, activation='relu'))
model.add(GlobalAveragePooling1D())
model.add(Dropout(0.5))
model.add(Dense(L.NUM_LABELS, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['categorical_accuracy'])

# checkpointer = ModelCheckpoint(
#   filepath="mlp.model_weights.hdf5", 
#   verbose=1,
#   monitor="val_categorical_accuracy",
#   save_best_only=True,
#   mode="max"
# )

with tf.Session() as sess:
  sess.run(tf.global_variables_initializer())
  # try:
  #   model.load_weights("mlp.model_weights.hdf5")
  # except IOError as ioe:
  #   print("no checkpoints available !")
  
  model.fit(
    x_train, y_train, 
    validation_data=(x_val, y_val),
    epochs=5, batch_size=64, shuffle=True
  )

  # score = model.evaluate(x_test, y_test, batch_size=64)
  model.save('conv-model.h5')