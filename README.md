# ATS Utilities

<img align="right" src="https://raw.githubusercontent.com/vroncevic/ats_utilities/dev/docs/ats_utilities_logo.png" width="25%">

**ats_utilities** is framework for creating Apps/Tools/Scripts.

Developed in **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![ats_utilities_python_checker](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_python_checker.yml/badge.svg)](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_python_checker.yml) [![ats_utilities_package_checker](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_package_checker.yml/badge.svg)](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_package_checker.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/ats_utilities.svg)](https://github.com/vroncevic/ats_utilities/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/ats_utilities.svg)](https://github.com/vroncevic/ats_utilities/graphs/contributors)

### 📋 Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [🚀 Installation](#-installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [📁 Framework structure](#-framework-structure)
  - [✨ Features](#-features)
- [Code coverage](#code-coverage)
- [🛠 Usage](#-usage)
- [📚 Docs](#-docs)
- [👥 Contributing](#-contributing)
- [📄 Copyright and Licence](#-copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### 🚀 Installation

Used next development environment

![debian linux os](https://raw.githubusercontent.com/vroncevic/ats_utilities/dev/docs/debtux.png)

[![ats_utilities_python3_build](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_python3_build.yml/badge.svg)](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_python3_build.yml)
[![ats_utilities_interface_checker](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_interface_checker.yml/badge.svg)](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_interface_checker.yml) [![ats_utilities_isp_checker](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_isp_checker.yml/badge.svg)](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_isp_checker.yml) [![ats_utilities_srp_checker](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_srp_checker.yml/badge.svg)](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_srp_checker.yml) [![ats_utilities_toc](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_toc.yml/badge.svg)](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_toc.yml)

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

### 📁 Framework structure

**ats_utilities** is designed from the ground up around robust, object-oriented paradigms and industrial-grade design patterns. The codebase strictly adheres to SOLID principles and is partitioned into highly decoupled, modular packages.

Design Pillars

Object-Oriented Architecture (OOP): Employs strong encapsulation, strict interface segregation, and clear class hierarchies to model system components.

SOLID Compliance: Engineered to facilitate seamless framework extension without modification (Open/Closed) and to decouple operations via explicit interface abstractions (Dependency Inversion).

Domain-Driven Package Organization: Functionality is organized into dedicated sub-packages—such as registries, bundle dataclasses, engines, and validators—ensuring clear separation of concerns.

<details>
<summary><b>Click to expand framework structure</b></summary>

```bash
    ats_utilities/
         ├── base/
         │   ├── engine.py
         │   ├── ibase.py
         │   ├── __init__.py
         │   └── setup/
         │       ├── bundle.py
         │       ├── dep_validator.py
         │       ├── dependencies.py
         │       ├── factory.py
         │       ├── __init__.py
         │       ├── keys.py
         │       ├── opt_validator.py
         │       ├── options.py
         │       ├── registry.py
         │       └── validator.py
         ├── checker/
         │   ├── context/
         │   │   ├── engine.py
         │   │   ├── icontext_provider.py
         │   │   └── __init__.py
         │   ├── engine.py
         │   ├── format/
         │   │   ├── engine.py
         │   │   ├── iformat_validator.py
         │   │   └── __init__.py
         │   ├── ichecker.py
         │   ├── __init__.py
         │   ├── proxy_validator.py
         │   ├── reporter/
         │   │   ├── data.py
         │   │   ├── data_validator.py
         │   │   ├── engine.py
         │   │   ├── icheck_reporter.py
         │   │   └── __init__.py
         │   ├── setup/
         │   │   ├── bundle.py
         │   │   ├── dep_validator.py
         │   │   ├── dependencies.py
         │   │   ├── factory.py
         │   │   ├── __init__.py
         │   │   ├── keys.py
         │   │   ├── opt_validator.py
         │   │   ├── options.py
         │   │   ├── registry.py
         │   │   ├── types.py
         │   │   └── validator.py
         │   └── type/
         │       ├── engine.py
         │       ├── __init__.py
         │       └── itype_validator.py
         ├── config_io/
         │   ├── conf_file.py
         │   ├── data.py
         │   ├── data_validator.py
         │   ├── iconf_file.py
         │   ├── __init__.py
         │   ├── loader/
         │   │   ├── engine.py
         │   │   ├── iloader.py
         │   │   └── __init__.py
         │   ├── processor/
         │   │   ├── cfg_processor.py
         │   │   ├── factory_processor.py
         │   │   ├── iconfig_processor.py
         │   │   ├── ifactory_processor.py
         │   │   ├── ini_processor.py
         │   │   ├── __init__.py
         │   │   ├── json_processor.py
         │   │   ├── xml_processor.py
         │   │   └── yaml_processor.py
         │   ├── setup/
         │   │   ├── bundle.py
         │   │   ├── dep_validator.py
         │   │   ├── dependencies.py
         │   │   ├── factory.py
         │   │   ├── __init__.py
         │   │   ├── keys.py
         │   │   ├── opt_validator.py
         │   │   ├── options.py
         │   │   ├── registry.py
         │   │   ├── types.py
         │   │   └── validator.py
         │   └── storer/
         │       ├── engine.py
         │       ├── __init__.py
         │       └── istorer.py
         ├── context/
         │   ├── bundle.py
         │   ├── dep_validator.py
         │   ├── dependencies.py
         │   ├── factory.py
         │   ├── __init__.py
         │   ├── keys.py
         │   ├── opt_validator.py
         │   ├── options.py
         │   ├── registry.py
         │   └── validator.py
         ├── exceptions/
         │   ├── ats_attribute_error.py
         │   ├── ats_bad_call_error.py
         │   ├── ats_error.py
         │   ├── ats_file_error.py
         │   ├── ats_generator_error.py
         │   ├── ats_key_error.py
         │   ├── ats_lookup_error.py
         │   ├── ats_parameter_error.py
         │   ├── ats_runtime_error.py
         │   ├── ats_type_error.py
         │   ├── ats_value_error.py
         │   ├── format_error.py
         │   └── __init__.py
         ├── generation/
         │   ├── data.py
         │   ├── data_validator.py
         │   ├── engine.py
         │   ├── imanager.py
         │   ├── __init__.py
         │   ├── project/
         │   │   ├── __init__.py
         │   │   ├── ipro_config.py
         │   │   ├── ipro_name.py
         │   │   ├── itemplate_dir.py
         │   │   ├── pro_config.py
         │   │   ├── pro_name.py
         │   │   └── template_dir.py
         │   ├── scheme/
         │   │   ├── engine.py
         │   │   ├── __init__.py
         │   │   └── ischeme_loader.py
         │   ├── setup/
         │   │   ├── bundle.py
         │   │   ├── dep_validator.py
         │   │   ├── dependencies.py
         │   │   ├── factory.py
         │   │   ├── __init__.py
         │   │   ├── keys.py
         │   │   ├── opt_validator.py
         │   │   ├── options.py
         │   │   ├── registry.py
         │   │   └── validator.py
         │   ├── tar/
         │   │   ├── data.py
         │   │   ├── data_validator.py
         │   │   ├── engine.py
         │   │   ├── __init__.py
         │   │   └── itar_processor.py
         │   └── template/
         │       ├── engine.py
         │       ├── __init__.py
         │       └── itemplate_processor.py
         ├── info/
         │   ├── build_date/
         │   │   ├── engine.py
         │   │   ├── ibuild_date.py
         │   │   └── __init__.py
         │   ├── engine.py
         │   ├── imanager.py
         │   ├── info_ok/
         │   │   ├── engine.py
         │   │   ├── iinfo_ok.py
         │   │   └── __init__.py
         │   ├── __init__.py
         │   ├── licence/
         │   │   ├── engine.py
         │   │   ├── ilicence.py
         │   │   └── __init__.py
         │   ├── log_file/
         │   │   ├── engine.py
         │   │   ├── ilog_file.py
         │   │   └── __init__.py
         │   ├── logo/
         │   │   ├── engine.py
         │   │   ├── ilogo.py
         │   │   └── __init__.py
         │   ├── name/
         │   │   ├── engine.py
         │   │   ├── iname.py
         │   │   └── __init__.py
         │   ├── organization/
         │   │   ├── engine.py
         │   │   ├── __init__.py
         │   │   └── iorganization.py
         │   ├── repository/
         │   │   ├── engine.py
         │   │   ├── __init__.py
         │   │   └── irepository.py
         │   ├── setup/
         │   │   ├── bundle.py
         │   │   ├── dep_validator.py
         │   │   ├── dependencies.py
         │   │   ├── expose.py
         │   │   ├── factory.py
         │   │   ├── iexpose.py
         │   │   ├── __init__.py
         │   │   ├── ischema.py
         │   │   ├── keys.py
         │   │   ├── opt_validator.py
         │   │   ├── options.py
         │   │   ├── registry.py
         │   │   ├── schema.py
         │   │   └── validator.py
         │   ├── use_github/
         │   │   ├── engine.py
         │   │   ├── __init__.py
         │   │   └── iuse_github.py
         │   └── version/
         │       ├── engine.py
         │       ├── __init__.py
         │       └── iversion.py
         ├── __init__.py
         ├── logger/
         │   ├── buffer/
         │   │   ├── engine.py
         │   │   ├── ibuffer.py
         │   │   └── __init__.py
         │   ├── engine.py
         │   ├── formatter/
         │   │   ├── engine.py
         │   │   ├── iformatter.py
         │   │   └── __init__.py
         │   ├── handler/
         │   │   ├── engine.py
         │   │   ├── ihandler_manager.py
         │   │   └── __init__.py
         │   ├── ilogger.py
         │   ├── __init__.py
         │   ├── processor/
         │   │   ├── engine.py
         │   │   └── imessage_processor.py
         │   ├── setup/
         │   │   ├── bundle.py
         │   │   ├── dep_validator.py
         │   │   ├── dependencies.py
         │   │   ├── factory.py
         │   │   ├── __init__.py
         │   │   ├── keys.py
         │   │   ├── opt_validator.py
         │   │   ├── options.py
         │   │   ├── registry.py
         │   │   └── validator.py
         │   └── underlying/
         │       ├── engine.py
         │       └── iunderlying.py
         ├── option/
         │   ├── command/
         │   │   ├── data.py
         │   │   ├── data_validator.py
         │   │   ├── __init__.py
         │   │   ├── ioption.py
         │   │   └── ioption_command.py
         │   ├── engine.py
         │   ├── imanager.py
         │   ├── __init__.py
         │   ├── ioption_configurator.py
         │   ├── ioption_parser.py
         │   ├── setup/
         │   │   ├── bundle.py
         │   │   ├── dep_validator.py
         │   │   ├── dependencies.py
         │   │   ├── factory.py
         │   │   ├── __init__.py
         │   │   ├── keys.py
         │   │   ├── opt_validator.py
         │   │   ├── options.py
         │   │   ├── registry.py
         │   │   ├── types.py
         │   │   └── validator.py
         │   ├── strategy/
         │   │   ├── data.py
         │   │   ├── data_validator.py
         │   │   ├── engine.py
         │   │   ├── __init__.py
         │   │   └── iparser_strategy.py
         │   └── underlying/
         │       ├── engine.py
         │       ├── __init__.py
         │       └── iunderlying.py
         ├── py.typed
         ├── reporter/
         │   ├── engine.py
         │   ├── __init__.py
         │   ├── ireporter.py
         │   ├── proxy_reporter.py
         │   ├── setup/
         │   │   ├── bundle.py
         │   │   ├── dep_validator.py
         │   │   ├── dependencies.py
         │   │   ├── factory.py
         │   │   ├── __init__.py
         │   │   ├── keys.py
         │   │   ├── opt_validator.py
         │   │   ├── options.py
         │   │   ├── registry.py
         │   │   └── validator.py
         │   └── theme/
         │       ├── engine.py
         │       ├── iconsole_theme.py
         │       ├── __init__.py
         │       └── types.py
         ├── splash/
         │   ├── data.py
         │   ├── data_validator.py
         │   ├── engine.py
         │   ├── external/
         │   │   ├── ext_infrastructure.py
         │   │   ├── github_infrastructure.py
         │   │   ├── iext_infrastructure.py
         │   │   └── __init__.py
         │   ├── imanager.py
         │   ├── __init__.py
         │   ├── progressbar/
         │   │   ├── __init__.py
         │   │   ├── iprogress_bar.py
         │   │   └── progress_bar.py
         │   ├── property/
         │   │   ├── __init__.py
         │   │   ├── isplash_property.py
         │   │   └── splash_property.py
         │   ├── setup/
         │   │   ├── bundle.py
         │   │   ├── dep_validator.py
         │   │   ├── dependencies.py
         │   │   ├── factory.py
         │   │   ├── __init__.py
         │   │   ├── keys.py
         │   │   ├── opt_validator.py
         │   │   ├── options.py
         │   │   ├── registry.py
         │   │   └── validator.py
         │   └── terminal/
         │       ├── __init__.py
         │       ├── iterminal_properties.py
         │       └── terminal_properties.py
         ├── utils/
         │   ├── boolean.py
         │   ├── component.py
         │   ├── data/
         │   │   ├── __init__.py
         │   │   └── ivalidator.py
         │   ├── dicts.py
         │   ├── dirs.py
         │   ├── files.py
         │   ├── __init__.py
         │   ├── reflection.py
         │   └── setup/
         │       ├── idep_validator.py
         │       ├── ifactory.py
         │       ├── ikeys.py
         │       ├── __init__.py
         │       ├── iopt_validator.py
         │       ├── iregistry.py
         │       └── ivalidator.py
         └── validation/
             ├── check_type.py
             ├── check_value.py
             ├── context_error.py
             └── __init__.py

     59 directories, 299 files
```
</details>

#### ✨ Features

* **Base Framework Architecture**: Standardized classes (`Base`, `BaseFactory`, `BaseOptions`) to quickly build robust command-line applications, scripts, and tools.
* **Robust Logging Engine**: Highly configurable logging module supporting log file outputs, buffers, custom formatters, message processors, and multiple severity levels.
* **Advanced Option Parsing**: Command-line option parser with modular design and strategy support (such as `fire` parsing or standard `argparse` processing).
* **Flexible Configuration I/O**: Config files loader and storer supporting formats like CFG, INI, JSON, XML, and YAML out of the box.
* **Themeable Console Reporter**: Enhanced feedback system that displays styled, colored, and verbose messages to the console with support for custom color themes.
* **Progressive Splash Screens**: Informative and visually appealing CLI splash screen implementation with customizable progress bars.
* **Type & Value Validation**: Built-in mechanisms to perform rigorous type checking and data validation on inputs and configs.
* **OOP and SOLID Design**: Decoupled, modular package design built around SOLID principles and clear interface segregation.

### Code coverage

<details>
<summary><b>Click to expand code coverage</b></summary>

| Name | Stmts | Miss | Cover |
|------|-------|------|-------|
| `ats_utilities/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/base/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/base/engine.py` | 55 | 0 | 100%|
| `ats_utilities/base/ibase.py` | 18 | 0 | 100%|
| `ats_utilities/base/setup/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/base/setup/bundle.py` | 25 | 0 | 100%|
| `ats_utilities/base/setup/dep_validator.py` | 32 | 0 | 100%|
| `ats_utilities/base/setup/dependencies.py` | 21 | 0 | 100%|
| `ats_utilities/base/setup/factory.py` | 58 | 0 | 100%|
| `ats_utilities/base/setup/keys.py` | 31 | 0 | 100%|
| `ats_utilities/base/setup/opt_validator.py` | 28 | 0 | 100%|
| `ats_utilities/base/setup/options.py` | 15 | 0 | 100%|
| `ats_utilities/base/setup/registry.py` | 21 | 0 | 100%|
| `ats_utilities/base/setup/validator.py` | 40 | 0 | 100%|
| `ats_utilities/checker/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/checker/context/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/checker/context/engine.py` | 47 | 0 | 100%|
| `ats_utilities/checker/context/icontext_provider.py` | 16 | 0 | 100%|
| `ats_utilities/checker/engine.py` | 95 | 0 | 100%|
| `ats_utilities/checker/format/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/checker/format/engine.py` | 49 | 0 | 100%|
| `ats_utilities/checker/format/iformat_validator.py` | 17 | 0 | 100%|
| `ats_utilities/checker/ichecker.py` | 25 | 0 | 100%|
| `ats_utilities/checker/proxy_validator.py` | 32 | 0 | 100%|
| `ats_utilities/checker/reporter/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/checker/reporter/data.py` | 21 | 0 | 100%|
| `ats_utilities/checker/reporter/data_validator.py` | 37 | 0 | 100%|
| `ats_utilities/checker/reporter/engine.py` | 44 | 0 | 100%|
| `ats_utilities/checker/reporter/icheck_reporter.py` | 14 | 0 | 100%|
| `ats_utilities/checker/setup/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/checker/setup/bundle.py` | 23 | 0 | 100%|
| `ats_utilities/checker/setup/dep_validator.py` | 27 | 0 | 100%|
| `ats_utilities/checker/setup/dependencies.py` | 19 | 0 | 100%|
| `ats_utilities/checker/setup/factory.py` | 34 | 0 | 100%|
| `ats_utilities/checker/setup/keys.py` | 31 | 0 | 100%|
| `ats_utilities/checker/setup/opt_validator.py` | 26 | 0 | 100%|
| `ats_utilities/checker/setup/options.py` | 16 | 0 | 100%|
| `ats_utilities/checker/setup/registry.py` | 21 | 0 | 100%|
| `ats_utilities/checker/setup/types.py` | 18 | 0 | 100%|
| `ats_utilities/checker/setup/validator.py` | 39 | 0 | 100%|
| `ats_utilities/checker/type/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/checker/type/engine.py` | 57 | 0 | 100%|
| `ats_utilities/checker/type/itype_validator.py` | 16 | 0 | 100%|
| `ats_utilities/config_io/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/conf_file.py` | 53 | 0 | 100%|
| `ats_utilities/config_io/data.py` | 19 | 0 | 100%|
| `ats_utilities/config_io/data_validator.py` | 38 | 0 | 100%|
| `ats_utilities/config_io/iconf_file.py` | 15 | 0 | 100%|
| `ats_utilities/config_io/loader/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/loader/engine.py` | 43 | 0 | 100%|
| `ats_utilities/config_io/loader/iloader.py` | 15 | 0 | 100%|
| `ats_utilities/config_io/processor/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/processor/cfg_processor.py` | 49 | 0 | 100%|
| `ats_utilities/config_io/processor/factory_processor.py` | 56 | 0 | 100%|
| `ats_utilities/config_io/processor/iconfig_processor.py` | 18 | 0 | 100%|
| `ats_utilities/config_io/processor/ifactory_processor.py` | 20 | 0 | 100%|
| `ats_utilities/config_io/processor/ini_processor.py` | 86 | 0 | 100%|
| `ats_utilities/config_io/processor/json_processor.py` | 44 | 0 | 100%|
| `ats_utilities/config_io/processor/xml_processor.py` | 86 | 0 | 100%|
| `ats_utilities/config_io/processor/yaml_processor.py` | 44 | 0 | 100%|
| `ats_utilities/config_io/setup/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/setup/bundle.py` | 23 | 0 | 100%|
| `ats_utilities/config_io/setup/dep_validator.py` | 30 | 0 | 100%|
| `ats_utilities/config_io/setup/dependencies.py` | 16 | 0 | 100%|
| `ats_utilities/config_io/setup/factory.py` | 27 | 0 | 100%|
| `ats_utilities/config_io/setup/keys.py` | 27 | 0 | 100%|
| `ats_utilities/config_io/setup/opt_validator.py` | 31 | 0 | 100%|
| `ats_utilities/config_io/setup/options.py` | 16 | 0 | 100%|
| `ats_utilities/config_io/setup/registry.py` | 21 | 0 | 100%|
| `ats_utilities/config_io/setup/types.py` | 3 | 0 | 100%|
| `ats_utilities/config_io/setup/validator.py` | 35 | 0 | 100%|
| `ats_utilities/config_io/storer/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/storer/engine.py` | 45 | 0 | 100%|
| `ats_utilities/config_io/storer/istorer.py` | 15 | 0 | 100%|
| `ats_utilities/context/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/context/bundle.py` | 22 | 0 | 100%|
| `ats_utilities/context/dep_validator.py` | 27 | 0 | 100%|
| `ats_utilities/context/dependencies.py` | 18 | 0 | 100%|
| `ats_utilities/context/factory.py` | 34 | 0 | 100%|
| `ats_utilities/context/keys.py` | 32 | 0 | 100%|
| `ats_utilities/context/opt_validator.py` | 26 | 0 | 100%|
| `ats_utilities/context/options.py` | 18 | 0 | 100%|
| `ats_utilities/context/registry.py` | 21 | 0 | 100%|
| `ats_utilities/context/validator.py` | 38 | 0 | 100%|
| `ats_utilities/exceptions/__init__.py` | 21 | 0 | 100%|
| `ats_utilities/exceptions/ats_attribute_error.py` | 11 | 0 | 100%|
| `ats_utilities/exceptions/ats_bad_call_error.py` | 11 | 0 | 100%|
| `ats_utilities/exceptions/ats_error.py` | 10 | 0 | 100%|
| `ats_utilities/exceptions/ats_file_error.py` | 11 | 0 | 100%|
| `ats_utilities/exceptions/ats_generator_error.py` | 11 | 0 | 100%|
| `ats_utilities/exceptions/ats_key_error.py` | 11 | 0 | 100%|
| `ats_utilities/exceptions/ats_lookup_error.py` | 11 | 0 | 100%|
| `ats_utilities/exceptions/ats_parameter_error.py` | 11 | 0 | 100%|
| `ats_utilities/exceptions/ats_runtime_error.py` | 11 | 0 | 100%|
| `ats_utilities/exceptions/ats_type_error.py` | 11 | 0 | 100%|
| `ats_utilities/exceptions/ats_value_error.py` | 11 | 0 | 100%|
| `ats_utilities/exceptions/format_error.py` | 22 | 0 | 100%|
| `ats_utilities/generation/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/generation/data.py` | 21 | 0 | 100%|
| `ats_utilities/generation/data_validator.py` | 46 | 0 | 100%|
| `ats_utilities/generation/engine.py` | 86 | 0 | 100%|
| `ats_utilities/generation/imanager.py` | 19 | 0 | 100%|
| `ats_utilities/generation/project/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/generation/project/ipro_config.py` | 18 | 0 | 100%|
| `ats_utilities/generation/project/ipro_name.py` | 18 | 0 | 100%|
| `ats_utilities/generation/project/itemplate_dir.py` | 18 | 0 | 100%|
| `ats_utilities/generation/project/pro_config.py` | 39 | 0 | 100%|
| `ats_utilities/generation/project/pro_name.py` | 35 | 0 | 100%|
| `ats_utilities/generation/project/template_dir.py` | 35 | 0 | 100%|
| `ats_utilities/generation/scheme/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/generation/scheme/engine.py` | 49 | 0 | 100%|
| `ats_utilities/generation/scheme/ischeme_loader.py` | 16 | 0 | 100%|
| `ats_utilities/generation/setup/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/generation/setup/bundle.py` | 21 | 0 | 100%|
| `ats_utilities/generation/setup/dep_validator.py` | 30 | 0 | 100%|
| `ats_utilities/generation/setup/dependencies.py` | 17 | 0 | 100%|
| `ats_utilities/generation/setup/factory.py` | 31 | 0 | 100%|
| `ats_utilities/generation/setup/keys.py` | 25 | 0 | 100%|
| `ats_utilities/generation/setup/opt_validator.py` | 31 | 0 | 100%|
| `ats_utilities/generation/setup/options.py` | 13 | 0 | 100%|
| `ats_utilities/generation/setup/registry.py` | 21 | 0 | 100%|
| `ats_utilities/generation/setup/validator.py` | 36 | 0 | 100%|
| `ats_utilities/generation/tar/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/generation/tar/data.py` | 31 | 0 | 100%|
| `ats_utilities/generation/tar/data_validator.py` | 68 | 0 | 100%|
| `ats_utilities/generation/tar/engine.py` | 76 | 0 | 100%|
| `ats_utilities/generation/tar/itar_processor.py` | 16 | 0 | 100%|
| `ats_utilities/generation/template/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/generation/template/engine.py` | 32 | 0 | 100%|
| `ats_utilities/generation/template/itemplate_processor.py` | 15 | 0 | 100%|
| `ats_utilities/info/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/build_date/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/build_date/engine.py` | 35 | 0 | 100%|
| `ats_utilities/info/build_date/ibuild_date.py` | 18 | 0 | 100%|
| `ats_utilities/info/engine.py` | 112 | 0 | 100%|
| `ats_utilities/info/imanager.py` | 20 | 0 | 100%|
| `ats_utilities/info/info_ok/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/info_ok/engine.py` | 35 | 0 | 100%|
| `ats_utilities/info/info_ok/iinfo_ok.py` | 18 | 0 | 100%|
| `ats_utilities/info/licence/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/licence/engine.py` | 35 | 0 | 100%|
| `ats_utilities/info/licence/ilicence.py` | 18 | 0 | 100%|
| `ats_utilities/info/log_file/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/log_file/engine.py` | 35 | 0 | 100%|
| `ats_utilities/info/log_file/ilog_file.py` | 18 | 0 | 100%|
| `ats_utilities/info/logo/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/logo/engine.py` | 35 | 0 | 100%|
| `ats_utilities/info/logo/ilogo.py` | 18 | 0 | 100%|
| `ats_utilities/info/name/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/name/engine.py` | 35 | 0 | 100%|
| `ats_utilities/info/name/iname.py` | 18 | 0 | 100%|
| `ats_utilities/info/organization/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/organization/engine.py` | 35 | 0 | 100%|
| `ats_utilities/info/organization/iorganization.py` | 18 | 0 | 100%|
| `ats_utilities/info/repository/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/repository/engine.py` | 35 | 0 | 100%|
| `ats_utilities/info/repository/irepository.py` | 18 | 0 | 100%|
| `ats_utilities/info/setup/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/setup/bundle.py` | 37 | 0 | 100%|
| `ats_utilities/info/setup/dep_validator.py` | 37 | 0 | 100%|
| `ats_utilities/info/setup/dependencies.py` | 33 | 0 | 100%|
| `ats_utilities/info/setup/expose.py` | 63 | 0 | 100%|
| `ats_utilities/info/setup/factory.py` | 39 | 0 | 100%|
| `ats_utilities/info/setup/iexpose.py` | 33 | 0 | 100%|
| `ats_utilities/info/setup/ischema.py` | 38 | 0 | 100%|
| `ats_utilities/info/setup/keys.py` | 53 | 0 | 100%|
| `ats_utilities/info/setup/opt_validator.py` | 42 | 0 | 100%|
| `ats_utilities/info/setup/options.py` | 15 | 0 | 100%|
| `ats_utilities/info/setup/registry.py` | 21 | 0 | 100%|
| `ats_utilities/info/setup/schema.py` | 65 | 0 | 100%|
| `ats_utilities/info/setup/validator.py` | 84 | 0 | 100%|
| `ats_utilities/info/use_github/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/use_github/engine.py` | 35 | 0 | 100%|
| `ats_utilities/info/use_github/iuse_github.py` | 18 | 0 | 100%|
| `ats_utilities/info/version/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/version/engine.py` | 35 | 0 | 100%|
| `ats_utilities/info/version/iversion.py` | 18 | 0 | 100%|
| `ats_utilities/logger/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/logger/buffer/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/logger/buffer/engine.py` | 39 | 0 | 100%|
| `ats_utilities/logger/buffer/ibuffer.py` | 19 | 0 | 100%|
| `ats_utilities/logger/engine.py` | 80 | 0 | 100%|
| `ats_utilities/logger/formatter/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/logger/formatter/engine.py` | 54 | 0 | 100%|
| `ats_utilities/logger/formatter/iformatter.py` | 17 | 0 | 100%|
| `ats_utilities/logger/handler/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/logger/handler/engine.py` | 27 | 0 | 100%|
| `ats_utilities/logger/handler/ihandler_manager.py` | 15 | 0 | 100%|
| `ats_utilities/logger/ilogger.py` | 21 | 0 | 100%|
| `ats_utilities/logger/processor/engine.py` | 46 | 0 | 100%|
| `ats_utilities/logger/processor/imessage_processor.py` | 16 | 0 | 100%|
| `ats_utilities/logger/setup/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/logger/setup/bundle.py` | 26 | 0 | 100%|
| `ats_utilities/logger/setup/dep_validator.py` | 27 | 0 | 100%|
| `ats_utilities/logger/setup/dependencies.py` | 22 | 0 | 100%|
| `ats_utilities/logger/setup/factory.py` | 47 | 0 | 100%|
| `ats_utilities/logger/setup/keys.py` | 35 | 0 | 100%|
| `ats_utilities/logger/setup/opt_validator.py` | 26 | 0 | 100%|
| `ats_utilities/logger/setup/options.py` | 15 | 0 | 100%|
| `ats_utilities/logger/setup/registry.py` | 21 | 0 | 100%|
| `ats_utilities/logger/setup/validator.py` | 48 | 0 | 100%|
| `ats_utilities/logger/underlying/engine.py` | 51 | 0 | 100%|
| `ats_utilities/logger/underlying/iunderlying.py` | 10 | 0 | 100%|
| `ats_utilities/option/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/option/command/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/option/command/data.py` | 40 | 0 | 100%|
| `ats_utilities/option/command/data_validator.py` | 40 | 0 | 100%|
| `ats_utilities/option/command/ioption.py` | 28 | 0 | 100%|
| `ats_utilities/option/command/ioption_command.py` | 20 | 0 | 100%|
| `ats_utilities/option/engine.py` | 77 | 0 | 100%|
| `ats_utilities/option/imanager.py` | 21 | 0 | 100%|
| `ats_utilities/option/ioption_configurator.py` | 16 | 0 | 100%|
| `ats_utilities/option/ioption_parser.py` | 14 | 0 | 100%|
| `ats_utilities/option/setup/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/option/setup/bundle.py` | 19 | 0 | 100%|
| `ats_utilities/option/setup/dep_validator.py` | 30 | 0 | 100%|
| `ats_utilities/option/setup/dependencies.py` | 15 | 0 | 100%|
| `ats_utilities/option/setup/factory.py` | 31 | 0 | 100%|
| `ats_utilities/option/setup/keys.py` | 27 | 0 | 100%|
| `ats_utilities/option/setup/opt_validator.py` | 35 | 0 | 100%|
| `ats_utilities/option/setup/options.py` | 15 | 0 | 100%|
| `ats_utilities/option/setup/registry.py` | 21 | 0 | 100%|
| `ats_utilities/option/setup/types.py` | 16 | 0 | 100%|
| `ats_utilities/option/setup/validator.py` | 25 | 0 | 100%|
| `ats_utilities/option/strategy/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/option/strategy/data.py` | 19 | 0 | 100%|
| `ats_utilities/option/strategy/data_validator.py` | 31 | 0 | 100%|
| `ats_utilities/option/strategy/engine.py` | 59 | 0 | 100%|
| `ats_utilities/option/strategy/iparser_strategy.py` | 19 | 0 | 100%|
| `ats_utilities/option/underlying/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/option/underlying/engine.py` | 26 | 0 | 100%|
| `ats_utilities/option/underlying/iunderlying.py` | 8 | 0 | 100%|
| `ats_utilities/reporter/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/reporter/engine.py` | 72 | 0 | 100%|
| `ats_utilities/reporter/ireporter.py` | 21 | 0 | 100%|
| `ats_utilities/reporter/proxy_reporter.py` | 15 | 0 | 100%|
| `ats_utilities/reporter/setup/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/reporter/setup/bundle.py` | 21 | 0 | 100%|
| `ats_utilities/reporter/setup/dep_validator.py` | 25 | 0 | 100%|
| `ats_utilities/reporter/setup/dependencies.py` | 17 | 0 | 100%|
| `ats_utilities/reporter/setup/factory.py` | 32 | 0 | 100%|
| `ats_utilities/reporter/setup/keys.py` | 30 | 0 | 100%|
| `ats_utilities/reporter/setup/opt_validator.py` | 26 | 0 | 100%|
| `ats_utilities/reporter/setup/options.py` | 17 | 0 | 100%|
| `ats_utilities/reporter/setup/registry.py` | 21 | 0 | 100%|
| `ats_utilities/reporter/setup/validator.py` | 34 | 0 | 100%|
| `ats_utilities/reporter/theme/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/reporter/theme/engine.py` | 36 | 0 | 100%|
| `ats_utilities/reporter/theme/iconsole_theme.py` | 14 | 0 | 100%|
| `ats_utilities/reporter/theme/types.py` | 16 | 0 | 100%|
| `ats_utilities/splash/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/splash/data.py` | 17 | 0 | 100%|
| `ats_utilities/splash/data_validator.py` | 31 | 0 | 100%|
| `ats_utilities/splash/engine.py` | 99 | 0 | 100%|
| `ats_utilities/splash/external/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/splash/external/ext_infrastructure.py` | 59 | 0 | 100%|
| `ats_utilities/splash/external/github_infrastructure.py` | 70 | 0 | 100%|
| `ats_utilities/splash/external/iext_infrastructure.py` | 20 | 0 | 100%|
| `ats_utilities/splash/imanager.py` | 19 | 0 | 100%|
| `ats_utilities/splash/progressbar/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/splash/progressbar/iprogress_bar.py` | 16 | 0 | 100%|
| `ats_utilities/splash/progressbar/progress_bar.py` | 54 | 0 | 100%|
| `ats_utilities/splash/property/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/splash/property/isplash_property.py` | 23 | 0 | 100%|
| `ats_utilities/splash/property/splash_property.py` | 66 | 0 | 100%|
| `ats_utilities/splash/setup/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/splash/setup/bundle.py` | 25 | 0 | 100%|
| `ats_utilities/splash/setup/dep_validator.py` | 30 | 0 | 100%|
| `ats_utilities/splash/setup/dependencies.py` | 21 | 0 | 100%|
| `ats_utilities/splash/setup/factory.py` | 41 | 0 | 100%|
| `ats_utilities/splash/setup/keys.py` | 33 | 0 | 100%|
| `ats_utilities/splash/setup/opt_validator.py` | 28 | 0 | 100%|
| `ats_utilities/splash/setup/options.py` | 15 | 0 | 100%|
| `ats_utilities/splash/setup/registry.py` | 21 | 0 | 100%|
| `ats_utilities/splash/setup/validator.py` | 50 | 0 | 100%|
| `ats_utilities/splash/terminal/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/splash/terminal/iterminal_properties.py` | 16 | 0 | 100%|
| `ats_utilities/splash/terminal/terminal_properties.py` | 35 | 0 | 100%|
| `ats_utilities/utils/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/utils/boolean.py` | 20 | 0 | 100%|
| `ats_utilities/utils/component.py` | 14 | 0 | 100%|
| `ats_utilities/utils/data/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/utils/data/ivalidator.py` | 14 | 0 | 100%|
| `ats_utilities/utils/dicts.py` | 40 | 0 | 100%|
| `ats_utilities/utils/dirs.py` | 17 | 0 | 100%|
| `ats_utilities/utils/files.py` | 106 | 0 | 100%|
| `ats_utilities/utils/reflection.py` | 39 | 0 | 100%|
| `ats_utilities/utils/setup/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/utils/setup/idep_validator.py` | 14 | 0 | 100%|
| `ats_utilities/utils/setup/ifactory.py` | 14 | 0 | 100%|
| `ats_utilities/utils/setup/ikeys.py` | 17 | 0 | 100%|
| `ats_utilities/utils/setup/iopt_validator.py` | 14 | 0 | 100%|
| `ats_utilities/utils/setup/iregistry.py` | 14 | 0 | 100%|
| `ats_utilities/utils/setup/ivalidator.py` | 14 | 0 | 100%|
| `ats_utilities/validation/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/validation/check_type.py` | 28 | 0 | 100%|
| `ats_utilities/validation/check_value.py` | 22 | 0 | 100%|
| `ats_utilities/validation/context_error.py` | 14 | 0 | 100%|
| **Total** | 7832 | 0 | 100% |

</details>

### 🛠 Usage

Below is a basic example illustrating how to define and use a tool by subclassing the `Base` class, integrating logger and reporter modules:

```python
from logging import INFO, WARNING
from os.path import dirname, realpath

from ats_utilities.base.engine import Base
from ats_utilities.base.setup.factory import BaseFactory
from ats_utilities.base.setup.options import BaseOptions
from ats_utilities.context.factory import ContextFactory
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter


class MyTool(Base):
    '''Concrete implementation of Base for use case illustration.'''

    _INFO_FILE: str = '../../tests/assets/config/read_only/ats_cli_cfg_api.cfg'
    _logger: ILogger
    _reporter: IReporter

    def __init__(self):
        '''Initialize MyTool instance.'''
        current_dir: str = dirname(realpath(__file__))
        super().__init__(
            BaseFactory.create_bundle(
                options=BaseOptions(
                    info_file=f'{current_dir}/{self._INFO_FILE}',
                    use_generator=False,
                    context_bundle=ContextFactory.create_bundle()
                )
            )
        )
        self._logger = self.get_context().logger
        self._reporter = self.get_context().reporter
        self._splash_manager.show()

        self._logger.write_log('Log: MyTool initialized successfully', INFO)
        self._reporter.success(['Report: MyTool initialized successfully'])

    def process(self, verbose: bool = True) -> bool:
        self._logger.write_log(f'Log: Processing starting, verbose: {verbose}', INFO)
        self._reporter.verbose(verbose, [f'Report: Processing starting, verbose: {verbose}'])
        print(f'Overwrite result {verbose} ...')
        return verbose

    def perform_action(self) -> None:
        '''A new method showing logging and reporting with different levels and colors.'''
        self._logger.write_log('Log: Performing a specific tool action', INFO)
        self._logger.write_log('Log: This is a warning log from MyTool action', WARNING)
        self._reporter.warning(['Report: This is a colored warning from MyTool'])
        self._reporter.error(['Report: This is a colored error from MyTool'])


if __name__ == "__main__":
    tool: MyTool = MyTool()

    result: bool = False
    print(f'Result: {result}')

    if tool.is_initialized():
        result = tool.process(True)
        tool.perform_action()

    print(f'Result: {result}')
```

### 📚 Docs

[![Documentation Status](https://readthedocs.org/projects/ats-utilities/badge/?version=master)](https://ats-utilities.readthedocs.io/?badge=master)

More documentation and info at

* [ats-utilities.readthedocs.io](https://ats-utilities.readthedocs.io/)
* [www.python.org](https://www.python.org/)

### 👥 Contributing

[Contributing to ats_utilities](CONTRIBUTING.md)

### 📄 Copyright and Licence

[![license: gpl v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![license apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2017 - 2026 by [vroncevic.github.io/ats_utilities](https://vroncevic.github.io/ats_utilities/)

**ats_utilities** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/ats_utilities/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)
