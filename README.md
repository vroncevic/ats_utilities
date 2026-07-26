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
[![ats_utilities_interface_checker](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_interface_checker.yml/badge.svg)](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_interface_checker.yml) [![ats_utilities_isp_checker](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_isp_checker.yml/badge.svg)](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_isp_checker.yml) [![ats_utilities_ocp_checker](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_ocp_checker.yml/badge.svg)](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_ocp_checker.yml) [![ats_utilities_srp_checker](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_srp_checker.yml/badge.svg)](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_srp_checker.yml) [![ats_utilities_toc](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_toc.yml/badge.svg)](https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_toc.yml)

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
         │       ├── dependencies.py
         │       ├── factory.py
         │       ├── __init__.py
         │       ├── registry.py
         │       └── validator.py
         ├── checker/
         │   ├── context/
         │   │   ├── context_provider.py
         │   │   ├── icontext_provider.py
         │   │   └── __init__.py
         │   ├── engine.py
         │   ├── format/
         │   │   ├── format_validator.py
         │   │   ├── iformat_validator.py
         │   │   └── __init__.py
         │   ├── ichecker.py
         │   ├── __init__.py
         │   ├── proxy_validator.py
         │   ├── reporter/
         │   │   ├── check_reporter.py
         │   │   ├── data.py
         │   │   ├── data_validator.py
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
         │       ├── __init__.py
         │       ├── itype_validator.py
         │       └── type_validator.py
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
         │   │   ├── dependencies.py
         │   │   ├── factory.py
         │   │   ├── __init__.py
         │   │   ├── registry.py
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
         ├── generator/
         │   ├── data.py
         │   ├── data_validator.py
         │   ├── engine.py
         │   ├── igenerator.py
         │   ├── __init__.py
         │   ├── project/
         │   │   ├── __init__.py
         │   │   ├── ipro_config.py
         │   │   ├── ipro_name.py
         │   │   ├── itemplate_dir.py
         │   │   ├── pro_config.py
         │   │   ├── pro_name.py
         │   │   ├── setup/
         │   │   │   ├── bundle.py
         │   │   │   ├── dependencies.py
         │   │   │   ├── factory.py
         │   │   │   ├── __init__.py
         │   │   │   ├── registry.py
         │   │   │   └── validator.py
         │   │   └── template_dir.py
         │   ├── scheme/
         │   │   ├── engine.py
         │   │   ├── __init__.py
         │   │   └── ischeme_loader.py
         │   ├── setup/
         │   │   ├── bundle.py
         │   │   ├── dependencies.py
         │   │   ├── factory.py
         │   │   ├── __init__.py
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
         │   ├── iinfo_manager.py
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
         │   │   ├── factory.py
         │   │   ├── __init__.py
         │   │   ├── keys.py
         │   │   ├── opt_validator.py
         │   │   ├── options.py
         │   │   ├── registry.py
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
         ├── option/
         │   ├── command/
         │   │   ├── data.py
         │   │   ├── data_validator.py
         │   │   ├── __init__.py
         │   │   └── ioption_command.py
         │   ├── engine.py
         │   ├── __init__.py
         │   ├── ioption_manager.py
         │   ├── option_namespace.py
         │   ├── parser/
         │   │   ├── data.py
         │   │   ├── data_validator.py
         │   │   ├── engine.py
         │   │   ├── iarg_parser.py
         │   │   └── __init__.py
         │   ├── setup/
         │   │   ├── bundle.py
         │   │   ├── dep_validator.py
         │   │   ├── dependencies.py
         │   │   ├── factory.py
         │   │   ├── __init__.py
         │   │   ├── opt_validator.py
         │   │   ├── options.py
         │   │   ├── registry.py
         │   │   └── validator.py
         │   └── strategy/
         │       ├── data.py
         │       ├── data_validator.py
         │       ├── engine.py
         │       ├── __init__.py
         │       └── iparser_strategy.py
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
         ├── splasher/
         │   ├── data.py
         │   ├── data_validator.py
         │   ├── engine.py
         │   ├── external/
         │   │   ├── ext_infrastructure.py
         │   │   ├── github_infrastructure.py
         │   │   ├── iext_infrastructure.py
         │   │   └── __init__.py
         │   ├── __init__.py
         │   ├── isplasher.py
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
         │   │   ├── opt_validator.py
         │   │   ├── options.py
         │   │   ├── registry.py
         │   │   ├── splash_keys.py
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

     58 directories, 282 files
```
</details>

### Code coverage

<details>
<summary><b>Click to expand code coverage</b></summary>

| Name | Stmts | Miss | Cover |
|------|-------|------|-------|
| `ats_utilities/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/base/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/base/engine.py` | 65 | 0 | 100%|
| `ats_utilities/base/ibase.py` | 15 | 0 | 100%|
| `ats_utilities/base/setup/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/base/setup/bundle.py` | 30 | 0 | 100%|
| `ats_utilities/base/setup/dependencies.py` | 29 | 0 | 100%|
| `ats_utilities/base/setup/factory.py` | 66 | 0 | 100%|
| `ats_utilities/base/setup/registry.py` | 21 | 0 | 100%|
| `ats_utilities/base/setup/validator.py` | 42 | 0 | 100%|
| `ats_utilities/checker/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/checker/context/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/checker/context/context_provider.py` | 47 | 7 | 78%|
| `ats_utilities/checker/context/icontext_provider.py` | 11 | 0 | 100%|
| `ats_utilities/checker/engine.py` | 81 | 16 | 77%|
| `ats_utilities/checker/format/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/checker/format/format_validator.py` | 44 | 4 | 89%|
| `ats_utilities/checker/format/iformat_validator.py` | 12 | 0 | 100%|
| `ats_utilities/checker/ichecker.py` | 11 | 0 | 100%|
| `ats_utilities/checker/proxy_validator.py` | 92 | 17 | 80%|
| `ats_utilities/checker/reporter/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/checker/reporter/check_reporter.py` | 46 | 4 | 91%|
| `ats_utilities/checker/reporter/data.py` | 22 | 0 | 100%|
| `ats_utilities/checker/reporter/data_validator.py` | 31 | 0 | 100%|
| `ats_utilities/checker/reporter/icheck_reporter.py` | 11 | 0 | 100%|
| `ats_utilities/checker/setup/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/checker/setup/bundle.py` | 24 | 0 | 100%|
| `ats_utilities/checker/setup/dep_validator.py` | 28 | 0 | 97%|
| `ats_utilities/checker/setup/dependencies.py` | 19 | 0 | 100%|
| `ats_utilities/checker/setup/factory.py` | 35 | 1 | 95%|
| `ats_utilities/checker/setup/keys.py` | 34 | 1 | 97%|
| `ats_utilities/checker/setup/opt_validator.py` | 28 | 8 | 62%|
| `ats_utilities/checker/setup/options.py` | 16 | 0 | 100%|
| `ats_utilities/checker/setup/registry.py` | 25 | 0 | 96%|
| `ats_utilities/checker/setup/types.py` | 20 | 0 | 100%|
| `ats_utilities/checker/setup/validator.py` | 33 | 0 | 100%|
| `ats_utilities/checker/type/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/checker/type/itype_validator.py` | 12 | 0 | 100%|
| `ats_utilities/checker/type/type_validator.py` | 54 | 0 | 100%|
| `ats_utilities/config_io/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/conf_file.py` | 55 | 0 | 100%|
| `ats_utilities/config_io/data.py` | 20 | 0 | 100%|
| `ats_utilities/config_io/data_validator.py` | 28 | 0 | 100%|
| `ats_utilities/config_io/iconf_file.py` | 15 | 0 | 100%|
| `ats_utilities/config_io/loader/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/loader/engine.py` | 52 | 0 | 100%|
| `ats_utilities/config_io/loader/iloader.py` | 12 | 0 | 100%|
| `ats_utilities/config_io/processor/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/processor/cfg_processor.py` | 56 | 0 | 100%|
| `ats_utilities/config_io/processor/factory_processor.py` | 56 | 0 | 100%|
| `ats_utilities/config_io/processor/iconfig_processor.py` | 13 | 0 | 100%|
| `ats_utilities/config_io/processor/ifactory_processor.py` | 13 | 0 | 100%|
| `ats_utilities/config_io/processor/ini_processor.py` | 94 | 0 | 100%|
| `ats_utilities/config_io/processor/json_processor.py` | 52 | 0 | 100%|
| `ats_utilities/config_io/processor/xml_processor.py` | 94 | 0 | 100%|
| `ats_utilities/config_io/processor/yaml_processor.py` | 52 | 0 | 100%|
| `ats_utilities/config_io/setup/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/setup/bundle.py` | 24 | 0 | 100%|
| `ats_utilities/config_io/setup/dependencies.py` | 23 | 0 | 100%|
| `ats_utilities/config_io/setup/factory.py` | 36 | 0 | 100%|
| `ats_utilities/config_io/setup/registry.py` | 32 | 0 | 100%|
| `ats_utilities/config_io/setup/validator.py` | 32 | 0 | 100%|
| `ats_utilities/config_io/storer/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/storer/engine.py` | 55 | 0 | 100%|
| `ats_utilities/config_io/storer/istorer.py` | 12 | 0 | 100%|
| `ats_utilities/context/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/context/bundle.py` | 23 | 0 | 100%|
| `ats_utilities/context/dep_validator.py` | 28 | 0 | 97%|
| `ats_utilities/context/dependencies.py` | 18 | 0 | 100%|
| `ats_utilities/context/factory.py` | 39 | 0 | 100%|
| `ats_utilities/context/keys.py` | 35 | 0 | 100%|
| `ats_utilities/context/opt_validator.py` | 28 | 0 | 100%|
| `ats_utilities/context/options.py` | 18 | 0 | 100%|
| `ats_utilities/context/registry.py` | 24 | 0 | 100%|
| `ats_utilities/context/validator.py` | 32 | 0 | 100%|
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
| `ats_utilities/generator/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/generator/data.py` | 22 | 0 | 100%|
| `ats_utilities/generator/data_validator.py` | 36 | 0 | 100%|
| `ats_utilities/generator/engine.py` | 76 | 0 | 100%|
| `ats_utilities/generator/igenerator.py` | 13 | 0 | 100%|
| `ats_utilities/generator/project/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/generator/project/ipro_config.py` | 13 | 0 | 100%|
| `ats_utilities/generator/project/ipro_name.py` | 11 | 0 | 100%|
| `ats_utilities/generator/project/itemplate_dir.py` | 11 | 0 | 100%|
| `ats_utilities/generator/project/pro_config.py` | 43 | 0 | 100%|
| `ats_utilities/generator/project/pro_name.py` | 39 | 0 | 100%|
| `ats_utilities/generator/project/setup/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/generator/project/setup/bundle.py` | 24 | 0 | 100%|
| `ats_utilities/generator/project/setup/dependencies.py` | 23 | 0 | 100%|
| `ats_utilities/generator/project/setup/factory.py` | 44 | 0 | 100%|
| `ats_utilities/generator/project/setup/registry.py` | 21 | 0 | 100%|
| `ats_utilities/generator/project/setup/validator.py` | 33 | 0 | 100%|
| `ats_utilities/generator/project/template_dir.py` | 39 | 0 | 100%|
| `ats_utilities/generator/scheme/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/generator/scheme/engine.py` | 48 | 0 | 100%|
| `ats_utilities/generator/scheme/ischeme_loader.py` | 13 | 0 | 100%|
| `ats_utilities/generator/setup/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/generator/setup/bundle.py` | 24 | 0 | 100%|
| `ats_utilities/generator/setup/dependencies.py` | 21 | 0 | 100%|
| `ats_utilities/generator/setup/factory.py` | 40 | 0 | 100%|
| `ats_utilities/generator/setup/registry.py` | 28 | 1 | 96%|
| `ats_utilities/generator/setup/validator.py` | 33 | 0 | 100%|
| `ats_utilities/generator/tar/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/generator/tar/data.py` | 32 | 0 | 100%|
| `ats_utilities/generator/tar/data_validator.py` | 50 | 0 | 100%|
| `ats_utilities/generator/tar/engine.py` | 75 | 0 | 100%|
| `ats_utilities/generator/tar/itar_processor.py` | 12 | 0 | 100%|
| `ats_utilities/generator/template/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/generator/template/engine.py` | 35 | 0 | 100%|
| `ats_utilities/generator/template/itemplate_processor.py` | 11 | 0 | 100%|
| `ats_utilities/info/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/build_date/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/build_date/engine.py` | 41 | 0 | 100%|
| `ats_utilities/info/build_date/ibuild_date.py` | 11 | 0 | 100%|
| `ats_utilities/info/engine.py` | 105 | 63 | 32%|
| `ats_utilities/info/iinfo_manager.py` | 11 | 0 | 100%|
| `ats_utilities/info/info_ok/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/info_ok/engine.py` | 41 | 0 | 100%|
| `ats_utilities/info/info_ok/iinfo_ok.py` | 11 | 0 | 100%|
| `ats_utilities/info/licence/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/licence/engine.py` | 41 | 0 | 100%|
| `ats_utilities/info/licence/ilicence.py` | 11 | 0 | 100%|
| `ats_utilities/info/log_file/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/log_file/engine.py` | 41 | 0 | 100%|
| `ats_utilities/info/log_file/ilog_file.py` | 11 | 0 | 100%|
| `ats_utilities/info/logo/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/logo/engine.py` | 41 | 0 | 100%|
| `ats_utilities/info/logo/ilogo.py` | 11 | 0 | 100%|
| `ats_utilities/info/name/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/name/engine.py` | 41 | 0 | 100%|
| `ats_utilities/info/name/iname.py` | 11 | 0 | 100%|
| `ats_utilities/info/organization/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/organization/engine.py` | 41 | 0 | 100%|
| `ats_utilities/info/organization/iorganization.py` | 11 | 0 | 100%|
| `ats_utilities/info/repository/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/repository/engine.py` | 41 | 0 | 100%|
| `ats_utilities/info/repository/irepository.py` | 11 | 0 | 100%|
| `ats_utilities/info/setup/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/setup/bundle.py` | 38 | 0 | 100%|
| `ats_utilities/info/setup/dep_validator.py` | 35 | 15 | 47%|
| `ats_utilities/info/setup/dependencies.py` | 33 | 0 | 100%|
| `ats_utilities/info/setup/factory.py` | 41 | 17 | 49%|
| `ats_utilities/info/setup/keys.py` | 109 | 20 | 82%|
| `ats_utilities/info/setup/opt_validator.py` | 37 | 17 | 44%|
| `ats_utilities/info/setup/options.py` | 15 | 0 | 100%|
| `ats_utilities/info/setup/registry.py` | 24 | 4 | 83%|
| `ats_utilities/info/setup/validator.py` | 60 | 0 | 100%|
| `ats_utilities/info/use_github/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/use_github/engine.py` | 41 | 0 | 100%|
| `ats_utilities/info/use_github/iuse_github.py` | 11 | 0 | 100%|
| `ats_utilities/info/version/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/version/engine.py` | 41 | 0 | 100%|
| `ats_utilities/info/version/iversion.py` | 11 | 0 | 100%|
| `ats_utilities/logger/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/logger/buffer/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/logger/buffer/engine.py` | 39 | 10 | 67%|
| `ats_utilities/logger/buffer/ibuffer.py` | 12 | 0 | 100%|
| `ats_utilities/logger/engine.py` | 88 | 35 | 46%|
| `ats_utilities/logger/formatter/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/logger/formatter/engine.py` | 24 | 6 | 69%|
| `ats_utilities/logger/formatter/iformatter.py` | 11 | 0 | 100%|
| `ats_utilities/logger/handler/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/logger/handler/engine.py` | 81 | 54 | 22%|
| `ats_utilities/logger/handler/ihandler_manager.py` | 11 | 0 | 100%|
| `ats_utilities/logger/ilogger.py` | 12 | 0 | 100%|
| `ats_utilities/logger/setup/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/logger/setup/bundle.py` | 24 | 1 | 96%|
| `ats_utilities/logger/setup/dep_validator.py` | 32 | 0 | 95%|
| `ats_utilities/logger/setup/dependencies.py` | 19 | 0 | 100%|
| `ats_utilities/logger/setup/factory.py` | 50 | 0 | 100%|
| `ats_utilities/logger/setup/keys.py` | 34 | 0 | 100%|
| `ats_utilities/logger/setup/opt_validator.py` | 28 | 0 | 100%|
| `ats_utilities/logger/setup/options.py` | 15 | 0 | 100%|
| `ats_utilities/logger/setup/registry.py` | 24 | 0 | 100%|
| `ats_utilities/logger/setup/validator.py` | 34 | 0 | 100%|
| `ats_utilities/option/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/option/command/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/option/command/data.py` | 27 | 0 | 100%|
| `ats_utilities/option/command/data_validator.py` | 34 | 0 | 93%|
| `ats_utilities/option/command/ioption_command.py` | 12 | 0 | 100%|
| `ats_utilities/option/engine.py` | 68 | 0 | 100%|
| `ats_utilities/option/ioption_manager.py` | 16 | 0 | 100%|
| `ats_utilities/option/option_namespace.py` | 15 | 0 | 100%|
| `ats_utilities/option/parser/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/option/parser/data.py` | 21 | 0 | 100%|
| `ats_utilities/option/parser/data_validator.py` | 30 | 0 | 100%|
| `ats_utilities/option/parser/engine.py` | 44 | 1 | 96%|
| `ats_utilities/option/parser/iarg_parser.py` | 13 | 0 | 100%|
| `ats_utilities/option/setup/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/option/setup/bundle.py` | 22 | 0 | 100%|
| `ats_utilities/option/setup/dep_validator.py` | 33 | 0 | 100%|
| `ats_utilities/option/setup/dependencies.py` | 17 | 0 | 100%|
| `ats_utilities/option/setup/factory.py` | 35 | 0 | 100%|
| `ats_utilities/option/setup/opt_validator.py` | 33 | 0 | 97%|
| `ats_utilities/option/setup/options.py` | 17 | 0 | 100%|
| `ats_utilities/option/setup/registry.py` | 23 | 0 | 100%|
| `ats_utilities/option/setup/validator.py` | 30 | 0 | 100%|
| `ats_utilities/option/strategy/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/option/strategy/data.py` | 23 | 0 | 100%|
| `ats_utilities/option/strategy/data_validator.py` | 31 | 0 | 100%|
| `ats_utilities/option/strategy/engine.py` | 93 | 33 | 53%|
| `ats_utilities/option/strategy/iparser_strategy.py` | 16 | 0 | 100%|
| `ats_utilities/reporter/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/reporter/engine.py` | 67 | 14 | 72%|
| `ats_utilities/reporter/ireporter.py` | 11 | 0 | 100%|
| `ats_utilities/reporter/proxy_reporter.py` | 64 | 1 | 98%|
| `ats_utilities/reporter/setup/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/reporter/setup/bundle.py` | 22 | 0 | 100%|
| `ats_utilities/reporter/setup/dep_validator.py` | 28 | 0 | 97%|
| `ats_utilities/reporter/setup/dependencies.py` | 17 | 0 | 100%|
| `ats_utilities/reporter/setup/factory.py` | 35 | 1 | 95%|
| `ats_utilities/reporter/setup/keys.py` | 33 | 1 | 97%|
| `ats_utilities/reporter/setup/opt_validator.py` | 28 | 8 | 62%|
| `ats_utilities/reporter/setup/options.py` | 17 | 0 | 100%|
| `ats_utilities/reporter/setup/registry.py` | 24 | 0 | 100%|
| `ats_utilities/reporter/setup/validator.py` | 30 | 0 | 100%|
| `ats_utilities/reporter/theme/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/reporter/theme/engine.py` | 36 | 0 | 100%|
| `ats_utilities/reporter/theme/iconsole_theme.py` | 11 | 0 | 100%|
| `ats_utilities/reporter/theme/types.py` | 16 | 0 | 100%|
| `ats_utilities/splasher/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/splasher/data.py` | 18 | 0 | 100%|
| `ats_utilities/splasher/data_validator.py` | 27 | 0 | 100%|
| `ats_utilities/splasher/engine.py` | 75 | 0 | 100%|
| `ats_utilities/splasher/external/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/splasher/external/ext_infrastructure.py` | 68 | 0 | 100%|
| `ats_utilities/splasher/external/github_infrastructure.py` | 77 | 0 | 100%|
| `ats_utilities/splasher/external/iext_infrastructure.py` | 13 | 0 | 100%|
| `ats_utilities/splasher/isplasher.py` | 11 | 0 | 100%|
| `ats_utilities/splasher/progressbar/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/splasher/progressbar/iprogress_bar.py` | 11 | 0 | 100%|
| `ats_utilities/splasher/progressbar/progress_bar.py` | 60 | 0 | 100%|
| `ats_utilities/splasher/property/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/splasher/property/isplash_property.py` | 13 | 0 | 100%|
| `ats_utilities/splasher/property/splash_property.py` | 49 | 0 | 100%|
| `ats_utilities/splasher/setup/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/splasher/setup/bundle.py` | 29 | 0 | 100%|
| `ats_utilities/splasher/setup/dep_validator.py` | 48 | 0 | 100%|
| `ats_utilities/splasher/setup/dependencies.py` | 24 | 0 | 100%|
| `ats_utilities/splasher/setup/factory.py` | 53 | 0 | 100%|
| `ats_utilities/splasher/setup/opt_validator.py` | 29 | 0 | 100%|
| `ats_utilities/splasher/setup/options.py` | 15 | 0 | 100%|
| `ats_utilities/splasher/setup/registry.py` | 23 | 0 | 100%|
| `ats_utilities/splasher/setup/splash_keys.py` | 59 | 0 | 100%|
| `ats_utilities/splasher/setup/validator.py` | 48 | 0 | 100%|
| `ats_utilities/splasher/terminal/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/splasher/terminal/iterminal_properties.py` | 12 | 0 | 100%|
| `ats_utilities/splasher/terminal/terminal_properties.py` | 61 | 0 | 100%|
| `ats_utilities/utils/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/utils/boolean.py` | 19 | 0 | 100%|
| `ats_utilities/utils/component.py` | 16 | 0 | 100%|
| `ats_utilities/utils/data/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/utils/data/ivalidator.py` | 11 | 0 | 100%|
| `ats_utilities/utils/dicts.py` | 36 | 0 | 100%|
| `ats_utilities/utils/dirs.py` | 19 | 0 | 100%|
| `ats_utilities/utils/files.py` | 123 | 0 | 100%|
| `ats_utilities/utils/reflection.py` | 55 | 0 | 100%|
| `ats_utilities/utils/setup/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/utils/setup/idep_validator.py` | 11 | 0 | 100%|
| `ats_utilities/utils/setup/ifactory.py` | 11 | 0 | 100%|
| `ats_utilities/utils/setup/ikeys.py` | 12 | 0 | 100%|
| `ats_utilities/utils/setup/iopt_validator.py` | 11 | 0 | 100%|
| `ats_utilities/utils/setup/iregistry.py` | 11 | 0 | 100%|
| `ats_utilities/utils/setup/ivalidator.py` | 11 | 0 | 100%|
| `ats_utilities/validation/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/validation/check_type.py` | 37 | 0 | 100%|
| `ats_utilities/validation/check_value.py` | 26 | 0 | 100%|
| `ats_utilities/validation/context_error.py` | 14 | 0 | 100%|
| **Total** | 7525 | 360 | 93% |

</details>

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
