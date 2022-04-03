.PHONY: brew build chmod clean install local publish tests

#BASH_ENV := .envrc
#export BASH_ENV
SHELL := $(shell bash -c 'command -v bash') -e
PACKAGE := $(shell basename "$$PWD")
#msg ?= auto
msg := fix: completions
export msg

brew:
	@brew bundle --file packages/Brewfile --quiet --cleanup --no-lock
	@brew cleanup
	@brew upgrade
	@brew autoremove

build: chmod
	@python3.10 -m build --wheel -o $$(mktemp -d)
	@rm -rf build dist

chmod: clean
	@chmod -R +x bin/* 2>/dev/null || true

clean:
	@rm -rf build dist

# https://pip.pypa.io/en/stable/topics/configuration/
# sudo python3 -m pip config --global set name value
install:
	@python3.10 -m pip --quiet uninstall -y $(PACKAGE)
	@python3.10 -m pip --quiet install --upgrade --no-cache --only-binary :all: $(PACKAGE)
	@$(PACKAGE) || true

local: build
	@python3.10 -m pip --quiet install --only-binary :all: .

publish: tests
	@git add .
	@git commit --quiet -a -m "$${msg:-auto}" || true
	@git push --quiet
	@[ "$(msg)" = "auto" ] || open https://github.com/j5pu/$(PACKAGE)/actions

tests:
	@brew bundle --file tests/Brewfile --quiet --no-lock | grep -v "^Using"
	@bin/bats.bash run
	@./tests/test_version
	@pytest
