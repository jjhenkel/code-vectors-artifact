SHELL:=bash

# Cross-platform realpath from 
# https://stackoverflow.com/a/18443300
# NOTE: Adapted for Makefile use
define BASH_FUNC_realpath%%
() {
  OURPWD=$PWD
  cd "$(dirname "$1")"
  LINK=$(readlink "$(basename "$1")")
  while [ "$LINK" ]; do
    cd "$(dirname "$LINK")"
    LINK=$(readlink "$(basename "$1")")
  done
  REALPATH="$PWD/$(basename "$1")"
  cd "$OURPWD"
  echo "$REALPATH"
}
endef
export BASH_FUNC_realpath%%

ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

.DEFAULT_GOAL := help

help: ## This help.
	@grep -E \
		'^[\/\.0-9a-zA-Z_-]+:.*?## .*$$' \
		$(MAKEFILE_LIST) \
		| sort \
		| grep -vF '<HIDE-FROM-HELP>' \
		| awk 'BEGIN {FS = ":.*?## "}; \
		       {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

docker-build: ## Builds the 'madpl/artifacts:analogies-suite' docker image.
	docker build -t madpl/artifacts:analogies-suite --label="madpl" --label="analogies-suite" --label="benchmark" --label="python3" --label="fse-2018" .

reproduce-rq1: docker-build ## Reproduces the results from RQ1 (the Code Analogies Suite, simple similarity, and queries via word-vector averaging).
	docker rm "reproduce-analogies-benchmark" &> /dev/null || true
	docker run -it --rm --name="reproduce-analogies-benchmark" madpl/artifacts:analogies-suite /vectors/vectors-gensim.txt 1
	
check-K: ## Ensures the parameter K (number of similar words to retrieve when solving analogies) is set. <HIDE-FROM-HELP>
ifndef K
	$(error K must be specified; K is the number of similar words to retrieve when solving analogies. Try `K=1 VECS=my-gensim-vectors.txt make run`)
endif

check-VECS: ## Ensures a path to a set of gensim compatible word-vectors is specified. <HIDE-FROM-HELP>
ifndef VECS
	$(error VECS must be specified; VECS is the name of your gensim compatible word vectors (stored in as .txt / not binary). Try `K=1 VECS=my-gensim-vectors.txt make run`)
endif

run-code-analogies: check-VECS check-K docker-build ## Runs the Code Analogies Suite against user provided parameters.
	docker rm "run-analogies-benchmark" &> /dev/null || true
	docker run -it --rm --name="run-analogies-benchmark" -v ${ROOT_DIR}:/mount madpl/artifacts:analogies-suite /mount/${VECS} ${K} 

interactive: check-VECS docker-build ## Runs an interactive session to allow for word-vector similarity queries.
	docker rm "interactive-analogies-benchmark" &> /dev/null || true
	docker run -it --rm --name="interactive-analogies-benchmark" -v ${ROOT_DIR}:/mount madpl/artifacts:analogies-suite /mount/${VECS} INTERACTIVE
	
.PHONY: docker-build
.PHONY: check-K
.PHONY: check-VECS
.PHONY: reproduce-rq1
.PHONY: interactive
.PHONY: run-code-analogies
