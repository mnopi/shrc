# coding=utf-8
"""
System Environment Variables
"""
__all__ = (
  "GIT",
  "INTERNET",
  "EMAIL",
  "ORG",
  "TOKEN",
  "HTTPASSWD_BCRYPT_INTERNET",

  "CF_ACCOUNT_ID",
  "CF_API_KEY",
  "CF_API_TOKEN",
  "CF_CA_KEY",
  "CF_EMAIL",
  "CF_ZONE_ID",
  "CF_API_EMAIL",
  "CF_API_DOMAIN",

  "DOCKER_HUB_TOKEN",
  "DOCKER_SYNC_TOKEN",

  "DOPPLER_TOKEN",
  "DOPPLER_ENV",

  "DUCKDNS_TOKEN",

  "FLIT_PASSWORD",
  "FLIT_USERNAME",

  "GH_TOKEN",

  "GITHUB_TOKEN",

  "HOMEBREW_GITHUB_API_TOKEN",

  "ID_RSA",
  "ID_RSA_PUB",

  "JETBRAINS_PERMANET_TOKEN",

  "NPM_EMAIL",
  "NPM_REGISTRY",
  "NPM_SCOPE",
  "NPM_TOKEN",
  "NPM_USER",
  "NPM_PUBLISH",

  "PYPI_API_TOKEN",
  "PYPI_CLEANUP_PASSWORD",

  "SCALEWAY_SECRET_KEY",
  "SCALEWAY_ACCESS_KEY",
  "SCW_TOKEN",
  "SCALEWAY_ORGANIZATION_ID",
  "SCALEWAY_ENDPOINT",

  "TWINE_PASSWORD",
  "TWINE_USER",

  "TWITTER_CONSUMER_API_KEY",
  "TWITTER_CONSUMER_API_SECRET_KEY",
  "TWITTER_ACCESS_TOKEN",
  "TWITTER_ACCESS_TOKEN_SECRET",

  "VERCEL_TOKEN",

  "VULTR_API_KEY",
)

from .noset import Noset
from .noset import NOSET

"""GitHub User"""
GIT: str | Noset | None = NOSET
"""Internet Password"""
INTERNET: str | Noset | None = NOSET
"""User Email"""
EMAIL: str | Noset | None = NOSET
"""GitHub Organization"""
ORG: str | Noset | None = NOSET
"""GitHub Token"""
TOKEN: str | Noset | None = NOSET
"""Bcrypt Http User Password"""
HTTPASSWD_BCRYPT_INTERNET: str | Noset | None = NOSET

CF_ACCOUNT_ID: str | Noset | None = NOSET
CF_API_KEY: str | Noset | None = NOSET
CF_API_TOKEN: str | Noset | None = NOSET
CF_CA_KEY: str | Noset | None = NOSET
CF_EMAIL: str | Noset | None = NOSET
CF_ZONE_ID: str | Noset | None = NOSET
CF_API_EMAIL: str | Noset | None = NOSET
CF_API_DOMAIN: str | Noset | None = NOSET

DOCKER_HUB_TOKEN: str | Noset | None = NOSET
DOCKER_SYNC_TOKEN: str | Noset | None = NOSET

DOPPLER_TOKEN: str | Noset | None = NOSET
DOPPLER_ENV: str | Noset | None = NOSET

DUCKDNS_TOKEN: str | Noset | None = NOSET

FLIT_PASSWORD: str | Noset | None = NOSET
FLIT_USERNAME: str | Noset | None = NOSET

GH_TOKEN: str | Noset | None = NOSET

GITHUB_TOKEN: str | Noset | None = NOSET

HOMEBREW_GITHUB_API_TOKEN: str | Noset | None = NOSET

ID_RSA: str | Noset | None = NOSET
ID_RSA_PUB: str | Noset | None = NOSET

JETBRAINS_PERMANET_TOKEN: str | Noset | None = NOSET

NPM_EMAIL: str | Noset | None = NOSET
NPM_REGISTRY: str | Noset | None = NOSET
NPM_SCOPE: str | Noset | None = NOSET
NPM_TOKEN: str | Noset | None = NOSET
NPM_USER: str | Noset | None = NOSET
NPM_PUBLISH: str | Noset | None = NOSET

PYPI_API_TOKEN: str | Noset | None = NOSET
PYPI_CLEANUP_PASSWORD: str | Noset | None = NOSET

SCALEWAY_SECRET_KEY: str | Noset | None = NOSET
SCALEWAY_ACCESS_KEY: str | Noset | None = NOSET
SCW_TOKEN: str | Noset | None = NOSET
SCALEWAY_ORGANIZATION_ID: str | Noset | None = NOSET
SCALEWAY_ENDPOINT: str | Noset | None = NOSET

TWINE_PASSWORD: str | Noset | None = NOSET
TWINE_USER: str | Noset | None = NOSET

TWITTER_CONSUMER_API_KEY: str | Noset | None = NOSET
TWITTER_CONSUMER_API_SECRET_KEY: str | Noset | None = NOSET
TWITTER_ACCESS_TOKEN: str | Noset | None = NOSET
TWITTER_ACCESS_TOKEN_SECRET: str | Noset | None = NOSET

VERCEL_TOKEN: str | Noset | None = NOSET

VULTR_API_KEY: str | Noset | None = NOSET
