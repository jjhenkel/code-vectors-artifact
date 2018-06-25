# Downstream Tasks (RQ4 Reproduction)

This directory contains a **updated** benchmark for our Downstream Tasks research
question. We have been working on updating this benchmark to be more comprehensive.

## Using this benchmark to reproduce our results

Run the following:

```bash
docker pull jjhenkel/code-vectors-artifact:rq4
docker run -it --rm jjhenkel/code-vectors-artifact:rq4
```

Results are printed to standard output.

To clean up afterwords run:

```bash
docker rmi jjhenkel/code-vectors-artifact:rq4
```

## Files in this directory

 - `Dockerfile`: provides a docker image the code for dataset generation.
 - `Dockerfile.learn`: providers a docker image with code for training an example Keras model.
 - `generate-data.py`: generates our example data (based off of good/bad traces).
 - `entrypoint.sh`: driver for docker container.
 - `example-output.md`: an example run of this benchmark.
 - `learn-model.py`: the code we used to learn a model of traces that end in an error.
 - `score-model.py`: the code we are using to evaluate that learned model.
 - `labels.py`: a manually generated listing of Linux kernel error codes.
 - `notes.md`: some notes on how to extract functions before/after a fixing commit (this was used to aid in generating our dataset).
