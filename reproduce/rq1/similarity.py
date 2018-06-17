import os
import sys
import gensim.models

def closest_words(model):
  targets = [
    'sin_mul',
    'dec_stream_header',
    'rx_b_frame',
    'nouveau_bo_new_$EQ_0'
  ]

  for target in targets:
    print('{} and {}'.format(
      target, 
      model.wv.most_similar(positive=[target], topn=1)[0][0]
    ))


def print_top_words(model):
  targets = [
    'affs_bread',
    'kzalloc'
  ]

  for target in targets:
    print('5 closest words to {}:'.format(target))
    words = model.wv.most_similar(positive=[target], topn=5)
    for i,word in enumerate(words):
      print('  #{} - {}'.format(i+1, word[0]))
