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

**ats_utilities** is based on OOP and following SOLID principles and it is organized in packages.

<details>
<summary><b>Click to expand framework structure</b></summary>

```bash
    ats_utilities/
         ├── base/
         │   ├── component_bundle.py
         │   ├── engine.py
         │   ├── ibase.py
         │   └── __init__.py
         ├── checker/
         │   ├── component_bundle.py
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
         │   │   ├── icheck_reporter.py
         │   │   └── __init__.py
         │   └── type/
         │       ├── __init__.py
         │       ├── itype_validator.py
         │       └── type_validator.py
         ├── config_io/
         │   ├── conf_file.py
         │   ├── config_file_bundle.py
         │   ├── file_bundle.py
         │   ├── file_check.py
         │   ├── iconf_file.py
         │   ├── ifile_check.py
         │   ├── __init__.py
         │   ├── loader/
         │   │   ├── config_loader.py
         │   │   ├── config_loader_bundle.py
         │   │   ├── file2object.py
         │   │   ├── iconfig_loader.py
         │   │   ├── iloader.py
         │   │   ├── __init__.py
         │   │   └── iread.py
         │   ├── processor/
         │   │   ├── cfg_processor.py
         │   │   ├── icfg_processor.py
         │   │   ├── iini_processor.py
         │   │   ├── ijson_processor.py
         │   │   ├── ini_processor.py
         │   │   ├── __init__.py
         │   │   ├── ixml_processor.py
         │   │   ├── iyaml_processor.py
         │   │   ├── json_processor.py
         │   │   ├── xml_processor.py
         │   │   └── yaml_processor.py
         │   └── storer/
         │       ├── config_storer.py
         │       ├── __init__.py
         │       ├── istorer.py
         │       ├── iwrite.py
         │       └── object2file.py
         ├── config_setup/
         │   ├── component_bundle.py
         │   ├── __init__.py
         │   ├── ipro_config.py
         │   ├── ipro_name.py
         │   ├── itemplate_dir.py
         │   ├── pro_config.py
         │   ├── pro_name.py
         │   └── template_dir.py
         ├── context_bundle.py
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
         │   └── __init__.py
         ├── factory_class.py
         ├── factory_component.py
         ├── factory_context_bundle.py
         ├── factory_context_error.py
         ├── factory_dict_utils.py
         ├── factory_file_utils.py
         ├── factory_inspector.py
         ├── factory_type.py
         ├── factory_value.py
         ├── generator/
         │   ├── component_bundle.py
         │   ├── engine.py
         │   ├── generator_bundle.py
         │   ├── igenerator.py
         │   ├── __init__.py
         │   ├── scheme/
         │   │   ├── __init__.py
         │   │   ├── ischeme_loader.py
         │   │   └── scheme_loader.py
         │   ├── tar/
         │   │   ├── __init__.py
         │   │   ├── itar_processor.py
         │   │   ├── tar_process_bundle.py
         │   │   ├── tar_process_member_bundle.py
         │   │   └── tar_processor.py
         │   └── template/
         │       ├── __init__.py
         │       ├── itemplate_processor.py
         │       └── template_processor.py
         ├── info/
         │   ├── build_date/
         │   │   ├── engine.py
         │   │   ├── ibuild_date.py
         │   │   └── __init__.py
         │   ├── component_bundle.py
         │   ├── engine.py
         │   ├── imanager.py
         │   ├── info_keys.py
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
         │   ├── component_bundle.py
         │   ├── engine.py
         │   ├── ilogger.py
         │   └── __init__.py
         ├── option/
         │   ├── command/
         │   │   ├── command_option.py
         │   │   ├── __init__.py
         │   │   └── ioption_command.py
         │   ├── component_bundle.py
         │   ├── engine.py
         │   ├── __init__.py
         │   ├── ioption_manager.py
         │   ├── option_namespace.py
         │   ├── parser/
         │   │   ├── engine.py
         │   │   └── __init__.py
         │   └── strategy/
         │       ├── __init__.py
         │       ├── iparser_strategy.py
         │       └── parser_strategy.py
         ├── py.typed
         ├── reporter/
         │   ├── component_bundle.py
         │   ├── engine.py
         │   ├── __init__.py
         │   ├── ireporter.py
         │   ├── proxy_reporter.py
         │   └── theme/
         │       ├── engine.py
         │       ├── iconsole_theme.py
         │       └── __init__.py
         └── splasher/
             ├── component_bundle.py
             ├── engine.py
             ├── external/
             │   ├── ext_infrastructure.py
             │   ├── github_infrastructure.py
             │   ├── iext_infrastructure.py
             │   └── __init__.py
             ├── __init__.py
             ├── isplasher.py
             ├── progressbar/
             │   ├── __init__.py
             │   ├── iprogress_bar.py
             │   └── progress_bar.py
             ├── property/
             │   ├── __init__.py
             │   ├── isplash_property.py
             │   └── splash_property.py
             ├── splash_center_bundle.py
             ├── splash_keys.py
             └── terminal/
                 ├── __init__.py
                 ├── iterminal_properties.py
                 └── terminal_properties.py

     40 directories, 179 files
```
</details>

### Code coverage

<details>
<summary><b>Click to expand code coverage</b></summary>

| Name | Stmts | Miss | Cover |
|------|-------|------|-------|
| `ats_utilities/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/base/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/base/component_bundle.py` | 108 | 0 | 99%|
| `ats_utilities/base/engine.py` | 77 | 0 | 99%|
| `ats_utilities/base/ibase.py` | 16 | 0 | 100%|
| `ats_utilities/checker/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/checker/component_bundle.py` | 60 | 0 | 100%|
| `ats_utilities/checker/context/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/checker/context/context_provider.py` | 36 | 0 | 100%|
| `ats_utilities/checker/context/icontext_provider.py` | 11 | 0 | 100%|
| `ats_utilities/checker/engine.py` | 69 | 0 | 100%|
| `ats_utilities/checker/format/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/checker/format/format_validator.py` | 24 | 0 | 100%|
| `ats_utilities/checker/format/iformat_validator.py` | 11 | 0 | 100%|
| `ats_utilities/checker/ichecker.py` | 20 | 0 | 100%|
| `ats_utilities/checker/proxy_validator.py` | 59 | 0 | 100%|
| `ats_utilities/checker/reporter/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/checker/reporter/check_reporter.py` | 30 | 0 | 100%|
| `ats_utilities/checker/reporter/checker_reporter_bundle.py` | 45 | 0 | 100%|
| `ats_utilities/checker/reporter/icheck_reporter.py` | 12 | 0 | 100%|
| `ats_utilities/checker/type/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/checker/type/itype_validator.py` | 12 | 0 | 100%|
| `ats_utilities/checker/type/type_validator.py` | 33 | 0 | 100%|
| `ats_utilities/config_io/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/conf_file.py` | 71 | 0 | 100%|
| `ats_utilities/config_io/config_file_bundle.py` | 34 | 0 | 100%|
| `ats_utilities/config_io/file_bundle.py` | 35 | 0 | 100%|
| `ats_utilities/config_io/file_check.py` | 71 | 0 | 100%|
| `ats_utilities/config_io/iconf_file.py` | 15 | 0 | 100%|
| `ats_utilities/config_io/ifile_check.py` | 13 | 0 | 100%|
| `ats_utilities/config_io/loader/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/loader/config_loader.py` | 59 | 0 | 100%|
| `ats_utilities/config_io/loader/config_loader_bundle.py` | 41 | 0 | 100%|
| `ats_utilities/config_io/loader/file2object.py` | 96 | 1 | 97%|
| `ats_utilities/config_io/loader/iconfig_loader.py` | 19 | 0 | 100%|
| `ats_utilities/config_io/loader/iloader.py` | 12 | 0 | 100%|
| `ats_utilities/config_io/loader/iread.py` | 12 | 0 | 100%|
| `ats_utilities/config_io/processor/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/processor/cfg_processor.py` | 36 | 0 | 100%|
| `ats_utilities/config_io/processor/icfg_processor.py` | 11 | 0 | 100%|
| `ats_utilities/config_io/processor/iini_processor.py` | 12 | 0 | 100%|
| `ats_utilities/config_io/processor/ijson_processor.py` | 11 | 0 | 100%|
| `ats_utilities/config_io/processor/ini_processor.py` | 44 | 0 | 100%|
| `ats_utilities/config_io/processor/ixml_processor.py` | 11 | 0 | 100%|
| `ats_utilities/config_io/processor/iyaml_processor.py` | 11 | 0 | 100%|
| `ats_utilities/config_io/processor/json_processor.py` | 33 | 0 | 100%|
| `ats_utilities/config_io/processor/xml_processor.py` | 46 | 0 | 100%|
| `ats_utilities/config_io/processor/yaml_processor.py` | 34 | 0 | 100%|
| `ats_utilities/config_io/storer/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/storer/config_storer.py` | 97 | 1 | 98%|
| `ats_utilities/config_io/storer/istorer.py` | 12 | 0 | 100%|
| `ats_utilities/config_io/storer/iwrite.py` | 12 | 0 | 100%|
| `ats_utilities/config_io/storer/object2file.py` | 71 | 2 | 95%|
| `ats_utilities/config_setup/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_setup/component_bundle.py` | 42 | 0 | 100%|
| `ats_utilities/config_setup/ipro_config.py` | 13 | 0 | 100%|
| `ats_utilities/config_setup/ipro_name.py` | 11 | 0 | 100%|
| `ats_utilities/config_setup/itemplate_dir.py` | 11 | 0 | 100%|
| `ats_utilities/config_setup/pro_config.py` | 50 | 0 | 100%|
| `ats_utilities/config_setup/pro_name.py` | 46 | 0 | 100%|
| `ats_utilities/config_setup/template_dir.py` | 46 | 0 | 100%|
| `ats_utilities/context_bundle.py` | 54 | 0 | 100%|
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
| `ats_utilities/factory_class.py` | 70 | 0 | 100%|
| `ats_utilities/factory_component.py` | 16 | 0 | 100%|
| `ats_utilities/factory_context_bundle.py` | 18 | 0 | 100%|
| `ats_utilities/factory_context_error.py` | 16 | 0 | 100%|
| `ats_utilities/factory_dict_utils.py` | 26 | 0 | 100%|
| `ats_utilities/factory_file_utils.py` | 116 | 0 | 100%|
| `ats_utilities/factory_inspector.py` | 25 | 0 | 100%|
| `ats_utilities/factory_type.py` | 37 | 0 | 100%|
| `ats_utilities/factory_value.py` | 21 | 0 | 100%|
| `ats_utilities/generator/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/generator/component_bundle.py` | 55 | 0 | 100%|
| `ats_utilities/generator/engine.py` | 87 | 0 | 100%|
| `ats_utilities/generator/generator_bundle.py` | 42 | 0 | 100%|
| `ats_utilities/generator/igenerator.py` | 14 | 0 | 100%|
| `ats_utilities/generator/scheme/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/generator/scheme/ischeme_loader.py` | 13 | 0 | 100%|
| `ats_utilities/generator/scheme/scheme_loader.py` | 53 | 0 | 100%|
| `ats_utilities/generator/tar/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/generator/tar/itar_processor.py` | 13 | 0 | 100%|
| `ats_utilities/generator/tar/tar_process_bundle.py` | 45 | 0 | 100%|
| `ats_utilities/generator/tar/tar_process_member_bundle.py` | 40 | 0 | 100%|
| `ats_utilities/generator/tar/tar_processor.py` | 73 | 0 | 100%|
| `ats_utilities/generator/template/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/generator/template/itemplate_processor.py` | 11 | 0 | 100%|
| `ats_utilities/generator/template/template_processor.py` | 40 | 0 | 100%|
| `ats_utilities/info/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/build_date/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/build_date/engine.py` | 46 | 0 | 100%|
| `ats_utilities/info/build_date/ibuild_date.py` | 11 | 0 | 100%|
| `ats_utilities/info/component_bundle.py` | 103 | 0 | 100%|
| `ats_utilities/info/engine.py` | 89 | 0 | 100%|
| `ats_utilities/info/imanager.py` | 14 | 0 | 100%|
| `ats_utilities/info/info_keys.py` | 29 | 0 | 100%|
| `ats_utilities/info/info_ok/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/info_ok/engine.py` | 46 | 0 | 100%|
| `ats_utilities/info/info_ok/iinfo_ok.py` | 11 | 0 | 100%|
| `ats_utilities/info/licence/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/licence/engine.py` | 46 | 0 | 100%|
| `ats_utilities/info/licence/ilicence.py` | 11 | 0 | 100%|
| `ats_utilities/info/log_file/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/log_file/engine.py` | 46 | 0 | 100%|
| `ats_utilities/info/log_file/ilog_file.py` | 11 | 0 | 100%|
| `ats_utilities/info/logo/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/logo/engine.py` | 46 | 0 | 100%|
| `ats_utilities/info/logo/ilogo.py` | 11 | 0 | 100%|
| `ats_utilities/info/name/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/name/engine.py` | 46 | 0 | 100%|
| `ats_utilities/info/name/iname.py` | 11 | 0 | 100%|
| `ats_utilities/info/organization/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/organization/engine.py` | 46 | 0 | 100%|
| `ats_utilities/info/organization/iorganization.py` | 11 | 0 | 100%|
| `ats_utilities/info/repository/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/repository/engine.py` | 46 | 0 | 100%|
| `ats_utilities/info/repository/irepository.py` | 11 | 0 | 100%|
| `ats_utilities/info/use_github/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/use_github/engine.py` | 46 | 0 | 100%|
| `ats_utilities/info/use_github/iuse_github.py` | 11 | 0 | 100%|
| `ats_utilities/info/version/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/version/engine.py` | 46 | 0 | 100%|
| `ats_utilities/info/version/iversion.py` | 11 | 0 | 100%|
| `ats_utilities/logger/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/logger/component_bundle.py` | 43 | 1 | 94%|
| `ats_utilities/logger/engine.py` | 94 | 14 | 74%|
| `ats_utilities/logger/ilogger.py` | 12 | 0 | 100%|
| `ats_utilities/option/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/option/command/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/option/command/command_option.py` | 49 | 0 | 100%|
| `ats_utilities/option/command/ioption_command.py` | 13 | 0 | 100%|
| `ats_utilities/option/component_bundle.py` | 45 | 0 | 100%|
| `ats_utilities/option/engine.py` | 85 | 0 | 100%|
| `ats_utilities/option/ioption_manager.py` | 17 | 0 | 100%|
| `ats_utilities/option/option_namespace.py` | 15 | 0 | 100%|
| `ats_utilities/option/parser/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/option/parser/engine.py` | 37 | 0 | 100%|
| `ats_utilities/option/strategy/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/option/strategy/iparser_strategy.py` | 16 | 0 | 100%|
| `ats_utilities/option/strategy/parser_strategy.py` | 94 | 0 | 100%|
| `ats_utilities/reporter/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/reporter/component_bundle.py` | 49 | 0 | 100%|
| `ats_utilities/reporter/engine.py` | 73 | 4 | 90%|
| `ats_utilities/reporter/ireporter.py` | 13 | 0 | 100%|
| `ats_utilities/reporter/proxy_reporter.py` | 57 | 0 | 100%|
| `ats_utilities/reporter/theme/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/reporter/theme/engine.py` | 33 | 0 | 100%|
| `ats_utilities/reporter/theme/iconsole_theme.py` | 11 | 0 | 100%|
| `ats_utilities/splasher/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/splasher/component_bundle.py` | 88 | 0 | 100%|
| `ats_utilities/splasher/engine.py` | 103 | 1 | 98%|
| `ats_utilities/splasher/external/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/splasher/external/ext_infrastructure.py` | 69 | 0 | 100%|
| `ats_utilities/splasher/external/github_infrastructure.py` | 78 | 0 | 100%|
| `ats_utilities/splasher/external/iext_infrastructure.py` | 13 | 0 | 100%|
| `ats_utilities/splasher/isplasher.py` | 13 | 0 | 100%|
| `ats_utilities/splasher/progressbar/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/splasher/progressbar/iprogress_bar.py` | 11 | 0 | 100%|
| `ats_utilities/splasher/progressbar/progress_bar.py` | 60 | 0 | 100%|
| `ats_utilities/splasher/property/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/splasher/property/isplash_property.py` | 13 | 0 | 100%|
| `ats_utilities/splasher/property/splash_property.py` | 55 | 0 | 100%|
| `ats_utilities/splasher/splash_center_bundle.py` | 44 | 0 | 100%|
| `ats_utilities/splasher/splash_keys.py` | 59 | 0 | 100%|
| `ats_utilities/splasher/terminal/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/splasher/terminal/iterminal_properties.py` | 12 | 0 | 100%|
| `ats_utilities/splasher/terminal/terminal_properties.py` | 62 | 0 | 100%|
| **Total** | 5379 | 24 | 99% |

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
