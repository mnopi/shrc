# [shrc](https://github.com/j5pu/shrc)
![shrc](./.idea/icon.svg)
[![Build Status](https://github.com/j5pu/shrc/workflows/main/badge.svg)](https://github.com/j5pu/shrc/actions/workflows/main.yaml)
[![tap](https://github.com/j5pu/homebrew-tap/workflows/main/badge.svg)](https://github.com/j5pu/homebrew-tap/actions)

macOS and Linux Environment

## [action](./action.yml)
Multi Language Releaser Action and Scripts

### Examples:
```yaml
name: main

on:
  push:
  release:
  workflow_dispatch:

env:
  GITHUB_TOKEN: ${{ secrets.GH_TOKEN }}

jobs:
  tests:
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: true
      matrix:
        os: [ macos-latest, macos-10.15, ubuntu-latest, ubuntu-18.04 ]
    steps:
      - uses: actions/checkout@v3
      - uses: Homebrew/actions/setup-homebrew@master
        if: runner.os == 'macOS'
      - run: ./tests

  release:
    needs: [ tests ]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@main
        with:
          fetch-depth: 0
          token: "${{ env.GITHUB_TOKEN }}"
      - id: release
        uses: j5pu/shrc@main
```

## [bats.bash](./bin/bats.bash)
Bats helpers

### Install

````shell
brew install j5pu/tap/shrc
bats.bash --help
````

### JetBrains

![PathVariables.png](./assets/Path%20Variables.png)
![Terminal.png](./assets/Terminal.png)

### [.env](.env)

```shell
# shellcheck disable=SC2034

BATS_BASH=$PROJECT_BATS_BASH$
BATS_NUMBER_OF_PARALLEL_JOBS=600
PATH="${BATS_BASH}/bin:${PATH}"
```

### [.envrc](.envrc)

````shell
BATS_BASH="$( cd "$(dirname "${BASH_SOURCE:-$0}")"; pwd -P )"; export BATS_BASH
eval "$(awk 'FNR > 1 { print "export " $0 }' "${BATS_BASH}/.env" | grep -v "^$" | sed 's/^/export /g')"

````

### [tests_helper.bats](tests/helpers/tests_helper.bash)

```shell
source bats.bats
```

### [test.bats](tests/func::exported.bats)

````shell
#!/usr/bin/env bats

setup_file() {
  load helpers/tests_helper
}
````
