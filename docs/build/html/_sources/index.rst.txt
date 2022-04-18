ATS Utilities
--------------

☯️ **ats_utilities** is framework for creating Apps/Tools/Scripts.

Developed in 🐍 `python <https://www.python.org/>`_ code.

|ats_utilities codecov| |ats_utilities circleci|

.. |ats_utilities codecov| image:: https://codecov.io/gh/vroncevic/ats_utilities/branch/dev/graph/badge.svg
   :target: https://codecov.io/gh/vroncevic/ats_utilities

.. |ats_utilities circleci| image:: https://circleci.com/gh/vroncevic/ats_utilities/tree/master.svg
   :target: https://circleci.com/gh/vroncevic/ats_utilities/tree/master

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|ats_utilities python checker| |ats_utilities package checker|

|ats_utilities github issues| |ats_utilities github contributors|

|ats_utilities documentation status|

.. |ats_utilities python checker| image:: https://img.shields.io/github/workflow/status/vroncevic/ats_utilities/ats_utilities_python_checker?style=flat&label=ats_utilities%20python%20checker
   :target: https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_python_checker.yml

.. |ats_utilities package checker| image:: https://img.shields.io/github/workflow/status/vroncevic/ats_utilities/ats_utilities_package_checker?style=flat&label=ats_utilities%20package%20checker
   :target: https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_package.yml

.. |ats_utilities github issues| image:: https://img.shields.io/github/issues/vroncevic/ats_utilities.svg
   :target: https://github.com/vroncevic/ats_utilities/issues

.. |ats_utilities github contributors| image:: https://img.shields.io/github/contributors/vroncevic/ats_utilities.svg
   :target: https://github.com/vroncevic/ats_utilities/graphs/contributors

.. |ats_utilities documentation Status| image:: https://readthedocs.org/projects/ats-utilities/badge/?version=master
   :target: https://ats-utilities.readthedocs.io/en/master/?badge=master

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

|ats_utilities python2 build| |ats_utilities python3 build|

.. |ats_utilities python2 build| image:: https://img.shields.io/github/workflow/status/vroncevic/ats_utilities/ats_utilities_python2_build?style=flat&label=ats_utilities%20python2%20build
   :target: https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_python2_build.yml

.. |ats_utilities python3 build| image:: https://img.shields.io/github/workflow/status/vroncevic/ats_utilities/ats_utilities_python3_build?style=flat&label=ats_utilities%20python3%20build
   :target: https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_python3_build.yml

Navigate to release `page`_ download and extract release archive 📦.

.. _page: https://github.com/vroncevic/ats_utilities/releases

To install **ats_utilities** 📦 run

.. code-block:: bash

    tar xvzf ats_utilities-x.y.z.tar.gz
    cd ats_utilities-x.y.z
    # python2
    wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
    python2 get-pip.py
    python2 -m pip install --upgrade setuptools
    python2 -m pip install --upgrade pip
    python2 -m pip install --upgrade build
    pip2 install -r requirements.txt
    python2 -m build --no-isolation --wheel
    pip2 install dist/ats_utilities-x.y.z-py2-none-any.whl
    rm -f get-pip.py
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
    # python2
    wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
    python2 get-pip.py
    python2 -m pip install --upgrade setuptools
    python2 -m pip install --upgrade pip
    python2 -m pip install --upgrade build
    pip2 install -r requirements.txt
    python2 setup.py install_lib
    python2 setup.py install_egg_info
    # pyton3
    wget https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py 
    python3 -m pip install --upgrade setuptools
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade build
    pip3 install -r requirements.txt
    python3 setup.py install_lib
    python3 setup.py install_egg_info

You can use Docker to create image/container, or You can use pip to install 📦

.. code-block:: bash

    # python2
    pip2 install ats_utilities
    # python3
    pip3 install ats_utilities

|ats_utilities docker checker|

.. |ats_utilities docker checker| image:: https://img.shields.io/github/workflow/status/vroncevic/ats_utilities/ats_utilities_docker_checker?style=flat&label=ats_utilities%20docker%20checker
   :target: https://github.com/vroncevic/ats_utilities/actions/workflows/ats_utilities_docker_checker.yml

Dependencies
-------------

**ats_utilities** requires next modules and libraries

* `six - Python 2 and 3 compatibility library <https://pypi.org/project/six/>`_
* `yaml - YAML parser and emitter for Python <https://pypi.org/project/PyYAML/>`_
* `bs4 - Screen-scraping library <https://pypi.org/project/beautifulsoup4/>`_
* `configparser - Configuration parser library <https://pypi.org/project/configparser/>`_
* `colorama - Cross-platform colored terminal text <https://pypi.org/project/colorama/>`_

Framework structure
--------------------

**ats_utilities** is based on OOP.

.. image:: https://raw.githubusercontent.com/vroncevic/ats_utilities/dev/docs/arch_flow_usage.png

🧰 Framework structure

.. code-block:: bash

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

Copyright and licence
----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2017 by `vroncevic.github.io/ats_utilities <https://vroncevic.github.io/ats_utilities>`_

**ats_utilities** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

🌎 🌍 🌏 Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/ats_utilities/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
   :target: https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
