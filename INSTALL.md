# Installing this artifact

## Prerequisites

This artifact makes heavy use of Docker and Docker Hub. As a prerequisite this artifact assumes the user has the following:

1. A machine running some Linux distribution (or OSX) and a working terminal. 
2. A working installation of Make and Git.
3. A working installation of docker (`docker run hello-world` produces output without errors).

## Installing and running an end-to-end demonstration

Given these prerequisites installing this artifact should be easy. To install follow these steps:

1. git clone https://github.com/jjhenkel/code-vectors-artifact
2. cd ./code-vectors-artifact
3. make end-to-end-test-hexchat

### What `make end-to-end-test-hexchat` is doing

If you were able to run the above three command successfully you have done the following:

1. Used our `spec2image` tool to create a docker image (locally) containing the `hexchat` program's source files and steps to build that program from those source files.
2. Built that program (in a container) with our custom version of GCC 7.2.0 running our `c2ocaml` plugin. 
3. Created an OCaml file for each procedure GCC/G++ encountered while building the `hexchat` application from source.
4. Grouped and merged these transformed OCaml files into larger chunks.
5. Ran (in parallel) our `lsee` tool on these merged OCaml files to produce abstracted symbolic traces.
6. Merged the abstracted symbolic traces into a single trace corpus named `hexchat.traces.txt`.
7. Used Standford NLP's GloVe tool to learn vectors from that trace corpus.

That's a lot of cool stuff! 

## Running experiments (to reproduce the results reported in our paper)

In addition to our end-to-end toolchain demonstrations, we have provided routines to reproduce each of our experiments. These reproductions do NOT including running our toolchain on Linux end-to-end (as this takes about 4 hours on our 64 core workstation). Instead, we have opted to provide pre-baked vectors.


