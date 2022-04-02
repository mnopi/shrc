#!/usr/bin/env bash

#
# install prefix for development, development variables and setup $PATH for testing and development

[  "${BASH_SOURCE-}" ] || return 0

# Build Python with Dependencies Build from Source in $DEV_PREFIX
#
export DEV_DEPS=1

# Installation Prefix for Development
#
export DEV_PREFIX="/opt"

# Python Major Minor Version
#
export PYTHON_VERSION="3.10"

#######################################
# wrapper for command -v
# Arguments:
#  1    command to check
#######################################
_has() { command -v "$1" >/dev/null; }

#######################################
# sources completions in $DEV_PREFIX and/or default completions in brew or /usr/local if not sourced already
# Globals:
#   DEV_PREFIX
#   PS1
#   __DEV_COMPLETION_SOURCED
#   __brew_completion
# Arguments:
#  None
#######################################
__dev_completion() {
  local __brew_completion
  if _has autoload && ! _has bashcompinit; then
    autoload -U +X bashcompinit && bashcompinit
  fi
  if ! _has _split_longopt &>/dev/null; then
    ! test -f /usr/share/bash-completion/bash_completion || . /usr/share/bash-completion/bash_completion
    __brew_completion="$(brew --prefix 2>/dev/null)/etc/profile.d/bash_completion.sh"
    [ ! -f "${__brew_completion}" ] || . "${__brew_completion}"
  fi
  __DEV_COMPLETION_SOURCED="${DEV_PREFIX}/etc/bash_completion.d"
 ! declare -pf _split_longopt &>/dev/null || __dev_source "${__DEV_COMPLETION_SOURCED}"
 ! [[ "${DEV_PREFIX}" =~ /var/|/tmp/ ]] || __dev_source "$(dirname "${1}")/bash_completion.d"
}

#######################################
# sets PATH and MANPATH with script dirname and DEV_PREFIX
# Globals:
#   BASH_SOURCE
#   DEV_BIN
#   DEV_MAN
#   MANPATH
#   PATH
# Arguments:
#   1
#######################################
__dev_paths() {
  if ! _has "${BASH_SOURCE[0]##*/}"; then
    PATH="${1}:${PATH}"
    MANPATH="$(dirname "$1")/share/man${MANPATH:+:${MANPATH%:$''*}}:"
  fi

  if ! [[ "${PATH}" =~ ${DEV_BIN}: ]]; then
    PATH="${DEV_BIN}:${PATH}"
    MANPATH="${DEV_MAN}${MANPATH:+:${MANPATH%:$''*}}:"
  fi
  if [ "${DEV_DEPS-1}" = 1 ] && ! [[ "${LD_LIBRARY_PATH-}" =~ ${DEV_LIB}: ]]; then
    LD_LIBRARY_PATH="${DEV_LIB}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}"
    PKG_CONFIG_PATH="${DEV_LIB}${PKG_CONFIG_PATH:+:${PKG_CONFIG_PATH}}"
  fi
}

#######################################
# sets temp $DEV_PREFIX if this script is under git repository, otherwise use the installed version
# Globals:
#   DEV_PREFIX
# Arguments:
#   1
#######################################
__dev_prefix() { ! git -C "$1" rev-parse --show-toplevel &>/dev/null || DEV_PREFIX="$(mktemp -d)"; }

#######################################
# sources a directory
# Globals:
#   __dev_file
# Arguments:
#   1
#######################################
__dev_source() {
  if test -d "$1" && test -n "$(find "$1" -type f)"; then
    for __dev_file in "$1"/*; do
      [ -f "${__dev_file}" ] || continue
      # shellcheck disable=SC1090
      . "${__dev_file}"
    done
  fi
  unset __dev_file
}

__dev_bash_env="${BASH_ENV-}"; unset BASH_ENV
__dev_dirname="$(cd "$(dirname "${BASH_SOURCE[0]}")" || return 1; pwd -P)"
__dev_prefix "${__dev_dirname}"
[ ! "${PS1-}" ] || [ "${__DEV_COMPLETION_SOURCED-}" ] || __dev_completion "${__dev_dirname}"

if [ ! "${__DEV_ENV_SOURCED-}" ]; then
  export __DEV_ENV_SOURCED="${DEV_PREFIX}/etc/profile.d"
  __dev_source "${__DEV_ENV_SOURCED}"

  # Set if uname is Darwin and unset for Linux
  #
  DARWIN="$(uname -s | grep Darwin || true)"; export DARWIN

  # Set if uname is Darwin and unset for Linux
  #
  DEBIAN="$(grep -i debian /etc/os-release 2>/dev/null || true)"; export DEBIAN

  # Development Install Bin Path
  #
  export DEV_BIN="${DEV_PREFIX}/bin"

  # Development Install Library Path
  #
  export DEV_INCLUDE="${DEV_PREFIX}/include"

  # Development Install Include Headers Path
  #
  export DEV_LIB="${DEV_PREFIX}/lib"

  # Development Install Share Path
  #
  export DEV_SHARE="${DEV_PREFIX}/share"

  # Development Install Share Path
  #
  export DEV_MAN="${DEV_PREFIX}/share/man"

  # Development Install Source Code Path
  #
  export DEV_SRC="${DEV_PREFIX}/src"

  export LD_LIBRARY_PATH
  export MANPATH
  export PKG_CONFIG_PATH

  __dev_root="$(dirname "${DEV_PREFIX}")"
  if [ "${__dev_root}" != "/" ]; then
    if ! test -O "${__dev_root}" || ! test -G "${__dev_root}"; then
      $(command -v sudo) chown -R "$(id -u):$(id -g)" "${__dev_root}"
    fi

    if ! test -w "${__dev_root}"; then
      $(command -v sudo) chmod -R g+w "${__dev_root}"
    fi
  fi

  __dev_paths "${__dev_dirname}"

  if [ "${BASH_SOURCE[0]##*/}" = "${0##*/}" ]; then
    for __dev_variable in DEV_DEPS DEV_PREFIX PYTHON_VERSION \
      DARWIN DEBIAN \
      DEV_BIN DEV_INCLUDE DEV_LIB DEV_SHARE DEV_MAN DEV_SRC \
      LD_LIBRARY_PATH MANPATH PKG_CONFIG_PATH PATH ; do
        echo "export ${__dev_variable}=${!__dev_variable}"
    done
  fi
fi

[ ! "${__dev_bash_env-}" ] || BASH_ENV="${__dev_bash_env}"

unset  __dev_bash_env __dev_dirname __dev_root __dev_variable
unset -f __brew_completion __dev_paths __dev_prefix __dev_source
