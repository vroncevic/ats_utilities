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
         │   ├── base_bundle.py
         │   ├── base_factory.py
         │   ├── base_params.py
         │   ├── base_registry.py
         │   ├── engine.py
         │   ├── ibase.py
         │   └── __init__.py
         ├── checker/
         │   ├── checker_bundle.py
         │   ├── checker_factory.py
         │   ├── checker_params.py
         │   ├── checker_registry.py
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
         │   │   ├── checker_reporter_bundle.py
         │   │   ├── checker_reporter_params.py
         │   │   ├── checker_reporter_registry.py
         │   │   ├── icheck_reporter.py
         │   │   └── __init__.py
         │   └── type/
         │       ├── __init__.py
         │       ├── itype_validator.py
         │       └── type_validator.py
         ├── config_io/
         │   ├── conf_file.py
         │   ├── conf_file_bundle.py
         │   ├── conf_file_factory.py
         │   ├── conf_file_params.py
         │   ├── conf_file_registry.py
         │   ├── config_io_bundle.py
         │   ├── config_io_params.py
         │   ├── config_io_registry.py
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
         │   └── storer/
         │       ├── engine.py
         │       ├── __init__.py
         │       └── istorer.py
         ├── context/
         │   ├── context_bundle.py
         │   ├── context_factory.py
         │   ├── context_params.py
         │   ├── context_registry.py
         │   ├── context_support.py
         │   ├── icontext_support.py
         │   └── __init__.py
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
         │   ├── engine.py
         │   ├── gen_params_bundle.py
         │   ├── gen_params_params.py
         │   ├── gen_params_registry.py
         │   ├── generator_bundle.py
         │   ├── generator_factory.py
         │   ├── generator_params.py
         │   ├── generator_registry.py
         │   ├── igenerator.py
         │   ├── __init__.py
         │   ├── scheme/
         │   │   ├── engine.py
         │   │   ├── __init__.py
         │   │   └── ischeme_loader.py
         │   ├── tar/
         │   │   ├── engine.py
         │   │   ├── __init__.py
         │   │   ├── itar_processor.py
         │   │   ├── tar_process_bundle.py
         │   │   ├── tar_process_member_bundle.py
         │   │   ├── tar_process_member_params.py
         │   │   ├── tar_process_member_registry.py
         │   │   ├── tar_process_params.py
         │   │   └── tar_process_registry.py
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
         │   ├── info_bundle.py
         │   ├── info_factory.py
         │   ├── info_keys.py
         │   ├── info_ok/
         │   │   ├── engine.py
         │   │   ├── iinfo_ok.py
         │   │   └── __init__.py
         │   ├── info_params.py
         │   ├── info_registry.py
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
         │   ├── engine.py
         │   ├── ilogger.py
         │   ├── __init__.py
         │   ├── logger_bundle.py
         │   ├── logger_factory.py
         │   ├── logger_params.py
         │   └── logger_registry.py
         ├── option/
         │   ├── command/
         │   │   ├── command_option.py
         │   │   ├── __init__.py
         │   │   └── ioption_command.py
         │   ├── engine.py
         │   ├── __init__.py
         │   ├── ioption_manager.py
         │   ├── option_bundle.py
         │   ├── option_factory.py
         │   ├── option_namespace.py
         │   ├── option_params.py
         │   ├── option_registry.py
         │   ├── parser/
         │   │   ├── engine.py
         │   │   ├── iarg_parser.py
         │   │   ├── __init__.py
         │   │   ├── parser_bundle.py
         │   │   ├── parser_params.py
         │   │   └── parser_registry.py
         │   └── strategy/
         │       ├── engine.py
         │       ├── __init__.py
         │       ├── iparser_strategy.py
         │       ├── parser_strategy_bundle.py
         │       ├── parser_strategy_params.py
         │       └── parser_strategy_registry.py
         ├── project_setup/
         │   ├── __init__.py
         │   ├── ipro_config.py
         │   ├── ipro_name.py
         │   ├── itemplate_dir.py
         │   ├── pro_config.py
         │   ├── pro_name.py
         │   ├── project_setup_bundle.py
         │   ├── project_setup_factory.py
         │   ├── project_setup_params.py
         │   ├── project_setup_registry.py
         │   └── template_dir.py
         ├── py.typed
         ├── reporter/
         │   ├── engine.py
         │   ├── __init__.py
         │   ├── ireporter.py
         │   ├── proxy_reporter.py
         │   ├── reporter_bundle.py
         │   ├── reporter_factory.py
         │   ├── reporter_params.py
         │   ├── reporter_registry.py
         │   └── theme/
         │       ├── engine.py
         │       ├── iconsole_theme.py
         │       └── __init__.py
         ├── splasher/
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
         │   ├── splash_bundle.py
         │   ├── splash_center_bundle.py
         │   ├── splash_center_params.py
         │   ├── splash_center_registry.py
         │   ├── splash_factory.py
         │   ├── splash_keys.py
         │   ├── splash_params.py
         │   ├── splash_registry.py
         │   └── terminal/
         │       ├── __init__.py
         │       ├── iterminal_properties.py
         │       └── terminal_properties.py
         ├── utils/
         │   ├── boolean.py
         │   ├── component.py
         │   ├── dicts.py
         │   ├── dirs.py
         │   ├── files.py
         │   ├── __init__.py
         │   ├── iregistry.py
         │   └── reflection.py
         └── validation/
             ├── check_type.py
             ├── check_value.py
             ├── context_error.py
             └── __init__.py

     43 directories, 228 files
```
</details>

### Code coverage

<details>
<summary><b>Click to expand code coverage</b></summary>

| Name | Stmts | Miss | Cover |
|------|-------|------|-------|
| `ats_utilities/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/base/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/base/base_bundle.py` | 50 | 0 | 100%|
| `ats_utilities/base/base_factory.py` | 54 | 0 | 100%|
| `ats_utilities/base/base_params.py` | 25 | 0 | 100%|
| `ats_utilities/base/base_registry.py` | 18 | 0 | 100%|
| `ats_utilities/base/engine.py` | 67 | 0 | 100%|
| `ats_utilities/base/ibase.py` | 17 | 0 | 100%|
| `ats_utilities/checker/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/checker/checker_bundle.py` | 37 | 0 | 100%|
| `ats_utilities/checker/checker_factory.py` | 22 | 0 | 100%|
| `ats_utilities/checker/checker_params.py` | 19 | 0 | 100%|
| `ats_utilities/checker/checker_registry.py` | 18 | 0 | 100%|
| `ats_utilities/checker/context/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/checker/context/context_provider.py` | 39 | 0 | 100%|
| `ats_utilities/checker/context/icontext_provider.py` | 11 | 0 | 100%|
| `ats_utilities/checker/engine.py` | 65 | 0 | 100%|
| `ats_utilities/checker/format/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/checker/format/format_validator.py` | 29 | 0 | 100%|
| `ats_utilities/checker/format/iformat_validator.py` | 11 | 0 | 100%|
| `ats_utilities/checker/ichecker.py` | 20 | 0 | 100%|
| `ats_utilities/checker/proxy_validator.py` | 78 | 0 | 100%|
| `ats_utilities/checker/reporter/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/checker/reporter/check_reporter.py` | 33 | 0 | 100%|
| `ats_utilities/checker/reporter/checker_reporter_bundle.py` | 35 | 0 | 100%|
| `ats_utilities/checker/reporter/checker_reporter_params.py` | 17 | 0 | 100%|
| `ats_utilities/checker/reporter/checker_reporter_registry.py` | 23 | 0 | 100%|
| `ats_utilities/checker/reporter/icheck_reporter.py` | 12 | 0 | 100%|
| `ats_utilities/checker/type/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/checker/type/itype_validator.py` | 12 | 0 | 100%|
| `ats_utilities/checker/type/type_validator.py` | 46 | 0 | 100%|
| `ats_utilities/config_io/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/conf_file.py` | 55 | 0 | 100%|
| `ats_utilities/config_io/conf_file_bundle.py` | 31 | 0 | 100%|
| `ats_utilities/config_io/conf_file_factory.py` | 18 | 0 | 100%|
| `ats_utilities/config_io/conf_file_params.py` | 15 | 0 | 100%|
| `ats_utilities/config_io/conf_file_registry.py` | 18 | 0 | 100%|
| `ats_utilities/config_io/config_io_bundle.py` | 38 | 0 | 100%|
| `ats_utilities/config_io/config_io_params.py` | 18 | 0 | 100%|
| `ats_utilities/config_io/config_io_registry.py` | 33 | 0 | 100%|
| `ats_utilities/config_io/iconf_file.py` | 16 | 0 | 100%|
| `ats_utilities/config_io/loader/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/loader/engine.py` | 53 | 0 | 100%|
| `ats_utilities/config_io/loader/iloader.py` | 14 | 0 | 100%|
| `ats_utilities/config_io/processor/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/processor/cfg_processor.py` | 56 | 0 | 100%|
| `ats_utilities/config_io/processor/factory_processor.py` | 56 | 0 | 100%|
| `ats_utilities/config_io/processor/iconfig_processor.py` | 13 | 0 | 100%|
| `ats_utilities/config_io/processor/ifactory_processor.py` | 13 | 0 | 100%|
| `ats_utilities/config_io/processor/ini_processor.py` | 94 | 0 | 100%|
| `ats_utilities/config_io/processor/json_processor.py` | 52 | 0 | 100%|
| `ats_utilities/config_io/processor/xml_processor.py` | 94 | 0 | 100%|
| `ats_utilities/config_io/processor/yaml_processor.py` | 52 | 0 | 100%|
| `ats_utilities/config_io/storer/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/storer/engine.py` | 56 | 0 | 100%|
| `ats_utilities/config_io/storer/istorer.py` | 14 | 0 | 100%|
| `ats_utilities/context/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/context/context_bundle.py` | 36 | 0 | 100%|
| `ats_utilities/context/context_factory.py` | 26 | 0 | 100%|
| `ats_utilities/context/context_params.py` | 18 | 0 | 100%|
| `ats_utilities/context/context_registry.py` | 19 | 0 | 100%|
| `ats_utilities/context/context_support.py` | 46 | 0 | 100%|
| `ats_utilities/context/icontext_support.py` | 14 | 0 | 100%|
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
| `ats_utilities/generator/engine.py` | 76 | 0 | 100%|
| `ats_utilities/generator/gen_params_bundle.py` | 41 | 0 | 100%|
| `ats_utilities/generator/gen_params_params.py` | 17 | 0 | 100%|
| `ats_utilities/generator/gen_params_registry.py` | 27 | 0 | 100%|
| `ats_utilities/generator/generator_bundle.py` | 37 | 0 | 100%|
| `ats_utilities/generator/generator_factory.py` | 21 | 0 | 100%|
| `ats_utilities/generator/generator_params.py` | 19 | 0 | 100%|
| `ats_utilities/generator/generator_registry.py` | 19 | 0 | 100%|
| `ats_utilities/generator/igenerator.py` | 15 | 0 | 100%|
| `ats_utilities/generator/scheme/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/generator/scheme/engine.py` | 50 | 0 | 100%|
| `ats_utilities/generator/scheme/ischeme_loader.py` | 14 | 0 | 100%|
| `ats_utilities/generator/tar/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/generator/tar/engine.py` | 72 | 0 | 100%|
| `ats_utilities/generator/tar/itar_processor.py` | 14 | 0 | 100%|
| `ats_utilities/generator/tar/tar_process_bundle.py` | 40 | 0 | 100%|
| `ats_utilities/generator/tar/tar_process_member_bundle.py` | 35 | 0 | 100%|
| `ats_utilities/generator/tar/tar_process_member_params.py` | 17 | 0 | 100%|
| `ats_utilities/generator/tar/tar_process_member_registry.py` | 27 | 0 | 100%|
| `ats_utilities/generator/tar/tar_process_params.py` | 18 | 0 | 100%|
| `ats_utilities/generator/tar/tar_process_registry.py` | 28 | 0 | 100%|
| `ats_utilities/generator/template/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/generator/template/engine.py` | 35 | 0 | 100%|
| `ats_utilities/generator/template/itemplate_processor.py` | 12 | 0 | 100%|
| `ats_utilities/info/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/build_date/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/build_date/engine.py` | 39 | 0 | 100%|
| `ats_utilities/info/build_date/ibuild_date.py` | 12 | 0 | 100%|
| `ats_utilities/info/engine.py` | 81 | 0 | 100%|
| `ats_utilities/info/iinfo_manager.py` | 15 | 0 | 100%|
| `ats_utilities/info/info_bundle.py` | 65 | 0 | 100%|
| `ats_utilities/info/info_factory.py` | 52 | 0 | 100%|
| `ats_utilities/info/info_keys.py` | 30 | 0 | 100%|
| `ats_utilities/info/info_ok/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/info_ok/engine.py` | 39 | 0 | 100%|
| `ats_utilities/info/info_ok/iinfo_ok.py` | 12 | 0 | 100%|
| `ats_utilities/info/info_params.py` | 35 | 0 | 100%|
| `ats_utilities/info/info_registry.py` | 20 | 0 | 100%|
| `ats_utilities/info/licence/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/licence/engine.py` | 39 | 0 | 100%|
| `ats_utilities/info/licence/ilicence.py` | 12 | 0 | 100%|
| `ats_utilities/info/log_file/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/log_file/engine.py` | 39 | 0 | 100%|
| `ats_utilities/info/log_file/ilog_file.py` | 12 | 0 | 100%|
| `ats_utilities/info/logo/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/logo/engine.py` | 39 | 0 | 100%|
| `ats_utilities/info/logo/ilogo.py` | 12 | 0 | 100%|
| `ats_utilities/info/name/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/name/engine.py` | 39 | 0 | 100%|
| `ats_utilities/info/name/iname.py` | 12 | 0 | 100%|
| `ats_utilities/info/organization/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/organization/engine.py` | 39 | 0 | 100%|
| `ats_utilities/info/organization/iorganization.py` | 12 | 0 | 100%|
| `ats_utilities/info/repository/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/repository/engine.py` | 39 | 0 | 100%|
| `ats_utilities/info/repository/irepository.py` | 12 | 0 | 100%|
| `ats_utilities/info/use_github/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/use_github/engine.py` | 39 | 0 | 100%|
| `ats_utilities/info/use_github/iuse_github.py` | 12 | 0 | 100%|
| `ats_utilities/info/version/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/version/engine.py` | 39 | 0 | 100%|
| `ats_utilities/info/version/iversion.py` | 12 | 0 | 100%|
| `ats_utilities/logger/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/logger/engine.py` | 142 | 0 | 100%|
| `ats_utilities/logger/ilogger.py` | 12 | 0 | 100%|
| `ats_utilities/logger/logger_bundle.py` | 30 | 0 | 100%|
| `ats_utilities/logger/logger_factory.py` | 24 | 0 | 100%|
| `ats_utilities/logger/logger_params.py` | 15 | 0 | 100%|
| `ats_utilities/logger/logger_registry.py` | 19 | 0 | 100%|
| `ats_utilities/option/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/option/command/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/option/command/command_option.py` | 51 | 0 | 100%|
| `ats_utilities/option/command/ioption_command.py` | 13 | 0 | 100%|
| `ats_utilities/option/engine.py` | 73 | 0 | 100%|
| `ats_utilities/option/ioption_manager.py` | 18 | 0 | 100%|
| `ats_utilities/option/option_bundle.py` | 33 | 0 | 100%|
| `ats_utilities/option/option_factory.py` | 23 | 0 | 100%|
| `ats_utilities/option/option_namespace.py` | 15 | 0 | 100%|
| `ats_utilities/option/option_params.py` | 19 | 0 | 100%|
| `ats_utilities/option/option_registry.py` | 20 | 0 | 100%|
| `ats_utilities/option/parser/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/option/parser/engine.py` | 46 | 0 | 100%|
| `ats_utilities/option/parser/iarg_parser.py` | 15 | 0 | 100%|
| `ats_utilities/option/parser/parser_bundle.py` | 34 | 0 | 100%|
| `ats_utilities/option/parser/parser_params.py` | 15 | 0 | 100%|
| `ats_utilities/option/parser/parser_registry.py` | 26 | 0 | 100%|
| `ats_utilities/option/strategy/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/option/strategy/engine.py` | 93 | 0 | 100%|
| `ats_utilities/option/strategy/iparser_strategy.py` | 17 | 0 | 100%|
| `ats_utilities/option/strategy/parser_strategy_bundle.py` | 38 | 0 | 100%|
| `ats_utilities/option/strategy/parser_strategy_params.py` | 17 | 0 | 100%|
| `ats_utilities/option/strategy/parser_strategy_registry.py` | 28 | 0 | 100%|
| `ats_utilities/project_setup/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/project_setup/ipro_config.py` | 14 | 0 | 100%|
| `ats_utilities/project_setup/ipro_name.py` | 12 | 0 | 100%|
| `ats_utilities/project_setup/itemplate_dir.py` | 12 | 0 | 100%|
| `ats_utilities/project_setup/pro_config.py` | 43 | 0 | 100%|
| `ats_utilities/project_setup/pro_name.py` | 39 | 0 | 100%|
| `ats_utilities/project_setup/project_setup_bundle.py` | 36 | 0 | 100%|
| `ats_utilities/project_setup/project_setup_factory.py` | 26 | 0 | 100%|
| `ats_utilities/project_setup/project_setup_params.py` | 20 | 0 | 100%|
| `ats_utilities/project_setup/project_setup_registry.py` | 19 | 0 | 100%|
| `ats_utilities/project_setup/template_dir.py` | 39 | 0 | 100%|
| `ats_utilities/reporter/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/reporter/engine.py` | 68 | 0 | 100%|
| `ats_utilities/reporter/ireporter.py` | 13 | 0 | 100%|
| `ats_utilities/reporter/proxy_reporter.py` | 62 | 0 | 100%|
| `ats_utilities/reporter/reporter_bundle.py` | 33 | 0 | 100%|
| `ats_utilities/reporter/reporter_factory.py` | 22 | 0 | 100%|
| `ats_utilities/reporter/reporter_params.py` | 17 | 0 | 100%|
| `ats_utilities/reporter/reporter_registry.py` | 18 | 0 | 100%|
| `ats_utilities/reporter/theme/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/reporter/theme/engine.py` | 33 | 0 | 100%|
| `ats_utilities/reporter/theme/iconsole_theme.py` | 11 | 0 | 100%|
| `ats_utilities/splasher/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/splasher/engine.py` | 80 | 0 | 99%|
| `ats_utilities/splasher/external/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/splasher/external/ext_infrastructure.py` | 66 | 0 | 100%|
| `ats_utilities/splasher/external/github_infrastructure.py` | 75 | 0 | 100%|
| `ats_utilities/splasher/external/iext_infrastructure.py` | 14 | 0 | 100%|
| `ats_utilities/splasher/isplasher.py` | 14 | 0 | 100%|
| `ats_utilities/splasher/progressbar/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/splasher/progressbar/iprogress_bar.py` | 11 | 0 | 100%|
| `ats_utilities/splasher/progressbar/progress_bar.py` | 60 | 0 | 100%|
| `ats_utilities/splasher/property/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/splasher/property/isplash_property.py` | 14 | 0 | 100%|
| `ats_utilities/splasher/property/splash_property.py` | 49 | 0 | 100%|
| `ats_utilities/splasher/splash_bundle.py` | 46 | 1 | 98%|
| `ats_utilities/splasher/splash_center_bundle.py` | 29 | 0 | 100%|
| `ats_utilities/splasher/splash_center_params.py` | 13 | 0 | 100%|
| `ats_utilities/splasher/splash_center_registry.py` | 21 | 0 | 100%|
| `ats_utilities/splasher/splash_factory.py` | 41 | 0 | 98%|
| `ats_utilities/splasher/splash_keys.py` | 59 | 0 | 100%|
| `ats_utilities/splasher/splash_params.py` | 24 | 0 | 100%|
| `ats_utilities/splasher/splash_registry.py` | 20 | 1 | 95%|
| `ats_utilities/splasher/terminal/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/splasher/terminal/iterminal_properties.py` | 13 | 0 | 100%|
| `ats_utilities/splasher/terminal/terminal_properties.py` | 59 | 0 | 100%|
| `ats_utilities/utils/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/utils/boolean.py` | 19 | 0 | 100%|
| `ats_utilities/utils/component.py` | 16 | 0 | 100%|
| `ats_utilities/utils/dicts.py` | 36 | 0 | 100%|
| `ats_utilities/utils/dirs.py` | 19 | 0 | 100%|
| `ats_utilities/utils/files.py` | 123 | 0 | 100%|
| `ats_utilities/utils/iregistry.py` | 12 | 0 | 100%|
| `ats_utilities/utils/reflection.py` | 48 | 0 | 100%|
| `ats_utilities/validation/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/validation/check_type.py` | 37 | 0 | 100%|
| `ats_utilities/validation/check_value.py` | 26 | 0 | 100%|
| `ats_utilities/validation/context_error.py` | 14 | 0 | 100%|
| **Total** | 6140 | 2 | 99% |

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
