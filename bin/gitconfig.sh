# shellcheck shell=sh

set -a
GIT_CONFIG_SYSTEM="$(command -v .gitconfig)"
GIT_TEMPLATE_DIR="${GIT_CONFIG_SYSTEM:+$(dirname "${GIT_CONFIG_SYSTEM}")/template}"

[ ! "${GITHUB_ACTION-}" ] || { set +a; return; }

GIT_CONFIG_COUNT=4
GIT_CONFIG_KEY_0='url.ssh://git@github.com/.insteadOf';
GIT_CONFIG_VALUE_0="$(! ssh -T git@github.com 2>&1 | grep -q "successfully authenticated" || echo https://github.com/ )"
GIT_CONFIG_KEY_1="credential.credentialStore"
GIT_CONFIG_VALUE_1="$(if [ "$(uname -s)" = 'Darwin' ]; then echo keychain; elif command -v secret-tool >/dev/null; \
then echo secretservice; else echo plaintext; fi)"
GIT_CONFIG_KEY_2="credential.helper"
GIT_CONFIG_VALUE_2="$(command -v git-credential-manager-core)"
GIT_CONFIG_KEY_3='credential."https://dev.azure.com".useHttpPath'
GIT_CONFIG_VALUE_3="${GIT_CONFIG_VALUE_2:+true}"

set +a

# git ls-remote --get-url
# git config credential.credentialStore
# git config credential.helper
# git config credential."https://dev.azure.com".useHttpPath
