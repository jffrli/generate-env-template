# generate-env-template
Generate a basic `env.template` file for [environs](https://pypi.org/project/environs/).

CURRENTLY A WORK IN PROGRESS.

## Supported Environs Features
- default variables 
  - e.g. `env("x")`
- type casted variables
  - e.g. `env.str("x")`
- prefixes
  - e.g. `with env.prefixed("x"):`
