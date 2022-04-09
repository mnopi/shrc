# shellcheck shell=sh

#
# sets "shrc" package/module/respository environment variables and functions for production and testing

# Path to 'shenv'
#
: "${SHRC?parameter not set, usage: eval "\$(shrc shenv)", see: shenv --help}"; export SHENV

# SHRC Package/Module/Repository Name
#
SHRC_NAME="shrc"; export SHRC_NAME
