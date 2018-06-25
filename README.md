# Artifact Repository for "Code Vectors" ESEC/FSE'18 Paper

[![DOI](https://zenodo.org/badge/122389109.svg)](https://zenodo.org/badge/latestdoi/122389109)

The contact author for this artifact is Jordan Henkel <jjhenkel@cs.wisc.edu>.

## Reproducing our experimental results

See [INSTALL.md](INSTALL.md).

## Running an end-to-end test

See [INSTALL.md](INSTALL.md).

## Getting our raw data

See [dataset/README.md](dataset/README.md).

## Exploring our `c2ocaml` tool

Check out [c2ocaml](https://github.com/jjhenkel/c2ocaml) on GitHub!

## Exploring our `lsee` tool

Check out [lsee](https://github.com/jjhenkel/lsee) on GitHub!

## Explore our ready-to-use docker images

Check them out at [hub.docker.com](https://hub.docker.com/r/jjhenkel/)!

---

## What you should expect to see running these artifacts

### For our rq1/rq2/rq3 artifacts

For these artifacts you should be able to match the output to either our included
example outputs (see [here](reproduce/rq1/example-output.md), [here](reproduce/rq2/example-output.md), and [here](reproduce/rq3/example-output.md)) or directly to the (updated) tables/charts
in [our paper](paper.pdf).

**Note:** tables and charts were recently updated to include a fix for a bug
found and patched during the creation of our artifact.

### For the rq4 artifact

For this artifact we have generated a more comprehensive benchmark compared to
the one we used in our initial submission. You can refer to the [example-output.md](reproduce/rq4/example-output.md) file
for expected output.

### For the end-to-end demo

If you choose to run the end-to-end demo, you should see quite a bit of console
output as transformed sources are generated and as traces are created. Finally, you
should be able to see some results from an example python script written to query
vectors learned from the open source project redis.

### For the artifact containing our raw dataset

For this artifact you should simply see an output directory with our raw traces
and vectors.

---

### NOTE: On docker/file permissions

Some of these docker containers may create artifacts in mounted directories with wonky permissions. This is because the docker container doesn't know the user/group id (on the host) that should own the files it creates.

If you need to remove artifacts created by our tools and are running into permissions errors try using docker to remove those directories/files. Here's an example:

```bash
# Remove the transformed sources for redis
rm -rf ./c2ocaml/artifacts/redis
rm: cannot remove './c2ocaml/artifacts/redis': Permission denied

# Okay, let's mount it with docker and remove it that way
docker run -it --rm -v `pwd`/c2ocaml/artifacts:/mnt debian:stretch
> rm -rf /mnt/redis
> exit

# All good now! ./c2ocaml/artifacts/redis should be totally removed
```
