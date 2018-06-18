import gensim


kv = gensim.models.KeyedVectors.load_word2vec_format(
  '/artifacts/redis/vectors.gensim.txt', binary=False
)


def demo(word):
  print('[code-vectors] 5 closest words to "{}"'.format(word))
  for (i, (n,_)) in enumerate(kv.most_similar(word, topn=5)):
    print('[code-vectors]  #{}. {}'.format(i, n))
  print()


# From: 
# https://github.com/antirez/redis/blob/44571088d8407749ca1c49cde09089664e7928ff/src/t_set.c#L52
demo('setTypeAdd')

# From:
# https://github.com/antirez/redis/blob/44571088d8407749ca1c49cde09089664e7928ff/src/t_stream.c#L532
demo('streamIteratorGetID')

# From:
# https://github.com/antirez/redis/blob/44571088d8407749ca1c49cde09089664e7928ff/src/cluster.c#L3692
demo('clusterAddSlot')
demo('clusterLoadConfig')
demo('!->importing_slots_from[?]')

# Just for fun, see what's close to the '$ERR' token
demo('$ERR')
