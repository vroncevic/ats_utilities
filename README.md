# Python Utilities

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
pip install -r requirements.txt
```

Install lib process
```
python setup.py install_lib
running install_lib
running build_py
creating build
creating build/lib.linux-x86_64-2.7
creating build/lib.linux-x86_64-2.7/ats_utilities
copying ats_utilities/__init__.py -> build/lib.linux-x86_64-2.7/ats_utilities
copying ats_utilities/cfg_base.py -> build/lib.linux-x86_64-2.7/ats_utilities
copying ats_utilities/ini_base.py -> build/lib.linux-x86_64-2.7/ats_utilities
copying ats_utilities/ats_info.py -> build/lib.linux-x86_64-2.7/ats_utilities
copying ats_utilities/yaml_base.py -> build/lib.linux-x86_64-2.7/ats_utilities
copying ats_utilities/json_base.py -> build/lib.linux-x86_64-2.7/ats_utilities
copying ats_utilities/xml_base.py -> build/lib.linux-x86_64-2.7/ats_utilities
copying ats_utilities/checker.py -> build/lib.linux-x86_64-2.7/ats_utilities
creating build/lib.linux-x86_64-2.7/ats_utilities/abstract
copying ats_utilities/abstract/__init__.py -> build/lib.linux-x86_64-2.7/ats_utilities/abstract
creating build/lib.linux-x86_64-2.7/ats_utilities/config
copying ats_utilities/config/base_read_config.py -> build/lib.linux-x86_64-2.7/ats_utilities/config
copying ats_utilities/config/config_context_manager.py -> build/lib.linux-x86_64-2.7/ats_utilities/config
copying ats_utilities/config/__init__.py -> build/lib.linux-x86_64-2.7/ats_utilities/config
copying ats_utilities/config/base_write_config.py -> build/lib.linux-x86_64-2.7/ats_utilities/config
copying ats_utilities/config/file_checking.py -> build/lib.linux-x86_64-2.7/ats_utilities/config
copying ats_utilities/config/check_base_config.py -> build/lib.linux-x86_64-2.7/ats_utilities/config
creating build/lib.linux-x86_64-2.7/ats_utilities/config/cfg
copying ats_utilities/config/cfg/__init__.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/cfg
copying ats_utilities/config/cfg/cfg2object.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/cfg
copying ats_utilities/config/cfg/object2cfg.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/cfg
creating build/lib.linux-x86_64-2.7/ats_utilities/config/ini
copying ats_utilities/config/ini/__init__.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/ini
copying ats_utilities/config/ini/object2ini.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/ini
copying ats_utilities/config/ini/ini2object.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/ini
creating build/lib.linux-x86_64-2.7/ats_utilities/config/json
copying ats_utilities/config/json/__init__.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/json
copying ats_utilities/config/json/object2json.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/json
copying ats_utilities/config/json/json2object.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/json
creating build/lib.linux-x86_64-2.7/ats_utilities/config/xml
copying ats_utilities/config/xml/xml2object.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/xml
copying ats_utilities/config/xml/__init__.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/xml
copying ats_utilities/config/xml/object2xml.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/xml
creating build/lib.linux-x86_64-2.7/ats_utilities/config/yaml
copying ats_utilities/config/yaml/yaml2object.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/yaml
copying ats_utilities/config/yaml/__init__.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/yaml
copying ats_utilities/config/yaml/object2yaml.py -> build/lib.linux-x86_64-2.7/ats_utilities/config/yaml
creating build/lib.linux-x86_64-2.7/ats_utilities/console_io
copying ats_utilities/console_io/__init__.py -> build/lib.linux-x86_64-2.7/ats_utilities/console_io
copying ats_utilities/console_io/warning.py -> build/lib.linux-x86_64-2.7/ats_utilities/console_io
copying ats_utilities/console_io/error.py -> build/lib.linux-x86_64-2.7/ats_utilities/console_io
copying ats_utilities/console_io/success.py -> build/lib.linux-x86_64-2.7/ats_utilities/console_io
copying ats_utilities/console_io/verbose.py -> build/lib.linux-x86_64-2.7/ats_utilities/console_io
creating build/lib.linux-x86_64-2.7/ats_utilities/exceptions
copying ats_utilities/exceptions/ats_value_error.py -> build/lib.linux-x86_64-2.7/ats_utilities/exceptions
copying ats_utilities/exceptions/__init__.py -> build/lib.linux-x86_64-2.7/ats_utilities/exceptions
copying ats_utilities/exceptions/ats_type_error.py -> build/lib.linux-x86_64-2.7/ats_utilities/exceptions
copying ats_utilities/exceptions/ats_file_error.py -> build/lib.linux-x86_64-2.7/ats_utilities/exceptions
copying ats_utilities/exceptions/ats_lookup_error.py -> build/lib.linux-x86_64-2.7/ats_utilities/exceptions
copying ats_utilities/exceptions/ats_key_error.py -> build/lib.linux-x86_64-2.7/ats_utilities/exceptions
copying ats_utilities/exceptions/ats_bad_call_error.py -> build/lib.linux-x86_64-2.7/ats_utilities/exceptions
copying ats_utilities/exceptions/ats_attribute_error.py -> build/lib.linux-x86_64-2.7/ats_utilities/exceptions
creating build/lib.linux-x86_64-2.7/ats_utilities/logging
copying ats_utilities/logging/ats_logger_file.py -> build/lib.linux-x86_64-2.7/ats_utilities/logging
copying ats_utilities/logging/ats_logger_base.py -> build/lib.linux-x86_64-2.7/ats_utilities/logging
copying ats_utilities/logging/ats_logger_status.py -> build/lib.linux-x86_64-2.7/ats_utilities/logging
copying ats_utilities/logging/ats_logger.py -> build/lib.linux-x86_64-2.7/ats_utilities/logging
copying ats_utilities/logging/__init__.py -> build/lib.linux-x86_64-2.7/ats_utilities/logging
copying ats_utilities/logging/ats_logger_name.py -> build/lib.linux-x86_64-2.7/ats_utilities/logging
creating build/lib.linux-x86_64-2.7/ats_utilities/option
copying ats_utilities/option/__init__.py -> build/lib.linux-x86_64-2.7/ats_utilities/option
copying ats_utilities/option/ats_option_parser.py -> build/lib.linux-x86_64-2.7/ats_utilities/option
creating build/lib.linux-x86_64-2.7/ats_utilities/register
copying ats_utilities/register/__init__.py -> build/lib.linux-x86_64-2.7/ats_utilities/register
copying build/lib.linux-x86_64-2.7/ats_utilities/__init__.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities
copying build/lib.linux-x86_64-2.7/ats_utilities/config/cfg/__init__.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/config/cfg
copying build/lib.linux-x86_64-2.7/ats_utilities/config/cfg/cfg2object.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/config/cfg
copying build/lib.linux-x86_64-2.7/ats_utilities/config/cfg/object2cfg.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/config/cfg
copying build/lib.linux-x86_64-2.7/ats_utilities/config/base_read_config.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/config
copying build/lib.linux-x86_64-2.7/ats_utilities/config/config_context_manager.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/config
copying build/lib.linux-x86_64-2.7/ats_utilities/config/__init__.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/config
copying build/lib.linux-x86_64-2.7/ats_utilities/config/base_write_config.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/config
copying build/lib.linux-x86_64-2.7/ats_utilities/config/json/__init__.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/config/json
copying build/lib.linux-x86_64-2.7/ats_utilities/config/json/object2json.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/config/json
copying build/lib.linux-x86_64-2.7/ats_utilities/config/json/json2object.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/config/json
copying build/lib.linux-x86_64-2.7/ats_utilities/config/xml/xml2object.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/config/xml
copying build/lib.linux-x86_64-2.7/ats_utilities/config/xml/__init__.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/config/xml
copying build/lib.linux-x86_64-2.7/ats_utilities/config/xml/object2xml.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/config/xml
copying build/lib.linux-x86_64-2.7/ats_utilities/config/file_checking.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/config
copying build/lib.linux-x86_64-2.7/ats_utilities/config/check_base_config.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/config
copying build/lib.linux-x86_64-2.7/ats_utilities/config/yaml/yaml2object.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/config/yaml
copying build/lib.linux-x86_64-2.7/ats_utilities/config/yaml/__init__.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/config/yaml
copying build/lib.linux-x86_64-2.7/ats_utilities/config/yaml/object2yaml.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/config/yaml
copying build/lib.linux-x86_64-2.7/ats_utilities/config/ini/__init__.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/config/ini
copying build/lib.linux-x86_64-2.7/ats_utilities/config/ini/object2ini.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/config/ini
copying build/lib.linux-x86_64-2.7/ats_utilities/config/ini/ini2object.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/config/ini
copying build/lib.linux-x86_64-2.7/ats_utilities/option/__init__.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/option
copying build/lib.linux-x86_64-2.7/ats_utilities/option/ats_option_parser.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/option
copying build/lib.linux-x86_64-2.7/ats_utilities/cfg_base.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities
copying build/lib.linux-x86_64-2.7/ats_utilities/console_io/__init__.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/console_io
copying build/lib.linux-x86_64-2.7/ats_utilities/console_io/warning.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/console_io
copying build/lib.linux-x86_64-2.7/ats_utilities/console_io/error.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/console_io
copying build/lib.linux-x86_64-2.7/ats_utilities/console_io/success.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/console_io
copying build/lib.linux-x86_64-2.7/ats_utilities/console_io/verbose.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/console_io
copying build/lib.linux-x86_64-2.7/ats_utilities/ini_base.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities
copying build/lib.linux-x86_64-2.7/ats_utilities/ats_info.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities
copying build/lib.linux-x86_64-2.7/ats_utilities/yaml_base.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities
copying build/lib.linux-x86_64-2.7/ats_utilities/register/__init__.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/register
copying build/lib.linux-x86_64-2.7/ats_utilities/exceptions/ats_value_error.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/exceptions
copying build/lib.linux-x86_64-2.7/ats_utilities/exceptions/__init__.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/exceptions
copying build/lib.linux-x86_64-2.7/ats_utilities/exceptions/ats_type_error.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/exceptions
copying build/lib.linux-x86_64-2.7/ats_utilities/exceptions/ats_file_error.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/exceptions
copying build/lib.linux-x86_64-2.7/ats_utilities/exceptions/ats_lookup_error.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/exceptions
copying build/lib.linux-x86_64-2.7/ats_utilities/exceptions/ats_key_error.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/exceptions
copying build/lib.linux-x86_64-2.7/ats_utilities/exceptions/ats_bad_call_error.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/exceptions
copying build/lib.linux-x86_64-2.7/ats_utilities/exceptions/ats_attribute_error.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/exceptions
copying build/lib.linux-x86_64-2.7/ats_utilities/json_base.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities
copying build/lib.linux-x86_64-2.7/ats_utilities/xml_base.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities
copying build/lib.linux-x86_64-2.7/ats_utilities/checker.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities
copying build/lib.linux-x86_64-2.7/ats_utilities/logging/ats_logger_file.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/logging
copying build/lib.linux-x86_64-2.7/ats_utilities/logging/ats_logger_base.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/logging
copying build/lib.linux-x86_64-2.7/ats_utilities/logging/ats_logger_status.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/logging
copying build/lib.linux-x86_64-2.7/ats_utilities/logging/ats_logger.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/logging
copying build/lib.linux-x86_64-2.7/ats_utilities/logging/__init__.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/logging
copying build/lib.linux-x86_64-2.7/ats_utilities/logging/ats_logger_name.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/logging
copying build/lib.linux-x86_64-2.7/ats_utilities/abstract/__init__.py -> /usr/local/lib/python2.7/dist-packages/ats_utilities/abstract
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/config/cfg/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/config/cfg/cfg2object.py to cfg2object.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/config/cfg/object2cfg.py to object2cfg.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/config/base_read_config.py to base_read_config.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/config/config_context_manager.py to config_context_manager.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/config/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/config/base_write_config.py to base_write_config.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/config/json/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/config/json/object2json.py to object2json.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/config/json/json2object.py to json2object.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/config/xml/xml2object.py to xml2object.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/config/xml/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/config/xml/object2xml.py to object2xml.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/config/file_checking.py to file_checking.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/config/check_base_config.py to check_base_config.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/config/yaml/yaml2object.py to yaml2object.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/config/yaml/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/config/yaml/object2yaml.py to object2yaml.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/config/ini/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/config/ini/object2ini.py to object2ini.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/config/ini/ini2object.py to ini2object.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/option/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/option/ats_option_parser.py to ats_option_parser.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/cfg_base.py to cfg_base.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/console_io/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/console_io/warning.py to warning.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/console_io/error.py to error.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/console_io/success.py to success.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/console_io/verbose.py to verbose.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/ini_base.py to ini_base.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/ats_info.py to ats_info.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/yaml_base.py to yaml_base.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/register/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/exceptions/ats_value_error.py to ats_value_error.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/exceptions/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/exceptions/ats_type_error.py to ats_type_error.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/exceptions/ats_file_error.py to ats_file_error.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/exceptions/ats_lookup_error.py to ats_lookup_error.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/exceptions/ats_key_error.py to ats_key_error.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/exceptions/ats_bad_call_error.py to ats_bad_call_error.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/exceptions/ats_attribute_error.py to ats_attribute_error.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/json_base.py to json_base.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/xml_base.py to xml_base.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/checker.py to checker.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/logging/ats_logger_file.py to ats_logger_file.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/logging/ats_logger_base.py to ats_logger_base.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/logging/ats_logger_status.py to ats_logger_status.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/logging/ats_logger.py to ats_logger.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/logging/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/logging/ats_logger_name.py to ats_logger_name.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/ats_utilities/abstract/__init__.py to __init__.pyc
```

Install lib egg info
```
python setup.py install_egg_info
running install_egg_info
running egg_info
creating ats_utilities.egg-info
writing requirements to ats_utilities.egg-info/requires.txt
writing ats_utilities.egg-info/PKG-INFO
writing top-level names to ats_utilities.egg-info/top_level.txt
writing dependency_links to ats_utilities.egg-info/dependency_links.txt
writing manifest file 'ats_utilities.egg-info/SOURCES.txt'
reading manifest file 'ats_utilities.egg-info/SOURCES.txt'
writing manifest file 'ats_utilities.egg-info/SOURCES.txt'
removing '/usr/local/lib/python2.7/dist-packages/ats_utilities-1.2.2.egg-info' (and everything under it)
Copying ats_utilities.egg-info to /usr/local/lib/python2.7/dist-packages/ats_utilities-1.2.2.egg-info
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

### Library structure

**ats_utilities** is based on OOP:

![alt tag](https://raw.githubusercontent.com/vroncevic/ats_utilities/dev/docs/arch_flow_usage.png)

Library structure:
```
ats_utilities/
├── abstract/
│   └── __init__.py
├── ats_info.py
├── cfg_base.py
├── checker.py
├── config/
│   ├── base_read_config.py
│   ├── base_write_config.py
│   ├── cfg/
│   │   ├── cfg2object.py
│   │   ├── __init__.py
│   │   └── object2cfg.py
│   ├── check_base_config.py
│   ├── config_context_manager.py
│   ├── file_checking.py
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
├── ini_base.py
├── __init__.py
├── json_base.py
├── logging/
│   ├── ats_logger_base.py
│   ├── ats_logger_file.py
│   ├── ats_logger_name.py
│   ├── ats_logger.py
│   ├── ats_logger_status.py
│   └── __init__.py
├── option/
│   ├── ats_option_parser.py
│   └── __init__.py
├── register/
│   └── __init__.py
├── xml_base.py
└── yaml_base.py
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
