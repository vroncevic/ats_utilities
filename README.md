<img align="right" src="https://raw.githubusercontent.com/vroncevic/ats_utilities/dev/docs/ats_utilities_logo.png" width="25%">

# ATS Utilities

**ats_utilities** is framework for creating/building Apps/Tools/Scripts.

Developed in **[python](https://www.python.org/)** code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/ats_utilities/workflows/Python%20package%20ats_utilities/badge.svg?branch=master) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/ats_utilities.svg)](https://github.com/vroncevic/ats_utilities/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/ats_utilities.svg)](https://github.com/vroncevic/ats_utilities/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
- [Dependencies](#dependencies)
- [Package structure](#package-structure)
- [Docs](#docs)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

![Install Python2 Package](https://github.com/vroncevic/ats_utilities/workflows/Install%20Python2%20Package%20ats_utilities/badge.svg?branch=master) ![Install Python3 Package](https://github.com/vroncevic/ats_utilities/workflows/Install%20Python3%20Package%20ats_utilities/badge.svg?branch=master)

Navigate to **[release page](https://github.com/vroncevic/ats_utilities/releases)** download and extract release archive.

To install modules, locate and run setup.py
```
tar xvzf ats_utilities-x.y.z.tar.gz
cd ats_utilities-x.y.z
pip install -r requirements.txt
```

Install lib process
```
python setup.py install_lib
```

Install lib egg info
```
python setup.py install_egg_info
```

Or You can use docker to create image/container.

[![ats_utilities docker checker](https://github.com/vroncevic/ats_utilities/workflows/ats_utilities%20docker%20checker/badge.svg)](https://github.com/vroncevic/ats_utilities/actions?query=workflow%3A%22ats_utilities+docker+checker%22)

### Dependencies

These modules requires other modules and libraries (Python 2.x/3.x):
* [yaml - YAML parser and emitter for Python](https://pypi.org/project/PyYAML/)
* [bs4 - Screen-scraping library](https://pypi.org/project/beautifulsoup4/)
* [configparser - Configuration parser library](https://pypi.org/project/configparser/)
* [colorama - Cross-platform colored terminal text](https://pypi.org/project/colorama/)
* [pathlib - Object-oriented filesystem paths](https://pypi.org/project/pathlib/)

### Package structure

**ats_utilities** is based on OOP:

![alt tag](https://raw.githubusercontent.com/vroncevic/ats_utilities/dev/docs/arch_flow_usage.png)

Package structure:
```
ats_utilities/
├── abstract/
│   └── __init__.py
├── checker/
│   └── __init__.py
├── cli/
│   ├── cfg_cli.py
│   ├── ini_cli.py
│   ├── __init__.py
│   ├── json_cli.py
│   ├── xml_cli.py
│   └── yaml_cli.py
├── config_io/
│   ├── base_check.py
│   ├── base_read.py
│   ├── base_write.py
│   ├── cfg/
│   │   ├── cfg2object.py
│   │   ├── __init__.py
│   │   └── object2cfg.py
│   ├── ini/
│   │   ├── ini2object.py
│   │   ├── __init__.py
│   │   └── object2ini.py
│   ├── __init__.py
│   ├── json/
│   │   ├── __init__.py
│   │   ├── json2object.py
│   │   └── object2json.py
│   ├── xml/
│   │   ├── __init__.py
│   │   ├── object2xml.py
│   │   └── xml2object.py
│   └── yaml/
│       ├── __init__.py
│       ├── object2yaml.py
│       └── yaml2object.py
├── console_io/
│   ├── error.py
│   ├── __init__.py
│   ├── success.py
│   ├── verbose.py
│   └── warning.py
├── exceptions/
│   ├── ats_attribute_error.py
│   ├── ats_bad_call_error.py
│   ├── ats_file_error.py
│   ├── ats_key_error.py
│   ├── ats_lookup_error.py
│   ├── ats_type_error.py
│   ├── ats_value_error.py
│   └── __init__.py
├── info/
│   ├── ats_build_date.py
│   ├── ats_info_ok.py
│   ├── ats_license.py
│   ├── ats_name.py
│   ├── ats_version.py
│   └── __init__.py
├── __init__.py
├── logging/
│   ├── ats_logger_file.py
│   ├── ats_logger_name.py
│   ├── ats_logger_status.py
│   └── __init__.py
├── option/
│   └── __init__.py
└── register/
    └── __init__.py
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/ats-utilities/badge/?version=latest)](https://ats-utilities.readthedocs.io/projects/ats-utilities/en/latest/?badge=latest)

More documentation and info at:
* [ats-utilities.readthedocs.io](https://ats-utilities.readthedocs.io/en/latest/)
* [www.python.org](https://www.python.org/)

### Copyright and Licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2017 by [vroncevic.github.io/ats_utilities](https://vroncevic.github.io/ats_utilities/)

**ats_utilities** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/ats_utilities/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
