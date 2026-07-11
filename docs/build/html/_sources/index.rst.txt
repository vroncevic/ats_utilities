ATS Utilities
--------------

**ats_utilities** is framework for creating Apps/Tools/Scripts.

Developed in `python <https://www.python.org/>`_ code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|ats_utilities python checker| |ats_utilities package checker|

|ats_utilities github issues| |ats_utilities github contributors|

|ats_utilities documentation status|

.. |ats_utilities python checker| image:: https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_python_checker.yml

.. |ats_utilities package checker| image:: https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_package.yml

.. |ats_utilities github issues| image:: https://img.shields.io/github/issues/vroncevic/ats_utilities.svg
   :target: https://github.com/vroncevic/ats_utilities/issues

.. |ats_utilities github contributors| image:: https://img.shields.io/github/contributors/vroncevic/ats_utilities.svg
   :target: https://github.com/vroncevic/ats_utilities/graphs/contributors

.. |ats_utilities documentation Status| image:: https://readthedocs.org/projects/ats-utilities/badge/?version=master
   :target: https://ats-utilities.readthedocs.io/?badge=master

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

Installation
-------------

Used next development environment

|debian linux os|

.. |debian linux os| image:: https://raw.githubusercontent.com/vroncevic/ats_utilities/dev/docs/debtux.png

|ats_utilities python3 build|

.. |ats_utilities python3 build| image:: https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/ats_utilities/releases

To install **ats_utilities** run

.. code-block:: bash

    tar xvzf ats_utilities-x.y.z.tar.gz
    cd ats_utilities-x.y.z
    # python3
    wget https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py 
    python3 -m pip install --upgrade setuptools
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade build
    pip3 install -r requirements.txt
    python3 -m build --no-isolation --wheel
    pip3 install dist/ats_utilities-x.y.z-py3-none-any.whl
    rm -f get-pip.py

Or type the following

.. code-block:: bash

    tar xvzf ats_utilities-x.y.z.tar.gz
    cd ats_utilities-x.y.z/
    # pyton3
    wget https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py 
    python3 -m pip install --upgrade setuptools
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade build
    pip3 install -r requirements.txt
    python3 setup.py install_lib
    python3 setup.py install_egg_info

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    # python3
    pip3 install ats_utilities

Dependencies
-------------

**ats_utilities** requires next modules and libraries

* `yaml - YAML parser and emitter for Python <https://pypi.org/project/PyYAML/>`_

Framework structure
--------------------

**ats_utilities** is based on OOP.

Framework structure

.. code-block:: bash

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
         │   ├── config_loader.py
         │   ├── config_loader_bundle.py
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
         ├── logging/
         │   ├── component_bundle.py
         │   ├── engine.py
         │   ├── ilogger_manager.py
         │   ├── __init__.py
         │   └── logger/
         │       ├── ilogger.py
         │       ├── __init__.py
         │       ├── logger.py
         │       └── logger_bundle.py
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

     42 directories, 199 files

Copyright and licence
----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2017 - 2026 by `vroncevic.github.io/ats_utilities <https://vroncevic.github.io/ats_utilities>`_

**ats_utilities** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/ats_utilities/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
   :target: https://www.python.org/psf/donations/

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
