# Ablation Study (RQ2 Reproduction)

This directory contains our ablation study. WARNING: running this reproduction takes about `6GB` of space and up to `4 hours` depending on the host machine.

## Using this benchmark to reproduce our results

Run the following:

```
docker pull jjhenkel/code-vectors-artifact:rq2
docker run -it --rm jjhenkel/code-vectors-artifact:rq2
```

Results are printed to standard output. 

To clean up afterwords run:

```
docker rmi jjhenkel/code-vectors-artifact:rq2
```

## Files in this directory

 - `Dockerfile`: provides a docker image that packages other prerequisites such as Python 3 and Gensim.
 - `ablation.py`: implementation of our ablation study.
 - `entrypoint.sh`: driver for docker container.
 - `example-output.md`: example runs of this benchmark on two different host machines.

