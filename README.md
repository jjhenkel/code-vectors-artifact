# Artifact Repository for "Code Vectors" ESEC/FSE'18 Paper

## Important Info

The contact author for this artifact is Jordan Henkel <jjhenkel@cs.wisc.edu>. The ESEC/FSE'18 paper ID is 149 (Code Vectors: Understanding Programs Through Embedded Abstracted Symbolic Traces).

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
