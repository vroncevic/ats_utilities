<img align="right" src="https://raw.githubusercontent.com/vroncevic/ats_utilities/dev/docs/ats_utilities_logo.png" width="25%">

# ATS Utilities

**ats_utilities** is framework for creating Apps/Tools/Scripts.

Developed in **[python](https://www.python.org/)** code: **https://github.com/vroncevic/ats_utilities/search?l=python**.

[![codecov](https://codecov.io/gh/vroncevic/ats_utilities/branch/dev/graph/badge.svg?token=VNQOBXIHDB)](https://codecov.io/gh/vroncevic/ats_utilities)
[![CircleCI](https://circleci.com/gh/vroncevic/ats_utilities/tree/master.svg?style=svg)](https://circleci.com/gh/vroncevic/ats_utilities/tree/master)

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/ats_utilities/workflows/Python%20package%20ats_utilities/badge.svg?branch=master) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/ats_utilities.svg)](https://github.com/vroncevic/ats_utilities/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/ats_utilities.svg)](https://github.com/vroncevic/ats_utilities/graphs/contributors)

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
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

![Install Python2 Package](https://github.com/vroncevic/ats_utilities/workflows/Install%20Python2%20Package%20ats_utilities/badge.svg?branch=master) ![Install Python3 Package](https://github.com/vroncevic/ats_utilities/workflows/Install%20Python3%20Package%20ats_utilities/badge.svg?branch=master)

![Debian Linux OS](https://raw.githubusercontent.com/vroncevic/ats_utilities/dev/docs/debtux.png)

Currently there are four ways to install framework
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

Python package is located at **[pypi.org](https://pypi.org/project/ats-utilities/)**.

You can install by using pip

```bash
# python2
pip2 install ats-utilities
# python3
pip3 install ats-utilities
```

##### Install using build

Navigate to **[release page](https://github.com/vroncevic/ats_utilities/releases)** download and extract release archive.

To install **ats-utilities**, run

```bash
tar xvzf ats-utilities-x.y.z.tar.gz
cd ats-utilities-x.y.z
# python2
wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
python2 get-pip.py
python2 -m pip install --upgrade setuptools
python2 -m pip install --upgrade pip
python2 -m pip install --upgrade build
pip2 install -r requirements.txt
python2 -m build --no-isolation --wheel
pip2 install dist/ats-utilities-x.y.z-py2-none-any.whl
rm -f get-pip.py
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
# python2
wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
python2 get-pip.py
python2 -m pip install --upgrade setuptools
python2 -m pip install --upgrade pip
python2 -m pip install --upgrade build
pip2 install -r requirements.txt
python2 setup.py install_lib
python2 setup.py install_egg_info
rm -f get-pip.py
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

[![ats_utilities docker checker](https://github.com/vroncevic/ats_utilities/workflows/ats_utilities%20docker%20checker/badge.svg)](https://github.com/vroncevic/ats_utilities/actions?query=workflow%3A%22ats_utilities+docker+checker%22)

### Dependencies

These modules requires other modules and libraries (Python 2.x/3.x)
* [six - Python 2 and 3 compatibility library](https://pypi.org/project/six)
* [yaml - YAML parser and emitter for Python](https://pypi.org/project/PyYAML/)
* [bs4 - Screen-scraping library](https://pypi.org/project/beautifulsoup4/)
* [configparser - Configuration parser library](https://pypi.org/project/configparser/)
* [colorama - Cross-platform colored terminal text](https://pypi.org/project/colorama/)

### Framework structure

**ats_utilities** is based on OOP.

![Framework structure](https://raw.githubusercontent.com/vroncevic/ats_utilities/dev/docs/arch_flow_usage.png)

Framework structure

```bash
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
├── cooperative/
│   └── __init__.py
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
├── final/
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
│   ├── ats_logger_file.py
│   ├── ats_logger_name.py
│   ├── ats_logger_status.py
│   └── __init__.py
├── option/
│   └── __init__.py
├── register/
│   └── __init__.py
├── singleton/
│   ├── base.py
│   ├── functional.py
│   ├── __init__.py
│   ├── meta.py
│   └── meta_thread.py
└── splash/
    ├── ext_infrastructure.py
    ├── github_infrastructure.py
    ├── __init__.py
    ├── progress_bar.py
    ├── splash_property.py
    └── terminal_properties.py

19 directories, 67 files
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/ats-utilities/badge/?version=master)](https://ats-utilities.readthedocs.io/projects/ats-utilities/en/master/?badge=master)

More documentation and info at
* [ats-utilities.readthedocs.io](https://ats-utilities.readthedocs.io/en/master/)
* [www.python.org](https://www.python.org/)

### Contributing

[Contributing to ats_utilities](CONTRIBUTING.md)

### Copyright and Licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2017 by [vroncevic.github.io/ats_utilities](https://vroncevic.github.io/ats_utilities/)

**ats_utilities** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/ats_utilities/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
