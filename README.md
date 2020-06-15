# Python Utilities

**ats_utilities** is framework for building Apps/Tools/Scripts.

Developed in python code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/ats_utilities/workflows/Python%20package%20ats_utilities/badge.svg?branch=master) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/ats_utilities.svg)](https://github.com/vroncevic/ats_utilities/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/ats_utilities.svg)](https://github.com/vroncevic/ats_utilities/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
- [Dependencies](#dependencies)
- [Library structure](#library-structure)
- [Docs](#docs)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

![Install Python2 Package](https://github.com/vroncevic/ats_utilities/workflows/Install%20Python2%20Package%20ats_utilities/badge.svg?branch=master) ![Install Python3 Package](https://github.com/vroncevic/ats_utilities/workflows/Install%20Python3%20Package%20ats_utilities/badge.svg?branch=master)

Navigate to **[release page](https://github.com/vroncevic/ats_utilities/releases)** download and extract release archive.

To install modules, locate and run setup.py, type the following:
```
tar xvzf ats_utilities-x.y.z.tar.gz
cd ats_utilities-x.y.z
```


```
python setup.py install_lib
```
<details>
  <summary>install lib process</summary>

    root@debtux:/data/dev/python/ats_utilities/github/ats_utilities# python setup.py install_lib<br/>
    running install_lib<br/>
    running build_py<br/>
    creating build<br/>
    creating build/lib.linux-x86_64-2.7<br/>
    creating build/lib.linux-x86_64-2.7/ats_utilities<br/>
    copying ats_utilities/__init__.py -> build/lib.linux-x86_64-2.7/ats_utilities<br/>
    copying ats_utilities/xml_base.py -> build/lib.linux-x86_64-2.7/ats_utilities<br/>
    copying ats_utilities/yaml_base.py -> build/lib.linux-x86_64-2.7/ats_utilities<br/>
    copying ats_utilities/ini_base.py -> build/lib.linux-x86_64-2.7/ats_utilities<br/>
    copying ats_utilities/cfg_base.py -> build/lib.linux-x86_64-2.7/ats_utilities<br/>
    copying ats_utilities/json_base.py -> build/lib.linux-x86_64-2.7/ats_utilities<br/>
    copying ats_utilities/ats_info.py -> build/lib.linux-x86_64-2.7/ats_utilities<br/>
    creating build/lib.linux-x86_64-2.7/ats_utilities/abstract<br/>
    copying ats_utilities/abstract/__init__.py -> build/lib.linux-x86_64-2.7/ats_utilities/abstract<br/>
    creating build/lib.linux-x86_64-2.7/ats_utilities/config<br/>
    copying ats_utilities/config/base_read_config.py -> build/lib.linux-x86_64-2.7/ats_utilities/config<br/>
    copying ats_utilities/config/check_base_config.py -> build/lib.linux-x86_64-2.7/ats_utilities/config<br/>
    copying ats_utilities/config/config_context_manager.py -> build/lib.linux-x86_64-2.7/ats_utilities/config<br/>
    copying ats_utilities/config/__init__.py -> build/lib.linux-x86_64-2.7/ats_utilities/config<br/>
    copying ats_utilities/config/file_checking.py -> build/lib.linux-x86_64-2.7/ats_utilities/config<br/>
    copying ats_utilities/config/base_write_config.py -> build/lib.linux-x86_64-2.7/ats_utilities/config<br/>
    creating build/lib.linux-x86_64-2.7/ats_utilities/config/cfg<br/>
    copying ats_utilities/config/cfg/object2cfg.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/cfg<br/>
    copying ats_utilities/config/cfg/cfg2object.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/cfg<br/>
    copying ats_utilities/config/cfg/__init__.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/cfg<br/>
    creating build/lib.linux-x86_64-2.7/ats_utilities/config/ini<br/>
    copying ats_utilities/config/ini/ini2object.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/ini<br/>
    copying ats_utilities/config/ini/object2ini.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/ini<br/>
    copying ats_utilities/config/ini/__init__.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/ini<br/>
    creating build/lib.linux-x86_64-2.7/ats_utilities/config/json<br/>
    copying ats_utilities/config/json/object2json.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/json<br/>
    copying ats_utilities/config/json/__init__.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/json<br/>
    copying ats_utilities/config/json/json2object.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/json<br/>
    creating build/lib.linux-x86_64-2.7/ats_utilities/config/xml<br/>
    copying ats_utilities/config/xml/xml2object.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/xml<br/>
    copying ats_utilities/config/xml/object2xml.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/xml<br/>
    copying ats_utilities/config/xml/__init__.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/xml<br/>
    creating build/lib.linux-x86_64-2.7/ats_utilities/config/yaml<br/>
    copying ats_utilities/config/yaml/__init__.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/yaml<br/>
    copying ats_utilities/config/yaml/yaml2object.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/yaml<br/>
    copying ats_utilities/config/yaml/object2yaml.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/yaml<br/>
    creating build/lib.linux-x86_64-2.7/ats_utilities/console_io<br/>
    copying ats_utilities/console_io/warning.py -> build/lib.linux-x86_64-2.7/ats_utilities/console_io<br/>
    copying ats_utilities/console_io/verbose.py -> build/lib.linux-x86_64-2.7/ats_utilities/console_io<br/>
    copying ats_utilities/console_io/__init__.py -> build/lib.linux-x86_64-2.7/ats_utilities/console_io<br/>
    copying ats_utilities/console_io/success.py -> build/lib.linux-x86_64-2.7/ats_utilities/console_io<br/>
    copying ats_utilities/console_io/error.py -> build/lib.linux-x86_64-2.7/ats_utilities/console_io<br/>
    creating build/lib.linux-x86_64-2.7/ats_utilities/exceptions<br/>
    copying ats_utilities/exceptions/ats_lookup_error.py -> build/lib.linux-x86_64-2.7/ats_utilities/exceptions<br/>
    copying ats_utilities/exceptions/__init__.py -> build/lib.linux-x86_64-2.7/ats_utilities/exceptions<br/>
    copying ats_utilities/exceptions/ats_bad_call_error.py -> build/lib.linux-x86_64-2.7/ats_utilities/exceptions<br/>
    copying ats_utilities/exceptions/ats_value_error.py -> build/lib.linux-x86_64-2.7/ats_utilities/exceptions<br/>
    copying ats_utilities/exceptions/ats_type_error.py -> build/lib.linux-x86_64-2.7/ats_utilities/exceptions<br/>
    copying ats_utilities/exceptions/ats_key_error.py -> build/lib.linux-x86_64-2.7/ats_utilities/exceptions<br/>
    copying ats_utilities/exceptions/ats_attribute_error.py -> build/lib.linux-x86_64-2.7/ats_utilities/exceptions<br/>
    copying ats_utilities/exceptions/ats_file_error.py -> build/lib.linux-x86_64-2.7/ats_utilities/exceptions<br/>
    creating build/lib.linux-x86_64-2.7/ats_utilities/logging<br/>
    copying ats_utilities/logging/ats_logger_status.py -> build/lib.linux-x86_64-2.7/ats_utilities/logging<br/>
    copying ats_utilities/logging/__init__.py -> build/lib.linux-x86_64-2.7/ats_utilities/logging<br/>
    copying ats_utilities/logging/ats_logger.py -> build/lib.linux-x86_64-2.7/ats_utilities/logging<br/>
    copying ats_utilities/logging/ats_logger_name.py -> build/lib.linux-x86_64-2.7/ats_utilities/logging<br/>
    copying ats_utilities/logging/ats_logger_file.py -> build/lib.linux-x86_64-2.7/ats_utilities/logging<br/>
    copying ats_utilities/logging/ats_logger_base.py -> build/lib.linux-x86_64-2.7/ats_utilities/logging<br/>
    creating build/lib.linux-x86_64-2.7/ats_utilities/option<br/>
    copying ats_utilities/option/ats_option_parser.py -> build/lib.linux-x86_64-2.7/ats_utilities/option<br/>
    copying ats_utilities/option/__init__.py -> build/lib.linux-x86_64-2.7/ats_utilities/option<br/>
    creating build/lib.linux-x86_64-2.7/ats_utilities/register<br/>
    copying ats_utilities/register/__init__.py -> build/lib.linux-x86_64-2.7/ats_utilities/register<br/>
    root@debtux:/data/dev/python/ats_utilities/github/ats_utilities#<br/>
</details>


```
python setup.py install_egg_info
```
<details>
  <summary>install lib egg info</summary>

    root@debtux:/data/dev/python/ats_utilities/github/ats_utilities# python setup.py install_egg_info<br/>
    running install_egg_info<br/>
    running egg_info<br/>
    creating ats_utilities.egg-info<br/>
    writing ats_utilities.egg-info/PKG-INFO<br/>
    writing top-level names to ats_utilities.egg-info/top_level.txt<br/>
    writing dependency_links to ats_utilities.egg-info/dependency_links.txt<br/>
    writing manifest file 'ats_utilities.egg-info/SOURCES.txt'<br/>
    reading manifest file 'ats_utilities.egg-info/SOURCES.txt'<br/>
    writing manifest file 'ats_utilities.egg-info/SOURCES.txt'<br/>
    removing '/usr/local/lib/python2.7/dist-packages/ats_utilities-1.0.2.egg-info' (and everything under it)<br/>
    Copying ats_utilities.egg-info to /usr/local/lib/python2.7/dist-packages/ats_utilities-1.0.2.egg-info<br/>
    root@debtux:/data/dev/python/ats_utilities/github/ats_utilities#<br/>
</details>

Or You can use docker to create image/container.

### Dependencies

These modules requires other modules and libraries (Python 2.x/3.x):
* [yaml - YAML parser and emitter for Python](https://pypi.org/project/PyYAML/)
* [bs4 - Screen-scraping library](https://pypi.org/project/beautifulsoup4/)
* [configparser - Configuration parser library](https://pypi.org/project/configparser/)
* [colorama - Cross-platform colored terminal text](https://pypi.org/project/colorama/)
* [pathlib - Object-oriented filesystem paths](https://pypi.org/project/pathlib/)


### Library structure

**ats_utilities** is based on OOP:

![alt tag](https://raw.githubusercontent.com/vroncevic/ats_utilities/dev/docs/arch_flow_usage.png)

Library structure:
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

### Docs

[![Documentation Status](https://readthedocs.org/projects/ats-utilities/badge/?version=latest)](https://ats-utilities.readthedocs.io/projects/ats-utilities/en/latest/?badge=latest)

More documentation and info at:

* [ats-utilities.readthedocs.io](https://ats-utilities.readthedocs.io/en/latest/)

### Copyright and Licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2018 by [vroncevic.github.io/ats_utilities](https://vroncevic.github.io/ats_utilities/)

This tool is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.
