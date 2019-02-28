#!/bin/bash
set -e

cd /app
make

# Adapted from GloVe's demo.sh

mkdir -p /output

# Fixed locations
VOCAB_FILE=/output/vocab.txt
COOCCURRENCE_FILE=/output/cooccurrence.bin
COOCCURRENCE_SHUF_FILE=/output/cooccurrence.shuf.bin
BUILDDIR=/app/build
SAVE_FILE=/output/vectors

# Input params
CORPUS=$1
VOCAB_MIN_COUNT=$2
VECTOR_SIZE=$4
WINDOW_SIZE=$3
MAX_ITER=$5
NUM_THREADS=$(getconf _NPROCESSORS_ONLN)

# Constant params
MEMORY=8
VERBOSE=2
BINARY=0
X_MAX=10

echo "[GloVe] Learning vectors with the following parameters:"
echo "[GloVe]               corpus: $CORPUS"
echo "[GloVe]      vocab min count: $VOCAB_MIN_COUNT"
echo "[GloVe]     vector dimension: $VECTOR_SIZE"
echo "[GloVe]          window size: $WINDOW_SIZE (window is symettric)"
echo "[GloVe]  max # of iterations: $MAX_ITER"
echo "[GloVe]         # of threads: $NUM_THREADS"
echo "[GloVe]         memory limit: $MEMORY"
echo "[GloVe]            verbosity: $VERBOSE"
echo "[GloVe]          file format: $BINARY"
echo "[GloVe]                X max: $X_MAX"

echo "[GloVe] Building vocabulary..."
gzip -cd $CORPUS | $BUILDDIR/vocab_count \
  -min-count $VOCAB_MIN_COUNT \
  -verbose $VERBOSE \
  > $VOCAB_FILE

echo "[GloVe] Building cooccurence matrix..."
gzip -cd $CORPUS | $BUILDDIR/cooccur \
  -memory $MEMORY \
  -vocab-file $VOCAB_FILE \
  -verbose $VERBOSE \
  -window-size $WINDOW_SIZE \
  > $COOCCURRENCE_FILE

echo "[GloVe] Shuffling cooccurence matrix..."
$BUILDDIR/shuffle \
  -memory $MEMORY \
  -verbose $VERBOSE \
  < $COOCCURRENCE_FILE \
  > $COOCCURRENCE_SHUF_FILE

echo "[GloVe] Learning vectors..."
$BUILDDIR/glove \
  -save-file $SAVE_FILE \
  -threads $NUM_THREADS \
  -input-file $COOCCURRENCE_SHUF_FILE \
  -x-max $X_MAX \
  -iter $MAX_ITER \
  -vector-size $VECTOR_SIZE \
  -binary $BINARY \
  -vocab-file $VOCAB_FILE \
  -verbose $VERBOSE

echo "[GloVe] Converting to gensim format..."
python -m gensim.scripts.glove2word2vec -i $SAVE_FILE.txt -o $SAVE_FILE.gensim.txt

echo "[GloVe] Complete!"
echo "[GloVe] Vectors saved in '$SAVE_FILE'"

