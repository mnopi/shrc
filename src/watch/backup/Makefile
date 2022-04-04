.PHONY: build chmod install test

SHELL := $(shell command -v bash)

clean: 
	@sudo rm -rf build dist

build: chmod
	@sudo python3 -m build  -o $$(mktemp -d)

chmod:
	@chmod -R +x bin/* 2>/dev/null || true

# https://pip.pypa.io/en/stable/topics/configuration/
# sudo python3 -m pip config --global set name value
install:
	@sudo python3.10 -m pip --quiet uninstall -y $$(basename "$$PWD") 
	@sudo python3.10 -m pip --quiet install --upgrade --no-cache --only-binary :all: $$(basename "$$PWD") 
	@secho || true

local: clean
	@sudo python3.10 -m pip --quiet install --only-binary :all: .

test:
	@pytest

