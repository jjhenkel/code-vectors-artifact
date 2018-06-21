# Code Analogies Benchmark / RQ1 Reproduction

This directory contains our code analogies benchmark: a set of over 19,000 code analogies 
extracted from the Linux kernel. This benchmark contains twenty different categories; 
within each category any two pairs of functions can be made into an analogy. 

For example, the `Lock / Unlock` category would have function pairs like the following:

```
mutex_lock_nested/mutex_unlock
spin_lock/spin_unlock
```

To form a ground-truth analogy we can take two pairs and write:
`mutex_lock_nested` : `mutex_unlock` :: `spin_lock` : `spin_unlock`. 

## Using this benchmark (to reproduce our results)

Run the following:

```
docker pull jjhenkel/code-vectors-artifact:rq1
docker run -it --rm jjhenkel/code-vectors-artifact:rq1
```

Results are printed to standard output. 

To clean up afterwords run:

```
docker rmi jjhenkel/code-vectors-artifact:rq1
```

## Using this benchmark (to run our benchmark on different vectors)

To run your own set of vectors against our benchmark do the following:

 - Save the vectors as text in a format Gensim can read (if you have GloVe vectors Gensim offers conversion utilities).
 - Move the vectors to this directory.
 - Run `VECS=your-vectors.txt K=1 make run`. The value of `K` (which controls how many results the analogy solver takes into consideration) can be any positive integer (although commonly `K` is set to `1`, `5`, or `10`).

## Files in this directory

 - `Dockerfile`: provides a docker image that packages other prerequisites such as Python 3 and Gensim.
 - `analogies.py`: actual implementation of our benchmark.
 - `similarity.py`: code to reproduce our similarity queries.
 - `averaging.py`: code to reproduce our queries via vector averaging results.
 - `Makefile`: quick way to run tests.
 - `vectors-gensim.txt`: our word vectors to reproduce analogy solving results.
 - `example-output.md`: example runs of this benchmark on two different host machines.

