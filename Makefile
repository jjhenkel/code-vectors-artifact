SHELL=/bin/bash

ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

.PHONY: help
.PHONY: submodules
.PHONY: c2ocaml
.PHONY: lsee
.PHONY: end-to-end-redis
.PHONY: end-to-end-nginx
.PHONY: end-to-end-hexchat
.PHONY: end-to-end-nmap
.PHONY: end-to-end-curl
.PHONY: end-to-end-linux

.DEFAULT_GOAL := help

help: ## This help.
	@grep -E \
		'^[\/\.0-9a-zA-Z_-]+:.*?## .*$$' \
		$(MAKEFILE_LIST) \
		| sort \
		| awk 'BEGIN {FS = ":.*?## "}; \
		       {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

submodules: ## Ensures that submodules are setup.
	git submodule init
	git submodule update --remote

c2ocaml: submodules ## Ensures that c2ocaml is cloned and setup.
	@echo "[code-vectors] Ensuring that we have c2ocaml"
	docker pull jjhenkel/c2ocaml

lsee: submodules ## Ensures that the lsee is cloned and setup.
	@echo "[code-vectors] Ensuring we have lsee"
	docker pull jjhenkel/lsee
	# TODO

end-to-end-redis: lsee c2ocaml ## Runs the toolchain end-to-end on redi.
	@echo "[code-vectors] Running end-to-end pipeline on redis..."
	@echo "[code-vectors] Transforming sources..."
	pushd ${ROOT_DIR}/c2ocaml ; make redis ; popd
	@echo "[code-vectors] Generating traces..."
	pushd ${ROOT_DIR}/lsee ; make redis ; popd
	@echo "[code-vectors] Collecting traces..."
	pushd ${ROOT_DIR}/lsee ; NAME=redis make collect ; popd
	@echo "[code-vectors] Learning vectors..."
	@echo "[code-vectors] Completed end-to-end run on redis!"

end-to-end-nginx: lsee c2ocaml  ## Runs the toolchain end-to-end on nginx.
	@echo "[code-vectors] Running end-to-end pipeline on nginx..."

end-to-end-hexchat: lsee c2ocaml ## Runs the toolchain end-to-end on curl.
	@echo "[code-vectors] Running end-to-end pipeline on hexchat..."

end-to-end-nmap: lsee c2ocaml ## Runs the toolchain end-to-end on nmap.
	@echo "[code-vectors] Running end-to-end pipeline on nmap..."

end-to-end-curl: lsee c2ocaml ## Runs the toolchain end-to-end on curl.
	@echo "[code-vectors] Running end-to-end pipeline on curl..."

end-to-end-linux: lsee c2ocaml ## Runs the toolchain end-to-end on linux. VERY SLOW.
	@echo "[code-vectors] Running end-to-end pipeline on linux (WARNING: VERY SLOW)..."
