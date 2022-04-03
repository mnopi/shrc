.PHONY: brew publish tests

#BASH_ENV := .envrc
#export BASH_ENV

SHELL := $(shell bash -c 'command -v bash') -e
msg := fix: completions
export msg

brew:
	@brew bundle --file packages/Brewfile --quiet --cleanup --no-lock
	@brew cleanup
	@brew upgrade
	@brew autoremove

publish: tests
	@git add .
	@git commit --quiet -a -m "$${msg:-auto}" || true
	@git push --quiet

tests:
	@brew bundle --file tests/Brewfile --quiet --no-lock | grep -v "^Using"
	@bin/bats.bash run
	@./tests/test_version
