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

from .utils import environment

GIT: str
"""GitHub User"""
INTERNET: str
"""Internet Password"""
EMAIL: str
"""User Email"""
ORG: str
"""GitHub Organization"""
TOKEN: str
"""GitHub Token"""
HTTPASSWD_BCRYPT_INTERNET: str
"""Bcrypt Http User Password"""

CF_ACCOUNT_ID: str
CF_API_KEY: str
CF_API_TOKEN: str
CF_CA_KEY: str
CF_EMAIL: str
CF_ZONE_ID: str
CF_API_EMAIL: str
CF_API_DOMAIN: str

DOCKER_HUB_TOKEN: str
DOCKER_SYNC_TOKEN: str

DOPPLER_TOKEN: str
DOPPLER_ENV: str

DUCKDNS_TOKEN: str

FLIT_PASSWORD: str
FLIT_USERNAME: str

GH_TOKEN: str

GITHUB_TOKEN: str

HOMEBREW_GITHUB_API_TOKEN: str

ID_RSA: str
ID_RSA_PUB: str

JETBRAINS_PERMANET_TOKEN: str

NPM_EMAIL: str
NPM_REGISTRY: str
NPM_SCOPE: str
NPM_TOKEN: str
NPM_USER: str
NPM_PUBLISH: str

PYPI_API_TOKEN: str
PYPI_CLEANUP_PASSWORD: str

SCALEWAY_SECRET_KEY: str
SCALEWAY_ACCESS_KEY: str
SCW_TOKEN: str
SCALEWAY_ORGANIZATION_ID: str
SCALEWAY_ENDPOINT: str

TWINE_PASSWORD: str
TWINE_USER: str

TWITTER_CONSUMER_API_KEY: str
TWITTER_CONSUMER_API_SECRET_KEY: str
TWITTER_ACCESS_TOKEN: str
TWITTER_ACCESS_TOKEN_SECRET: str

VERCEL_TOKEN: str

VULTR_API_KEY: str

environment()
