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

🚀 Installation
----------------

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

📦 Dependencies
----------------

**ats_utilities** requires next modules and libraries

* `yaml - YAML parser and emitter for Python <https://pypi.org/project/PyYAML/>`_

📁 Framework structure
-----------------------

**ats_utilities** is designed from the ground up around robust, object-oriented paradigms and industrial-grade design patterns. The codebase strictly adheres to SOLID principles and is partitioned into highly decoupled, modular packages.

Design Pillars

Object-Oriented Architecture (OOP): Employs strong encapsulation, strict interface segregation, and clear class hierarchies to model system components.

SOLID Compliance: Engineered to facilitate seamless framework extension without modification (Open/Closed) and to decouple operations via explicit interface abstractions (Dependency Inversion).

Domain-Driven Package Organization: Functionality is organized into dedicated sub-packages—such as registries, bundle dataclasses, engines, and validators—ensuring clear separation of concerns.

Framework structure

.. code-block:: bash

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

✨ Features
------------

* **Base Framework Architecture**: Standardized classes (``Base``, ``BaseFactory``, ``BaseOptions``) to quickly build robust command-line applications, scripts, and tools.
* **Robust Logging Engine**: Highly configurable logging module supporting log file outputs, buffers, custom formatters, message processors, and multiple severity levels.
* **Advanced Option Parsing**: Command-line option parser with modular design and strategy support (such as ``fire`` parsing or standard ``argparse`` processing).
* **Flexible Configuration I/O**: Config files loader and storer supporting formats like CFG, INI, JSON, XML, and YAML out of the box.
* **Themeable Console Reporter**: Enhanced feedback system that displays styled, colored, and verbose messages to the console with support for custom color themes.
* **Progressive Splash Screens**: Informative and visually appealing CLI splash screen implementation with customizable progress bars.
* **Type & Value Validation**: Built-in mechanisms to perform rigorous type checking and data validation on inputs and configs.
* **OOP and SOLID Design**: Decoupled, modular package design built around SOLID principles and clear interface segregation.

📊 Code coverage
-----------------

.. csv-table::
   :file: coverage_table.csv
   :header-rows: 1
   :widths: 60, 10, 10, 10

🛠 Usage
---------

Below is a basic example illustrating how to define and use a tool by subclassing the ``Base`` class, integrating logger and reporter modules:

.. code-block:: python

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

👥 Contributing
----------------

`Contributing to ats_utilities <https://github.com/vroncevic/ats_utilities/blob/dev/CONTRIBUTING.md>`_

📄 Copyright and licence
------------------------

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
