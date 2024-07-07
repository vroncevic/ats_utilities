# ATS Utilities

<img align="right" src="https://raw.githubusercontent.com/vroncevic/ats_utilities/dev/docs/ats_utilities_logo.png" width="25%">

**ats_utilities** is framework for creating Apps/Tools/Scripts.

Developed in **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![ats_utilities_python_checker](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_python_checker.yml/badge.svg)](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_python_checker.yml) [![ats_utilities_package_checker](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_package_checker.yml/badge.svg)](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_package_checker.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/ats_utilities.svg)](https://github.com/vroncevic/ats_utilities/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/ats_utilities.svg)](https://github.com/vroncevic/ats_utilities/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Framework structure](#framework-structure)
- [Code coverage](#code-coverage)
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Used next development environment

![debian linux os](https://raw.githubusercontent.com/vroncevic/ats_utilities/dev/docs/debtux.png)

[![ats_utilities_python3_build](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_python3_build.yml/badge.svg)](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_python3_build.yml)

Currently there are four ways to install framework
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

Python is located at **[pypi.org](https://pypi.org/project/ats-utilities/)**.

You can install by using pip

```bash
# python3
pip3 install ats-utilities
```

##### Install using build

Navigate to **[release page](https://github.com/vroncevic/ats_utilities/releases)** download and extract release archive.

To install **ats-utilities**, run

```bash
tar xvzf ats-utilities-x.y.z.tar.gz
cd ats-utilities-x.y.z
# python3
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py 
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
pip3 install -r requirements.txt
python3 -m build --no-isolation --wheel
pip3 install dist/ats-utilities-x.y.z-py3-none-any.whl
rm -f get-pip.py
```

##### Install using py setup

Navigate to **[release page](https://github.com/vroncevic/ats_utilities/releases)** download and extract release archive.

To install **ats-utilities**, locate and run setup.py with arguments

```bash
tar xvzf ats-utilities-x.y.z.tar.gz
cd ats-utilities-x.y.z
# python3
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_egg_info
rm -f get-pip.py
```

##### Install using docker

You can use Dockerfile to create image/container.

### Dependencies

These modules requires other modules and libraries (Python 3.x)
* [yaml - YAML parser and emitter for Python](https://pypi.org/project/PyYAML/)
* [bs4 - Screen-scraping library](https://pypi.org/project/beautifulsoup4/)
* [colorama - Cross-platform colored terminal text](https://pypi.org/project/colorama/)
* [lxml - XML processing library](https://pypi.org/project/lxml/)

### Framework structure

**ats_utilities** is based on OOP.

Framework structure

```bash
    ats_utilities/
          ├── checker
          │   └── __init__.py
          ├── cli/
          │   └── __init__.py
          ├── config_io/
          │   ├── cfg/
          │   │   ├── cfg2object.py
          │   │   ├── __init__.py
          │   │   └── object2cfg.py
          │   ├── file_check.py
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
          │   ├── ats_parameter_error.py
          │   ├── ats_type_error.py
          │   ├── ats_value_error.py
          │   └── __init__.py
          ├── info/
          │   ├── ats_build_date.py
          │   ├── ats_info_ok.py
          │   ├── ats_licence.py
          │   ├── ats_name.py
          │   ├── ats_version.py
          │   └── __init__.py
          ├── __init__.py
          ├── logging/
          │   └── __init__.py
          ├── option/
          │   └── __init__.py
          ├── pro_config/
          │   ├── __init__.py
          │   ├── pro_name.py
          │   └── template_dir.py
          ├── py.typed
          └── splash/
              ├── ext_infrastructure.py
              ├── github_infrastructure.py
              ├── __init__.py
              ├── progress_bar.py
              ├── splash_property.py
              └── terminal_properties.py

    16 directories, 52 files
```

### Code coverage

| Name | Stmts | Miss | Cover |
|------|-------|------|-------|
| `ats_utilities/__init__.py` | 0 | 0 | 100%|
| `ats_utilities/checker/__init__.py` | 73 | 23 | 68%|
| `ats_utilities/cli/__init__.py` | 62 | 16 | 74%|
| `ats_utilities/config_io/__init__.py` | 58 | 2 | 97%|
| `ats_utilities/config_io/cfg/__init__.py` | 46 | 3 | 93%|
| `ats_utilities/config_io/cfg/cfg2object.py` | 46 | 3 | 93%|
| `ats_utilities/config_io/cfg/object2cfg.py` | 48 | 3 | 94%|
| `ats_utilities/config_io/file_check.py` | 79 | 2 | 97%|
| `ats_utilities/config_io/ini/__init__.py` | 52 | 3 | 94%|
| `ats_utilities/config_io/ini/ini2object.py` | 41 | 3 | 93%|
| `ats_utilities/config_io/ini/object2ini.py` | 51 | 4 | 92%|
| `ats_utilities/config_io/json/__init__.py` | 46 | 3 | 93%|
| `ats_utilities/config_io/json/json2object.py` | 40 | 3 | 92%|
| `ats_utilities/config_io/json/object2json.py` | 48 | 3 | 94%|
| `ats_utilities/config_io/xml/__init__.py` | 59 | 3 | 95%|
| `ats_utilities/config_io/xml/object2xml.py` | 51 | 4 | 92%|
| `ats_utilities/config_io/xml/xml2object.py` | 42 | 3 | 93%|
| `ats_utilities/config_io/yaml/__init__.py` | 46 | 3 | 93%|
| `ats_utilities/config_io/yaml/object2yaml.py` | 48 | 3 | 94%|
| `ats_utilities/config_io/yaml/yaml2object.py` | 40 | 3 | 92%|
| `ats_utilities/console_io/__init__.py` | 0 | 0 | 100%|
| `ats_utilities/console_io/error.py` | 40 | 24 | 40%|
| `ats_utilities/console_io/success.py` | 40 | 24 | 40%|
| `ats_utilities/console_io/verbose.py` | 41 | 24 | 41%|
| `ats_utilities/console_io/warning.py` | 40 | 2 | 95%|
| `ats_utilities/exceptions/__init__.py` | 10 | 10 | 0%|
| `ats_utilities/exceptions/ats_attribute_error.py` | 10 | 0 | 100%|
| `ats_utilities/exceptions/ats_bad_call_error.py` | 10 | 0 | 100%|
| `ats_utilities/exceptions/ats_file_error.py` | 10 | 10 | 0%|
| `ats_utilities/exceptions/ats_key_error.py` | 10 | 0 | 100%|
| `ats_utilities/exceptions/ats_lookup_error.py` | 10 | 0 | 100%|
| `ats_utilities/exceptions/ats_parameter_error.py` | 10 | 0 | 100%|
| `ats_utilities/exceptions/ats_type_error.py` | 10 | 10 | 0%|
| `ats_utilities/exceptions/ats_value_error.py` | 10 | 0 | 100%|
| `ats_utilities/info/__init__.py` | 62 | 2 | 97%|
| `ats_utilities/info/ats_build_date.py` | 35 | 2 | 94%|
| `ats_utilities/info/ats_info_ok.py` | 33 | 2 | 94%|
| `ats_utilities/info/ats_licence.py` | 35 | 2 | 94%|
| `ats_utilities/info/ats_name.py` | 35 | 2 | 94%|
| `ats_utilities/info/ats_version.py` | 35 | 2 | 94%|
| `ats_utilities/logging/__init__.py` | 72 | 8 | 89%|
| `ats_utilities/option/__init__.py` | 40 | 27 | 32%|
| `ats_utilities/pro_config/__init__.py` | 37 | 2 | 95%|
| `ats_utilities/pro_config/pro_name.py` | 34 | 2 | 94%|
| `ats_utilities/pro_config/template_dir.py` | 34 | 2 | 94%|
| `ats_utilities/splash/__init__.py` | 63 | 2 | 97%|
| `ats_utilities/splash/ext_infrastructure.py` | 39 | 3 | 92%|
| `ats_utilities/splash/github_infrastructure.py` | 46 | 3 | 93%|
| `ats_utilities/splash/progress_bar.py` | 44 | 2 | 95%|
| `ats_utilities/splash/splash_property.py` | 39 | 3 | 92%|
| `ats_utilities/splash/terminal_properties.py` | 51 | 3 | 94%|
| **Total** | 1961 | 263 | 87% |

### Docs

[![Documentation Status](https://readthedocs.org/projects/ats-utilities/badge/?version=master)](https://ats-utilities.readthedocs.io/?badge=master)

More documentation and info at

* [ats-utilities.readthedocs.io](https://ats-utilities.readthedocs.io/)
* [www.python.org](https://www.python.org/)

### Contributing

[Contributing to ats_utilities](CONTRIBUTING.md)

### Copyright and Licence

[![license: gpl v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![license apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2017 - 2024 by [vroncevic.github.io/ats_utilities](https://vroncevic.github.io/ats_utilities/)

**ats_utilities** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/ats_utilities/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)
