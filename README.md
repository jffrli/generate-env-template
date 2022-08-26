# generate-env-template
Generate a basic `env.template` file for a `.py` source file using [environs](https://pypi.org/project/environs/). 
Variables will be in the same order as they first appear in the source file.

## Usage
`python3 generate-env-template.py [source].py`

The resulting `env.template` file will be generated in the same directory as the input source file.  
Note: Any file with the same name in the destination folder will be overwritten.

## Supported Environs Features
- default variables 
  - e.g. `env("x")`
- type casted variables
  - e.g. `env.str("x")`
  - Note: optional arguments not supported
- prefixes
  - e.g. `with env.prefixed("x"):`

### Variable Arguments
This program only supports variable arguments for prefixes, in a specific format.  
Prefixes should be placed in a single-line comment, comma separated, with no whitespace in between.

```
with env.prefixed(x): #prefix1,prefix2,prefix3
  ENV_VAR = env("VAR")
```  
will result in
```
prefix1VAR=
prefix2VAR=
prefix3VAR=
```

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
