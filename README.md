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
        │   ├── checker_reporter_bundle.py
        │   ├── check_reporter.py
        │   ├── component_bundle.py
        │   ├── context_provider.py
        │   ├── engine.py
        │   ├── format_validator.py
        │   ├── ichecker.py
        │   ├── icheck_reporter.py
        │   ├── icontext_provider.py
        │   ├── iformat_validator.py
        │   ├── __init__.py
        │   ├── itype_validator.py
        │   ├── proxy_validator.py
        │   └── type_validator.py
        ├── config_io/
        │   ├── cfg/
        │   │   ├── cfg2object.py
        │   │   ├── cfg_loader.py
        │   │   ├── cfg_processor.py
        │   │   ├── cfg_storer.py
        │   │   ├── icfg_processor.py
        │   │   ├── __init__.py
        │   │   └── object2cfg.py
        │   ├── conf_file.py
        │   ├── config_file_bundle.py
        │   ├── config_loader_bundle.py
        │   ├── config_loader.py
        │   ├── file_bundle.py
        │   ├── file_check.py
        │   ├── iconf_file.py
        │   ├── iconfig_loader.py
        │   ├── ifile_check.py
        │   ├── iloader.py
        │   ├── ini/
        │   │   ├── iini_processor.py
        │   │   ├── ini2object.py
        │   │   ├── ini_loader.py
        │   │   ├── ini_processor.py
        │   │   ├── ini_storer.py
        │   │   ├── __init__.py
        │   │   └── object2ini.py
        │   ├── __init__.py
        │   ├── iread.py
        │   ├── istorer.py
        │   ├── iwrite.py
        │   ├── json/
        │   │   ├── ijson_processor.py
        │   │   ├── __init__.py
        │   │   ├── json2object.py
        │   │   ├── json_loader.py
        │   │   ├── json_processor.py
        │   │   ├── json_storer.py
        │   │   └── object2json.py
        │   ├── xml/
        │   │   ├── __init__.py
        │   │   ├── ixml_processor.py
        │   │   ├── object2xml.py
        │   │   ├── xml2object.py
        │   │   ├── xml_loader.py
        │   │   ├── xml_processor.py
        │   │   └── xml_storer.py
        │   └── yaml/
        │       ├── __init__.py
        │       ├── iyaml_processor.py
        │       ├── object2yaml.py
        │       ├── yaml2object.py
        │       ├── yaml_loader.py
        │       ├── yaml_processor.py
        │       └── yaml_storer.py
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
        ├── factory_dict_utils.py
        ├── factory_file_utils.py
        ├── generator/
        │   ├── component_bundle.py
        │   ├── engine.py
        │   ├── generator_bundle.py
        │   ├── igenerator.py
        │   ├── __init__.py
        │   ├── ischeme_loader.py
        │   ├── itar_processor.py
        │   ├── itemplate_processor.py
        │   ├── scheme_loader.py
        │   ├── tar_process_bundle.py
        │   ├── tar_process_member_bundle.py
        │   ├── tar_processor.py
        │   └── template_processor.py
        ├── info/
        │   ├── build_date.py
        │   ├── component_bundle.py
        │   ├── engine.py
        │   ├── ibuild_date.py
        │   ├── iinfo_ok.py
        │   ├── ilicence.py
        │   ├── ilogo_path.py
        │   ├── imanager.py
        │   ├── iname.py
        │   ├── info_keys.py
        │   ├── info_ok.py
        │   ├── __init__.py
        │   ├── iorganization.py
        │   ├── irepository.py
        │   ├── iuse_github.py
        │   ├── iversion.py
        │   ├── licence.py
        │   ├── logo.py
        │   ├── name.py
        │   ├── organization.py
        │   ├── repository.py
        │   ├── use_github.py
        │   └── version.py
        ├── __init__.py
        ├── logging/
        │   ├── component_bundle.py
        │   ├── engine.py
        │   ├── ilogger_manager.py
        │   ├── ilogger.py
        │   ├── __init__.py
        │   ├── logger_bundle.py
        │   └── logger.py
        ├── option/
        │   ├── arg_parser.py
        │   ├── command_option.py
        │   ├── component_bundle.py
        │   ├── engine.py
        │   ├── __init__.py
        │   ├── ioption_command.py
        │   ├── ioption_parser.py
        │   ├── iparser_strategy.py
        │   ├── option_namespace.py
        │   └── parser_strategy.py
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
            ├── ext_infrastructure.py
            ├── github_infrastructure.py
            ├── iext_infrastructure.py
            ├── __init__.py
            ├── iprogress_bar.py
            ├── isplasher.py
            ├── isplash_property.py
            ├── iterminal_properties.py
            ├── progress_bar.py
            ├── splash_center_bundle.py
            ├── splash_keys.py
            ├── splash_property.py
            └── terminal_properties.py

    18 directories, 171 files
```

</details>

### Code coverage

<details>
<summary><b>Click to expand code coverage</b></summary>

| Name | Stmts | Miss | Cover |
|------|-------|------|-------|
| `ats_utilities/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/base/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/base/component_bundle.py` | 110 | 19 | 81%|
| `ats_utilities/base/engine.py` | 81 | 4 | 93%|
| `ats_utilities/base/ibase.py` | 16 | 0 | 100%|
| `ats_utilities/checker/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/checker/check_reporter.py` | 30 | 0 | 100%|
| `ats_utilities/checker/checker_reporter_bundle.py` | 44 | 3 | 92%|
| `ats_utilities/checker/component_bundle.py` | 59 | 0 | 99%|
| `ats_utilities/checker/context_provider.py` | 35 | 0 | 98%|
| `ats_utilities/checker/engine.py` | 68 | 0 | 99%|
| `ats_utilities/checker/format_validator.py` | 24 | 0 | 100%|
| `ats_utilities/checker/icheck_reporter.py` | 12 | 0 | 100%|
| `ats_utilities/checker/ichecker.py` | 20 | 0 | 100%|
| `ats_utilities/checker/icontext_provider.py` | 11 | 0 | 100%|
| `ats_utilities/checker/iformat_validator.py` | 11 | 0 | 100%|
| `ats_utilities/checker/itype_validator.py` | 12 | 0 | 100%|
| `ats_utilities/checker/proxy_validator.py` | 62 | 0 | 98%|
| `ats_utilities/checker/type_validator.py` | 33 | 1 | 95%|
| `ats_utilities/config_io/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/cfg/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/cfg/cfg2object.py` | 56 | 0 | 98%|
| `ats_utilities/config_io/cfg/cfg_loader.py` | 49 | 0 | 98%|
| `ats_utilities/config_io/cfg/cfg_processor.py` | 35 | 0 | 100%|
| `ats_utilities/config_io/cfg/cfg_storer.py` | 42 | 0 | 100%|
| `ats_utilities/config_io/cfg/icfg_processor.py` | 11 | 0 | 100%|
| `ats_utilities/config_io/cfg/object2cfg.py` | 58 | 0 | 100%|
| `ats_utilities/config_io/conf_file.py` | 69 | 0 | 100%|
| `ats_utilities/config_io/config_file_bundle.py` | 33 | 1 | 95%|
| `ats_utilities/config_io/config_loader.py` | 55 | 0 | 100%|
| `ats_utilities/config_io/config_loader_bundle.py` | 41 | 5 | 87%|
| `ats_utilities/config_io/file_bundle.py` | 33 | 0 | 97%|
| `ats_utilities/config_io/file_check.py` | 69 | 0 | 99%|
| `ats_utilities/config_io/iconf_file.py` | 15 | 0 | 100%|
| `ats_utilities/config_io/iconfig_loader.py` | 23 | 0 | 100%|
| `ats_utilities/config_io/ifile_check.py` | 13 | 0 | 100%|
| `ats_utilities/config_io/iloader.py` | 12 | 0 | 100%|
| `ats_utilities/config_io/ini/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/ini/iini_processor.py` | 12 | 0 | 100%|
| `ats_utilities/config_io/ini/ini2object.py` | 55 | 0 | 98%|
| `ats_utilities/config_io/ini/ini_loader.py` | 49 | 0 | 98%|
| `ats_utilities/config_io/ini/ini_processor.py` | 43 | 0 | 100%|
| `ats_utilities/config_io/ini/ini_storer.py` | 48 | 0 | 100%|
| `ats_utilities/config_io/ini/object2ini.py` | 57 | 0 | 98%|
| `ats_utilities/config_io/iread.py` | 12 | 0 | 100%|
| `ats_utilities/config_io/istorer.py` | 12 | 0 | 100%|
| `ats_utilities/config_io/iwrite.py` | 12 | 0 | 100%|
| `ats_utilities/config_io/json/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/json/ijson_processor.py` | 11 | 0 | 100%|
| `ats_utilities/config_io/json/json2object.py` | 56 | 0 | 98%|
| `ats_utilities/config_io/json/json_loader.py` | 49 | 0 | 98%|
| `ats_utilities/config_io/json/json_processor.py` | 32 | 0 | 100%|
| `ats_utilities/config_io/json/json_storer.py` | 47 | 0 | 100%|
| `ats_utilities/config_io/json/object2json.py` | 57 | 0 | 100%|
| `ats_utilities/config_io/xml/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/xml/ixml_processor.py` | 11 | 0 | 100%|
| `ats_utilities/config_io/xml/object2xml.py` | 60 | 0 | 97%|
| `ats_utilities/config_io/xml/xml2object.py` | 59 | 0 | 97%|
| `ats_utilities/config_io/xml/xml_loader.py` | 49 | 0 | 98%|
| `ats_utilities/config_io/xml/xml_processor.py` | 45 | 0 | 100%|
| `ats_utilities/config_io/xml/xml_storer.py` | 55 | 0 | 100%|
| `ats_utilities/config_io/yaml/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_io/yaml/iyaml_processor.py` | 11 | 0 | 100%|
| `ats_utilities/config_io/yaml/object2yaml.py` | 57 | 0 | 100%|
| `ats_utilities/config_io/yaml/yaml2object.py` | 57 | 0 | 98%|
| `ats_utilities/config_io/yaml/yaml_loader.py` | 49 | 0 | 98%|
| `ats_utilities/config_io/yaml/yaml_processor.py` | 33 | 0 | 100%|
| `ats_utilities/config_io/yaml/yaml_storer.py` | 47 | 0 | 100%|
| `ats_utilities/config_setup/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/config_setup/component_bundle.py` | 41 | 0 | 98%|
| `ats_utilities/config_setup/ipro_config.py` | 13 | 0 | 100%|
| `ats_utilities/config_setup/ipro_name.py` | 11 | 0 | 100%|
| `ats_utilities/config_setup/itemplate_dir.py` | 11 | 0 | 100%|
| `ats_utilities/config_setup/pro_config.py` | 48 | 0 | 100%|
| `ats_utilities/config_setup/pro_name.py` | 44 | 0 | 100%|
| `ats_utilities/config_setup/template_dir.py` | 44 | 0 | 100%|
| `ats_utilities/context_bundle.py` | 45 | 0 | 98%|
| `ats_utilities/exceptions/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/exceptions/ats_attribute_error.py` | 10 | 0 | 100%|
| `ats_utilities/exceptions/ats_bad_call_error.py` | 10 | 0 | 100%|
| `ats_utilities/exceptions/ats_error.py` | 10 | 0 | 100%|
| `ats_utilities/exceptions/ats_file_error.py` | 10 | 0 | 100%|
| `ats_utilities/exceptions/ats_generator_error.py` | 11 | 0 | 100%|
| `ats_utilities/exceptions/ats_key_error.py` | 10 | 0 | 100%|
| `ats_utilities/exceptions/ats_lookup_error.py` | 10 | 0 | 100%|
| `ats_utilities/exceptions/ats_parameter_error.py` | 10 | 0 | 100%|
| `ats_utilities/exceptions/ats_runtime_error.py` | 10 | 0 | 100%|
| `ats_utilities/exceptions/ats_type_error.py` | 10 | 0 | 100%|
| `ats_utilities/exceptions/ats_value_error.py` | 10 | 0 | 100%|
| `ats_utilities/factory_class.py` | 71 | 0 | 99%|
| `ats_utilities/factory_component.py` | 16 | 0 | 100%|
| `ats_utilities/factory_context_bundle.py` | 17 | 0 | 100%|
| `ats_utilities/factory_context_error.py` | 16 | 0 | 100%|
| `ats_utilities/factory_dict_utils.py` | 26 | 0 | 100%|
| `ats_utilities/factory_file_utils.py` | 117 | 16 | 82%|
| `ats_utilities/factory_inspector.py` | 25 | 3 | 77%|
| `ats_utilities/factory_type.py` | 15 | 0 | 100%|
| `ats_utilities/factory_value.py` | 21 | 0 | 100%|
| `ats_utilities/generator/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/generator/component_bundle.py` | 54 | 0 | 98%|
| `ats_utilities/generator/engine.py` | 86 | 0 | 100%|
| `ats_utilities/generator/generator_bundle.py` | 41 | 0 | 98%|
| `ats_utilities/generator/igenerator.py` | 14 | 0 | 100%|
| `ats_utilities/generator/ischeme_loader.py` | 13 | 0 | 100%|
| `ats_utilities/generator/itar_processor.py` | 13 | 0 | 100%|
| `ats_utilities/generator/itemplate_processor.py` | 11 | 0 | 100%|
| `ats_utilities/generator/scheme_loader.py` | 51 | 0 | 100%|
| `ats_utilities/generator/tar_process_bundle.py` | 44 | 0 | 98%|
| `ats_utilities/generator/tar_process_member_bundle.py` | 39 | 4 | 88%|
| `ats_utilities/generator/tar_processor.py` | 71 | 0 | 98%|
| `ats_utilities/generator/template_processor.py` | 40 | 0 | 100%|
| `ats_utilities/info/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/info/build_date.py` | 44 | 0 | 100%|
| `ats_utilities/info/component_bundle.py` | 103 | 0 | 99%|
| `ats_utilities/info/engine.py` | 85 | 1 | 96%|
| `ats_utilities/info/ibuild_date.py` | 11 | 0 | 100%|
| `ats_utilities/info/iinfo_ok.py` | 11 | 0 | 100%|
| `ats_utilities/info/ilicence.py` | 11 | 0 | 100%|
| `ats_utilities/info/ilogo_path.py` | 11 | 0 | 100%|
| `ats_utilities/info/imanager.py` | 14 | 0 | 100%|
| `ats_utilities/info/iname.py` | 11 | 0 | 100%|
| `ats_utilities/info/info_keys.py` | 28 | 0 | 100%|
| `ats_utilities/info/info_ok.py` | 44 | 1 | 98%|
| `ats_utilities/info/iorganization.py` | 11 | 0 | 100%|
| `ats_utilities/info/irepository.py` | 11 | 0 | 100%|
| `ats_utilities/info/iuse_github.py` | 11 | 0 | 100%|
| `ats_utilities/info/iversion.py` | 11 | 0 | 100%|
| `ats_utilities/info/licence.py` | 44 | 0 | 100%|
| `ats_utilities/info/logo.py` | 44 | 0 | 100%|
| `ats_utilities/info/name.py` | 44 | 0 | 100%|
| `ats_utilities/info/organization.py` | 44 | 0 | 100%|
| `ats_utilities/info/repository.py` | 44 | 0 | 100%|
| `ats_utilities/info/use_github.py` | 44 | 0 | 100%|
| `ats_utilities/info/version.py` | 44 | 0 | 100%|
| `ats_utilities/logging/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/logging/component_bundle.py` | 46 | 0 | 98%|
| `ats_utilities/logging/engine.py` | 61 | 0 | 100%|
| `ats_utilities/logging/ilogger.py` | 24 | 0 | 100%|
| `ats_utilities/logging/ilogger_manager.py` | 13 | 0 | 100%|
| `ats_utilities/logging/logger.py` | 64 | 0 | 100%|
| `ats_utilities/logging/logger_bundle.py` | 37 | 0 | 98%|
| `ats_utilities/option/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/option/arg_parser.py` | 35 | 0 | 100%|
| `ats_utilities/option/command_option.py` | 43 | 0 | 100%|
| `ats_utilities/option/component_bundle.py` | 44 | 3 | 92%|
| `ats_utilities/option/engine.py` | 86 | 0 | 99%|
| `ats_utilities/option/ioption_command.py` | 13 | 0 | 100%|
| `ats_utilities/option/ioption_manager.py` | 17 | 0 | 100%|
| `ats_utilities/option/iparser_strategy.py` | 16 | 0 | 100%|
| `ats_utilities/option/option_namespace.py` | 15 | 0 | 100%|
| `ats_utilities/option/parser_strategy.py` | 90 | 2 | 95%|
| `ats_utilities/reporter/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/reporter/component_bundle.py` | 41 | 0 | 98%|
| `ats_utilities/reporter/engine.py` | 60 | 0 | 98%|
| `ats_utilities/reporter/ireporter.py` | 13 | 0 | 100%|
| `ats_utilities/reporter/proxy_reporter.py` | 57 | 0 | 99%|
| `ats_utilities/reporter/theme/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/reporter/theme/engine.py` | 31 | 0 | 100%|
| `ats_utilities/reporter/theme/iconsole_theme.py` | 11 | 0 | 100%|
| `ats_utilities/splasher/__init__.py` | 9 | 0 | 100%|
| `ats_utilities/splasher/component_bundle.py` | 87 | 0 | 99%|
| `ats_utilities/splasher/engine.py` | 98 | 1 | 99%|
| `ats_utilities/splasher/ext_infrastructure.py` | 67 | 0 | 100%|
| `ats_utilities/splasher/github_infrastructure.py` | 76 | 0 | 100%|
| `ats_utilities/splasher/iext_infrastructure.py` | 13 | 0 | 100%|
| `ats_utilities/splasher/iprogress_bar.py` | 11 | 0 | 100%|
| `ats_utilities/splasher/isplash_property.py` | 13 | 0 | 100%|
| `ats_utilities/splasher/isplasher.py` | 13 | 0 | 100%|
| `ats_utilities/splasher/iterminal_properties.py` | 12 | 0 | 100%|
| `ats_utilities/splasher/progress_bar.py` | 53 | 0 | 100%|
| `ats_utilities/splasher/splash_center_bundle.py` | 43 | 2 | 91%|
| `ats_utilities/splasher/splash_keys.py` | 43 | 0 | 100%|
| `ats_utilities/splasher/splash_property.py` | 53 | 0 | 100%|
| `ats_utilities/splasher/terminal_properties.py` | 60 | 0 | 98%|
| **Total** | 5842 | 66 | 98% |

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
