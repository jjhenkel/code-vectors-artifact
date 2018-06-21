# Syntactic VS Semantic Vectors Study (RQ3 Reproduction)

This directory contains our syntactic vs semantic vectors study (RQ3). NOTE: running this reproduction takes about `2GB` of space and up to `1 hour` depending on the host machine.

## Using this benchmark to reproduce our results

Run the following:

```
docker pull jjhenkel/code-vectors-artifact:rq3
docker run -it --rm jjhenkel/code-vectors-artifact:rq3
```

Results are printed to standard output. 

To clean up afterwords run:

```
docker rmi jjhenkel/code-vectors-artifact:rq3
```

## Files in this directory

 - `Dockerfile`: provides a docker image that packages other prerequisites such as Python 3 and Gensim.
 - `syntactic-vs-semantic.py`: implementation of our syntactiv-vs-semantic vectors study.
 - `entrypoint.sh`: driver for docker container.
 - `example-output.md`: example runs of this benchmark on two different host machines.

