.PHONY: publish tests

SHELL := $(shell bash -c 'command -v bash')
msg := fix: completions
export msg

publish: tests
	@git add .
	@git commit --quiet -a -m "$${msg:-auto}"
	@git push --quiet

tests:
	@brew bundle --file tests/Brewfile --quiet --no-lock | grep -v "^Using"
	@bin/bats.bash run
	@./tests/test_version
