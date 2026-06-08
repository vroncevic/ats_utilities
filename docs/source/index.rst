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
* `bs4 - Screen-scraping library <https://pypi.org/project/beautifulsoup4/>`_
* `colorama - Cross-platform colored terminal text <https://pypi.org/project/colorama/>`_
* `lxml - XML processing library <https://pypi.org/project/lxml/>`_

Framework structure
--------------------

**ats_utilities** is based on OOP.

Framework structure

.. code-block:: bash

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
   │   ├── icli.py
   │   └── __init__.py
   ├── config_io/
   │   ├── cfg/
   │   │   ├── cfg2object.py
   │   │   ├── cfgbase.py
   │   │   ├── __init__.py
   │   │   └── object2cfg.py
   │   ├── conf_file.py
   │   ├── file_check.py
   │   ├── iconf_file.py
   │   ├── ifile_check.py
   │   ├── ini/
   │   │   ├── ini2object.py
   │   │   ├── inibase.py
   │   │   ├── __init__.py
   │   │   └── object2ini.py
   │   ├── __init__.py
   │   ├── iread.py
   │   ├── iwrite.py
   │   ├── json/
   │   │   ├── __init__.py
   │   │   ├── json2object.py
   │   │   ├── jsonbase.py
   │   │   └── object2json.py
   │   ├── xml/
   │   │   ├── __init__.py
   │   │   ├── object2xml.py
   │   │   ├── xml2object.py
   │   │   └── xmlbase.py
   │   └── yaml/
   │       ├── __init__.py
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

   17 directories, 100 files

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
