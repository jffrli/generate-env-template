# generate-env-template
Generate a basic `env.template` file for a `.py` source file using [environs](https://pypi.org/project/environs/). 
Variables will be in the same order as they first appear in the source file.

## Usage
`python3 generate-env-template.py [source].py`

\[Not yet implemented\]. 
The resulting `env.template` file will be generated in the same directory as the input source file.
Note: Currently, it is generated in the directory where this program is run.


## Supported Environs Features
- default variables 
  - e.g. `env("x")`
- type casted variables
  - e.g. `env.str("x")`
  - Note: optional arguments not supported
- prefixes
  - e.g. `with env.prefixed("x"):`

### Supported type casts (in case the environs list changes)
- str
- bool
- int
- float
- decimal
- list
- dict
- json
- datetime
- date
- time
- timedelta
- url
- uuid
- log_level
- path
- enum
