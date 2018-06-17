import os
import sys
import gensim.models

ERR_CODES = [
  '$RET_EINVAL',
  '$RET_ENOMEM',
  '$RET_EIO',
  '$RET_EPERM',
  '$RET_ENODEV',
  '$RET_EFAULT',
  '$RET_ETIMEDOUT',
  '$RET_EAGAIN',
  '$RET_EBUSY',
  '$RET_EMSGSIZE',
  '$RET_ENXIO',
  '$RET_ENOSPC',
  '$RET_ENOENT',
  '$RET_EUCLEAN',
  '$RET_ENOBUFS',
  '$RET_EINTR',
  '$RET_EOPNOTSUPP',
  '$RET_ENODATA',
  '$RET_EREMOTEIO',
  '$RET_EPROTO',
  '$RET_EBADMSG',
  '$RET_EPIPE',
  '$RET_ETIME',
  '$RET_EINPROGRESS',
  '$RET_EACCES',
  '$RET_ENOSYS',
  '$RET_EEXIST',
  '$RET_ENETDOWN',
  '$RET_EADDRINUSE',
  '$RET_ESRCH',
  '$RET_ERANGE',
  '$RET_ESHUTDOWN',
  '$RET_ENOTBLK',
  '$RET_EROFS',
  '$RET_ENOTCONN',
  '$RET_EMLINK',
  '$RET_EADDRNOTAVAIL',
  '$RET_EHOSTUNREACH',
  '$RET_EBADR',
  '$RET_EFBIG',
  '$RET_ESTALE',
  '$RET_EPROTONOSUPPORT',
  '$RET_EDEADLK',
  '$RET_EBADF',
  '$RET_EXFULL',
  '$RET_EOVERFLOW',
  '$RET_ENOTTY',
  '$RET_ECONNREFUSED',
  '$RET_ENOMSG',
  '$RET_ENAMETOOLONG',
  '$RET_EHOSTDOWN',
  '$RET_ENOTDIR',
  '$RET_ENETUNREACH',
  '$RET_EDQUOT',
  '$RET_EXDEV',
  '$RET_ECHILD',
  '$RET_ELOOP',
  '$RET_EBADRQC',
  '$RET_ERESTART',
  '$RET_EISDIR',
  '$RET_EILSEQ',
  '$RET_ENOLCK',
  '$RET_ENOMEDIUM',
  '$RET_ECONNRESET',
  '$RET_EDOM',
]

TESTS = [
  ('Suite 1: Things that lead to ENOMEM on failure', '$RET_ENOMEM', [
    'devm_kzalloc',
    'kzalloc',
    'kmalloc',
    'alloc_pages',
    'fb_alloc_cmap',
    'alloc_etherdev_mqs',
    'kcalloc',
    'comedi_alloc_subdev_readback',
    'pci_alloc_consistent',
    'vmalloc',
    'dev_alloc_skb',
    'alloc_skb',
    'debugfs_create_file',
    'proc_create_data',
    'ioremap',
    'kmem_cache_create',
    'proc_mkdir',
    'add_uevent_var',
    'dma_alloc_coherent',
    'ceph_buffer_new'
  ])
]


def most_similar_to_given(model, average, given):
  '''
  Finds the most similar word from the set of words
  to the average word

  average : a word VECTOR that represents the average of several words
  given   : a set of words to compare the average word to

  Returns the word in given closest to the average word
  '''
  minimum = (float('inf'), None)

  # Precomute distances
  distances = model.wv.distances(average, given)

  # Find the most similar word
  for i, w in enumerate(distances):
    if distances[i] < minimum[0]:
      minimum = (distances[i], given[i])
  
  # Return that word
  return minimum[1]


def queries_via_averaging(model):

  # Two special vectors we'll use in our averages
  ERR_VECTOR = model.wv.word_vec('$ERR')
  END_VECTOR = model.wv.word_vec('$END')

  # Average vectors we'll test with
  build_averages = lambda q: (
    (model.wv.word_vec(q)), 
    (model.wv.word_vec(q) + ERR_VECTOR) / 2.0,
    (model.wv.word_vec(q) + END_VECTOR) / 2.0,
    (model.wv.word_vec(q) + ERR_VECTOR + END_VECTOR) / 3.0
  )

  # Result format
  print_results = lambda title,p,total: print(
    '{} : {:>3}/{:<3} passed ({:.2%})'.format(title,p,total,float(p)/float(total))
  )

  # Run through each test (ONLY ONE right now)
  for _,answer,questions in TESTS:
    # Init counters
    total, p1, p2, p3, p4 = (0,0,0,0,0)

    # Go through each 'question' in this test suite
    for q in questions:
      # try:
      total += 1 

      # Build our 4 target vectors
      q1,q2,q3,q4 = build_averages(q)

      # Accumulate results
      p1 += 1 if most_similar_to_given(model, q1, ERR_CODES) == answer else 0
      p2 += 1 if most_similar_to_given(model, q2, ERR_CODES) == answer else 0
      p3 += 1 if most_similar_to_given(model, q3, ERR_CODES) == answer else 0
      p4 += 1 if most_similar_to_given(model, q4, ERR_CODES) == answer else 0
      # except Exception: # Shouldn't happen
        # print("Cannot run this benchmark if any words are out-of-vocabulary.")
        # exit(1)

    # Need to have run at least one test
    if total == 0:
      print("Cannot run benchmark with no queries.")
      exit(1)

    # Pretty print it!
    print_results('              w', p1, total)
    print_results('       w + $ERR', p2, total)
    print_results('       w + $END', p3, total)
    print_results('w + $ERR + $END', p4, total)
