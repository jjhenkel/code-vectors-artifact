# Code-Vectors-Artifact Dataset

## If you haven't already run the artifact

The following commands will get you setup. WARNING: this artifact produces several gigabytes of output data!

To get setup with our original traces and two sets of learned vectors run the following:

```bash
# 1. Make sure we have an output directory to hold the data
mkdir -p ./output
```

```bash
# 2. Pulls the docker image down from docker hub
docker pull jjhenkel/code-vectors-artifact:dataset
```

```bash
# 3. Extracts the (heavily compressed) datasets to the ./output dir
docker run --rm -it -v `pwd`/output:/output jjhenkel/code-vectors-artifact:dataset
```

That's it, you're all set!

## If you've already run the artifact

If you're reading this after running a container off of the `jjhenkel/code-vectors-artifact:dataset` docker image you should 
have a directory (`./output` if you followed the steps above) with the following files:

 - `README.md`: this readme.
 - `vectors-vmin-0.txt`: our vectors learned without a vocabulary minimum (vmin) threshold set.
 - `vectors-vmin-1000.txt`: our vectors learned with a more reasonable vocabulary minimum (vmin) threshold (to filter out rare words).
 - `kernel-traces`: our full set of abstracted symbolic traces extracted from the Linux kernel using our `spec2image`, `c2ocaml`, and `lsee` tools.
 - `peek-traces.sh`: a tool to run to view the first `N` traces from our trace corpus (streams and decompresses the gzipped traces and then runs `head -n$1`). Example: `./peek-traces.sh 100` (prints the first 100 traces from our corpus). NOTE: you need to run this tool in the `./output` directory.
 - `analogies.py`: our full analogies benchmark and scaffolding code to run it on a given set of traces. (NOTE: requires Python and the Gensim library to be installed/working.)

