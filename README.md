# Python Utilities

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

### INSTALLATION

To install modules, locate and run setup.py, type the following:

```
python setup.py install
```

### DEPENDENCIES

These modules requires other modules and libraries (Python 2/3):

```
sys
logging
distutils
os
yaml
bs4
json
configparser
optparse
re
inspect
Exception
ImportError
LookupError
IOError
TypeError
ValueError
AttributeError
KeyError
colorama
datetime
pathlib
```

### Testing framework

```
unittest
```

### COPYRIGHT AND LICENCE

Copyright (C) 2018 by https://vroncevic.github.io/ats_utilities/

This tool is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.7/3.4 or,
at your option, any later version of Python 3 you may have available.

:sparkles:

### Library structure

```
.
├── ats_utilities/
│   ├── abstract/
│   │   └── __init__.py
│   ├── ats_info.py
│   ├── cfg_base.py
│   ├── config/
│   │   ├── base_read_config.py
│   │   ├── base_write_config.py
│   │   ├── cfg/
│   │   │   ├── cfg2object.py
│   │   │   ├── __init__.py
│   │   │   └── object2cfg.py
│   │   ├── check_base_config.py
│   │   ├── config_context_manager.py
│   │   ├── file_checking.py
│   │   ├── ini/
│   │   │   ├── ini2object.py
│   │   │   ├── __init__.py
│   │   │   └── object2ini.py
│   │   ├── __init__.py
│   │   ├── json/
│   │   │   ├── __init__.py
│   │   │   ├── json2object.py
│   │   │   └── object2json.py
│   │   ├── xml/
│   │   │   ├── __init__.py
│   │   │   ├── object2xml.py
│   │   │   └── xml2object.py
│   │   └── yaml/
│   │       ├── __init__.py
│   │       ├── object2yaml.py
│   │       └── yaml2object.py
│   ├── console_io/
│   │   ├── error.py
│   │   ├── __init__.py
│   │   ├── success.py
│   │   ├── verbose.py
│   │   └── warning.py
│   ├── exceptions/
│   │   ├── ats_attribute_error.py
│   │   ├── ats_bad_call_error.py
│   │   ├── ats_file_error.py
│   │   ├── ats_key_error.py
│   │   ├── ats_lookup_error.py
│   │   ├── ats_type_error.py
│   │   ├── ats_value_error.py
│   │   └── __init__.py
│   ├── ini_base.py
│   ├── __init__.py
│   ├── json_base.py
│   ├── logging/
│   │   ├── ats_logger_base.py
│   │   ├── ats_logger_file.py
│   │   ├── ats_logger_name.py
│   │   ├── ats_logger.py
│   │   ├── ats_logger_status.py
│   │   └── __init__.py
│   ├── option/
│   │   ├── ats_option_parser.py
│   │   └── __init__.py
│   ├── register/
│   │   └── __init__.py
│   ├── xml_base.py
│   └── yaml_base.py
└── setup.py
```

