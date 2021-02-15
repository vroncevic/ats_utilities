ATS Utilities
--------------

**ats_utilities** is framework for building Apps/Tools/Scripts.

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|Python package| |GitHub issues| |Documentation Status| |GitHub contributors|

.. |Python package| image:: https://github.com/vroncevic/ats_utilities/workflows/Python%20package/badge.svg
   :target: https://github.com/vroncevic/ats_utilities/workflows/Python%20package/badge.svg?branch=master

.. |GitHub issues| image:: https://img.shields.io/github/issues/vroncevic/ats_utilities.svg
   :target: https://github.com/vroncevic/ats_utilities/issues

.. |GitHub contributors| image:: https://img.shields.io/github/contributors/vroncevic/ats_utilities.svg
   :target: https://github.com/vroncevic/ats_utilities/graphs/contributors

.. |Documentation Status| image:: https://readthedocs.org/projects/ats_utilities/badge/?version=latest
   :target: https://ats_utilities.readthedocs.io/projects/ats_utilities/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   self
   modules

Installation
-------------

|Install Python2 Package| |Install Python3 Package|

.. |Install Python2 Package| image:: https://github.com/vroncevic/ats_utilities/workflows/Install%20Python2%20Package%20ats_utilities/badge.svg
   :target: https://github.com/vroncevic/ats_utilities/workflows/Install%20Python2%20Package%20ats_utilities/badge.svg?branch=master

.. |Install Python3 Package| image:: https://github.com/vroncevic/ats_utilities/workflows/Install%20Python3%20Package%20ats_utilities/badge.svg
   :target: https://github.com/vroncevic/ats_utilities/workflows/Install%20Python3%20Package%20ats_utilities/badge.svg?branch=master

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/ats_utilities/releases

To install this set of modules type the following:

.. code-block:: bash

    tar xvzf ats_utilities-x.y.z.tar.gz
    cd ats_utilities-x.y.z/
    pip install -r requirements.txt
    python setup.py install_lib
    python setup.py install_egg_info

You can use Docker to create image/container.

|GitHub docker checker|

.. |GitHub docker checker| image:: https://github.com/vroncevic/ats_utilities/workflows/ats_utilities%20docker%20checker/badge.svg
   :target: https://github.com/vroncevic/ats_utilities/actions?query=workflow%3A%22ats_utilities+docker+checker%22

Dependencies
-------------

**ats_utilities** requires next modules and libraries:

* `yaml - YAML parser and emitter for Python <https://pypi.org/project/PyYAML/>`_
* `bs4 - Screen-scraping library <https://pypi.org/project/beautifulsoup4/>`_
* `configparser - Configuration parser library <https://pypi.org/project/configparser/>`_
* `colorama - Cross-platform colored terminal text <https://pypi.org/project/colorama/>`_
* `pathlib - Object-oriented filesystem paths <https://pypi.org/project/pathlib/>`_

Library structure
------------------

**ats_utilities** is based on OOP:

.. image:: https://raw.githubusercontent.com/vroncevic/ats_utilities/dev/docs/arch_flow_usage.png

Code structure:

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
    ├── exceptions/
    │   ├── ats_attribute_error.py
    │   ├── ats_bad_call_error.py
    │   ├── ats_file_error.py
    │   ├── ats_key_error.py
    │   ├── ats_lookup_error.py
    │   ├── ats_type_error.py
    │   ├── ats_value_error.py
    │   └── __init__.py
    ├── info/
    │   ├── ats_build_date.py
    │   ├── ats_info_ok.py
    │   ├── ats_license.py
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
    └── register/
        └── __init__.py

Copyright and licence
----------------------

|License: GPL v3| |License: Apache 2.0|

.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |License: Apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2017 by `vroncevic.github.io/ats_utilities <https://vroncevic.github.io/ats_utilities>`_

**ats_utilities** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|Python Software Foundation|

.. |Python Software Foundation| image:: https://raw.githubusercontent.com/vroncevic/ats_utilities/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|Donate|

.. |Donate| image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
   :target: https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
