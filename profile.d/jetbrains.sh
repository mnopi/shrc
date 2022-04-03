# shellcheck shell=sh

[ ! "${JETBRAINS-}" ] || return 0

set -a
JETBRAINS="/Users/Shared/JetBrains"
JETBRAINS_APPLICATIONS="${JETBRAINS}/Applications"
JETBRAINS_CACHES="${JETBRAINS}/Caches"
JETBRAINS_CONFIG="PyCharm"
JETBRAINS_LIBRARY="${JETBRAINS}/Library"
JETBRAINS_NAMES="AppCode DataGrip Gateway GoLand Idea PyCharm RubyMine WebStorm"
set +a