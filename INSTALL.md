# Installing this artifact

## Prerequisites (for reproducing our experiments)

This artifact makes heave use of Docker and Docker Hub. To reproduce our experiments
we assume the user has the following:

1. A machine with a working installation of Docker.
2. A good internet connection.

We have tested our docker images on both Linux clients (Ubuntu/Debian and CentOS) as well
as a Windows laptop with docker installed.

## Running experiments (to reproduce the results reported in our paper)

In addition to our end-to-end toolchain demonstrations (descried below), we have provided routines to reproduce each of our experiments. These reproductions do NOT include running our toolchain on Linux end-to-end (as this takes about 4 hours on our 64 core workstation). Instead, we have opted to provide pre-baked vectors.

### Reproducing rq1

See [reproduce/rq1/README.md](reproduce/rq1/README.md) or just run the following:

```bash
docker pull jjhenkel/code-vectors-artifact:rq1
docker run -it --rm jjhenkel/code-vectors-artifact:rq1
```

### Reproducing rq2

WARNING: can take up to `4 hours` and `6 GB` of space. (Runtime on a 8-core desktop machine is about `3 hours`.)

See [reproduce/rq2/README.md](reproduce/rq2/README.md) or just run the following:

```bash
docker pull jjhenkel/code-vectors-artifact:rq2
docker run -it --rm jjhenkel/code-vectors-artifact:rq2
```

### Reproducing rq3

NOTE: can take up to `1 hour` and `2 GB` of space.

See [reproduce/rq3/README.md](reproduce/rq3/README.md) or just run the following:

```bash
docker pull jjhenkel/code-vectors-artifact:rq3
docker run -it --rm jjhenkel/code-vectors-artifact:rq3
```

### Reproducing rq4

See [reproduce/rq4/README.md](reproduce/rq4/README.md) or just run the following:

```bash
docker pull jjhenkel/code-vectors-artifact:rq4
docker run -it --rm jjhenkel/code-vectors-artifact:rq4
```

---

## Prerequisites (for our end-to-end demo)

This artifact makes heavy use of Docker and Docker Hub. As a prerequisite this artifact assumes the user has the following:

1. A machine running some Linux distribution. (We've tested on Ubuntu/Debian and CentOS.) We've also done some limited testing of the end-to-end demo on OSX, but support for that platform is still experimental.
2. A working installation of Make and Git.
3. A working installation of docker (`docker run hello-world` produces output without errors).

## Installing and running an end-to-end demonstration

Given these prerequisites installing this artifact should be easy. To install follow these steps:

1. `git clone https://github.com/jjhenkel/code-vectors-artifact`
2. `cd ./code-vectors-artifact`
3. `make end-to-end-redis`
4. `make learn-vectors-redis`

### What `make end-to-end-redis` is doing

NOTE: can take up to `3 hours` and `4 GB` of space. (Runtime on a 4-core desktop machine is about an hour.)

If you were able to run the first three commands (listed above) you have done the following:

1. Used our `spec2image` tool to create a docker image (locally) containing the `redis` program's source files and steps to build that program from those source files.
2. Built that program (in a container) with our custom version of GCC 7.3.0 running our `c2ocaml` plugin.
3. Created an OCaml file for each procedure GCC/G++ encountered while building the `redis` application from source.
4. Grouped and merged these transformed OCaml files into larger chunks.
5. Ran (in parallel) our `lsee` tool on these merged OCaml files to produce abstracted symbolic traces.
6. Merged the abstracted symbolic traces into a single trace corpus named `redis.traces.txt`.

That's a lot of cool stuff!

### What `learn-vectors-redis` is doing

**IMPORTANT:** make sure you run `make end-to-end-redis` before attempting to learn vectors.

Here's what `learn-vectors-redis` does:

1. Uses GloVe to build a vocabulary / cooccurence matrix 
2. Learns word vectors using some default parameters
3. Runs a demonstration using some Python and the Gensim library
