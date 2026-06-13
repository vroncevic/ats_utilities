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

### Framework structure

**ats_utilities** is based on OOP.

Framework structure

```bash
    ats_utilities/
    ├── checker/
    │   ├── ats_checker.py
    │   ├── default_check_reporter.py
    │   ├── default_context_provider.py
    │   ├── default_format_validator.py
    │   ├── default_type_validator.py
    │   ├── iats_checker.py
    │   ├── icheck_reporter.py
    │   ├── icontext_provider.py
    │   ├── iformat_validator.py
    │   ├── __init__.py
    │   └── itype_validator.py
    ├── cli/
    │   ├── ats_cli.py
    │   ├── config_manager.py
    │   ├── icli.py
    │   ├── iconfig_manager.py
    │   └── __init__.py
    ├── config_io/
    │   ├── cfg/
    │   │   ├── cfg2object.py
    │   │   ├── cfgbase.py
    │   │   ├── default_cfg_processor.py
    │   │   ├── icfg_processor.py
    │   │   ├── __init__.py
    │   │   └── object2cfg.py
    │   ├── conf_file.py
    │   ├── file_check.py
    │   ├── iconf_file.py
    │   ├── ifile_check.py
    │   ├── ini/
    │   │   ├── default_ini_processor.py
    │   │   ├── iini_processor.py
    │   │   ├── ini2object.py
    │   │   ├── inibase.py
    │   │   ├── __init__.py
    │   │   └── object2ini.py
    │   ├── __init__.py
    │   ├── iread.py
    │   ├── iwrite.py
    │   ├── json/
    │   │   ├── default_json_processor.py
    │   │   ├── ijson_processor.py
    │   │   ├── __init__.py
    │   │   ├── json2object.py
    │   │   ├── jsonbase.py
    │   │   └── object2json.py
    │   ├── xml/
    │   │   ├── default_xml_processor.py
    │   │   ├── __init__.py
    │   │   ├── ixml_processor.py
    │   │   ├── object2xml.py
    │   │   ├── xml2object.py
    │   │   └── xmlbase.py
    │   └── yaml/
    │       ├── default_yaml_processor.py
    │       ├── __init__.py
    │       ├── iyaml_processor.py
    │       ├── object2yaml.py
    │       ├── yaml2object.py
    │       └── yamlbase.py
    ├── console_io/
    │   ├── __init__.py
    │   ├── ireporter.py
    │   ├── reporter.py
    │   └── theme/
    │       ├── default_theme.py
    │       ├── iconsole_theme.py
    │       └── __init__.py
    ├── exceptions/
    │   ├── ats_attribute_error.py
    │   ├── ats_bad_call_error.py
    │   ├── ats_error.py
    │   ├── ats_file_error.py
    │   ├── ats_key_error.py
    │   ├── ats_lookup_error.py
    │   ├── ats_parameter_error.py
    │   ├── ats_type_error.py
    │   ├── ats_value_error.py
    │   └── __init__.py
    ├── info/
    │   ├── ats_info.py
    │   ├── build_date.py
    │   ├── ibuild_date.py
    │   ├── iinfo_ok.py
    │   ├── ilicence.py
    │   ├── iname.py
    │   ├── info_ok.py
    │   ├── __init__.py
    │   ├── iversion.py
    │   ├── licence.py
    │   ├── name.py
    │   └── version.py
    ├── __init__.py
    ├── logging/
    │   ├── ats_logger.py
    │   ├── default_logger.py
    │   ├── ilogger.py
    │   └── __init__.py
    ├── option/
    │   ├── ats_option_parser.py
    │   ├── ats_parser_strategy.py
    │   ├── __init__.py
    │   ├── ioption_parser.py
    │   ├── iparser_strategy.py
    │   └── option_namespace.py
    ├── pro_config/
    │   ├── __init__.py
    │   ├── ipro_config.py
    │   ├── ipro_name.py
    │   ├── itemplate_dir.py
    │   ├── pro_config.py
    │   ├── pro_name.py
    │   └── template_dir.py
    ├── py.typed
    └── splash/
        ├── ext_infrastructure.py
        ├── github_infrastructure.py
        ├── iext_infrastructure.py
        ├── __init__.py
        ├── iprogress_bar.py
        ├── isplash.py
        ├── isplash_screen.py
        ├── iterminal_properties.py
        ├── progress_bar.py
        ├── splash_property.py
        ├── splash.py
        └── terminal_properties.py
    
    17 directories, 112 files
```

### Code coverage

| Name | Stmts | Miss | Cover |
|------|-------|------|-------|
| `ats_utilities/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/checker/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/checker/ats_checker.py` | 49 | 0 | 100%|
| `ats_utilities/checker/default_check_reporter.py` | 21 | 0 | 100%|
| `ats_utilities/checker/default_context_provider.py` | 16 | 0 | 100%|
| `ats_utilities/checker/default_format_validator.py` | 17 | 0 | 100%|
| `ats_utilities/checker/default_type_validator.py` | 17 | 2 | 88%|
| `ats_utilities/checker/iats_checker.py` | 26 | 1 | 96%|
| `ats_utilities/checker/icheck_reporter.py` | 15 | 1 | 93%|
| `ats_utilities/checker/icontext_provider.py` | 14 | 1 | 93%|
| `ats_utilities/checker/iformat_validator.py` | 17 | 2 | 88%|
| `ats_utilities/checker/itype_validator.py` | 20 | 3 | 85%|
| `ats_utilities/cli/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/cli/ats_cli.py` | 40 | 4 | 90%|
| `ats_utilities/cli/config_manager.py` | 51 | 0 | 100%|
| `ats_utilities/cli/icli.py` | 25 | 4 | 84%|
| `ats_utilities/cli/iconfig_manager.py` | 20 | 1 | 95%|
| `ats_utilities/config_io/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/cfg/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/cfg/cfg2object.py` | 46 | 1 | 98%|
| `ats_utilities/config_io/cfg/cfgbase.py` | 52 | 0 | 100%|
| `ats_utilities/config_io/cfg/default_cfg_processor.py` | 27 | 1 | 96%|
| `ats_utilities/config_io/cfg/icfg_processor.py` | 20 | 3 | 85%|
| `ats_utilities/config_io/cfg/object2cfg.py` | 52 | 0 | 100%|
| `ats_utilities/config_io/conf_file.py` | 63 | 0 | 100%|
| `ats_utilities/config_io/file_check.py` | 69 | 0 | 100%|
| `ats_utilities/config_io/iconf_file.py` | 18 | 2 | 89%|
| `ats_utilities/config_io/ifile_check.py` | 25 | 4 | 84%|
| `ats_utilities/config_io/ini/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/ini/default_ini_processor.py` | 30 | 8 | 73%|
| `ats_utilities/config_io/ini/iini_processor.py` | 20 | 3 | 85%|
| `ats_utilities/config_io/ini/ini2object.py` | 45 | 1 | 98%|
| `ats_utilities/config_io/ini/inibase.py` | 54 | 0 | 100%|
| `ats_utilities/config_io/ini/object2ini.py` | 51 | 0 | 100%|
| `ats_utilities/config_io/iread.py` | 14 | 1 | 93%|
| `ats_utilities/config_io/iwrite.py` | 14 | 1 | 93%|
| `ats_utilities/config_io/json/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/json/default_json_processor.py` | 24 | 3 | 88%|
| `ats_utilities/config_io/json/ijson_processor.py` | 20 | 3 | 85%|
| `ats_utilities/config_io/json/json2object.py` | 46 | 1 | 98%|
| `ats_utilities/config_io/json/jsonbase.py` | 52 | 0 | 100%|
| `ats_utilities/config_io/json/object2json.py` | 51 | 0 | 100%|
| `ats_utilities/config_io/xml/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/xml/default_xml_processor.py` | 33 | 6 | 82%|
| `ats_utilities/config_io/xml/ixml_processor.py` | 20 | 3 | 85%|
| `ats_utilities/config_io/xml/object2xml.py` | 53 | 1 | 98%|
| `ats_utilities/config_io/xml/xml2object.py` | 47 | 0 | 100%|
| `ats_utilities/config_io/xml/xmlbase.py` | 54 | 0 | 100%|
| `ats_utilities/config_io/yaml/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/yaml/default_yaml_processor.py` | 24 | 3 | 88%|
| `ats_utilities/config_io/yaml/iyaml_processor.py` | 20 | 3 | 85%|
| `ats_utilities/config_io/yaml/object2yaml.py` | 51 | 0 | 100%|
| `ats_utilities/config_io/yaml/yaml2object.py` | 46 | 1 | 98%|
| `ats_utilities/config_io/yaml/yamlbase.py` | 52 | 0 | 100%|
| `ats_utilities/console_io/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/console_io/ireporter.py` | 25 | 4 | 84%|
| `ats_utilities/console_io/reporter.py` | 35 | 1 | 97%|
| `ats_utilities/console_io/theme/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/console_io/theme/default_theme.py` | 16 | 0 | 100%|
| `ats_utilities/console_io/theme/iconsole_theme.py` | 14 | 1 | 93%|
| `ats_utilities/exceptions/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/exceptions/ats_attribute_error.py` | 10 | 0 | 100%|
| `ats_utilities/exceptions/ats_bad_call_error.py` | 10 | 0 | 100%|
| `ats_utilities/exceptions/ats_error.py` | 10 | 10 | 0%|
| `ats_utilities/exceptions/ats_file_error.py` | 10 | 0 | 100%|
| `ats_utilities/exceptions/ats_key_error.py` | 10 | 0 | 100%|
| `ats_utilities/exceptions/ats_lookup_error.py` | 10 | 0 | 100%|
| `ats_utilities/exceptions/ats_parameter_error.py` | 10 | 0 | 100%|
| `ats_utilities/exceptions/ats_type_error.py` | 10 | 0 | 100%|
| `ats_utilities/exceptions/ats_value_error.py` | 10 | 0 | 100%|
| `ats_utilities/info/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/ats_info.py` | 63 | 0 | 100%|
| `ats_utilities/info/build_date.py` | 36 | 1 | 97%|
| `ats_utilities/info/ibuild_date.py` | 22 | 3 | 86%|
| `ats_utilities/info/iinfo_ok.py` | 19 | 2 | 89%|
| `ats_utilities/info/ilicence.py` | 22 | 3 | 86%|
| `ats_utilities/info/iname.py` | 22 | 3 | 86%|
| `ats_utilities/info/info_ok.py` | 34 | 0 | 100%|
| `ats_utilities/info/iversion.py` | 22 | 3 | 86%|
| `ats_utilities/info/licence.py` | 36 | 1 | 97%|
| `ats_utilities/info/name.py` | 36 | 0 | 100%|
| `ats_utilities/info/version.py` | 36 | 0 | 100%|
| `ats_utilities/logging/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/logging/ats_logger.py` | 27 | 0 | 100%|
| `ats_utilities/logging/default_logger.py` | 63 | 5 | 92%|
| `ats_utilities/logging/ilogger.py` | 35 | 1 | 97%|
| `ats_utilities/option/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/option/ats_option_parser.py` | 46 | 7 | 85%|
| `ats_utilities/option/ats_parser_strategy.py` | 43 | 8 | 81%|
| `ats_utilities/option/ioption_parser.py` | 25 | 4 | 84%|
| `ats_utilities/option/iparser_strategy.py` | 25 | 4 | 84%|
| `ats_utilities/option/option_namespace.py` | 13 | 0 | 100%|
| `ats_utilities/pro_config/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/pro_config/ipro_config.py` | 22 | 3 | 86%|
| `ats_utilities/pro_config/ipro_name.py` | 22 | 3 | 86%|
| `ats_utilities/pro_config/itemplate_dir.py` | 22 | 3 | 86%|
| `ats_utilities/pro_config/pro_config.py` | 40 | 1 | 98%|
| `ats_utilities/pro_config/pro_name.py` | 38 | 1 | 97%|
| `ats_utilities/pro_config/template_dir.py` | 38 | 1 | 97%|
| `ats_utilities/splash/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/splash/ext_infrastructure.py` | 40 | 1 | 98%|
| `ats_utilities/splash/github_infrastructure.py` | 47 | 1 | 98%|
| `ats_utilities/splash/iext_infrastructure.py` | 20 | 3 | 85%|
| `ats_utilities/splash/iprogress_bar.py` | 20 | 3 | 85%|
| `ats_utilities/splash/isplash.py` | 14 | 1 | 93%|
| `ats_utilities/splash/isplash_screen.py` | 14 | 1 | 93%|
| `ats_utilities/splash/iterminal_properties.py` | 20 | 3 | 85%|
| `ats_utilities/splash/progress_bar.py` | 45 | 2 | 96%|
| `ats_utilities/splash/splash.py` | 70 | 0 | 100%|
| `ats_utilities/splash/splash_property.py` | 39 | 1 | 97%|
| `ats_utilities/splash/terminal_properties.py` | 52 | 1 | 98%|
| **Total** | 3062 | 158 | 95% |

### Docs

[![Documentation Status](https://readthedocs.org/projects/ats-utilities/badge/?version=master)](https://ats-utilities.readthedocs.io/?badge=master)

More documentation and info at

* [ats-utilities.readthedocs.io](https://ats-utilities.readthedocs.io/)
* [www.python.org](https://www.python.org/)

### Contributing

[Contributing to ats_utilities](CONTRIBUTING.md)

### Copyright and Licence

[![license: gpl v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![license apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2017 - 2026 by [vroncevic.github.io/ats_utilities](https://vroncevic.github.io/ats_utilities/)

**ats_utilities** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/ats_utilities/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)
