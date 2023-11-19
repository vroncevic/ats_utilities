# -*- coding: UTF-8 -*-

'''
 Module
     object2yaml.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
     ats_utilities is free software: you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     ats_utilities is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Defined class Object2Yaml with attribute(s) and method(s).
     Created API for writing a configuration/information to a yaml file.
'''

import sys

try:
    from six import add_metaclass
    from yaml import dump
    from ats_utilities import VerboseRoot
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io import ConfigFile
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.base_write import BaseWriteConfig
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.6.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@add_metaclass(VerboseRoot)
class Object2Yaml(BaseWriteConfig):
    '''
        Defined class Object2Yaml with attribute(s) and method(s).
        Created API for writing a configuration/information to a yaml file.
        It defines:

            :attributes:
                | __FORMAT - format of configuration content.
                | __verbose - enable/disable verbose option.
            :methods:
                | __init__ - initial constructor.
                | write_configuration - write configuration to a yaml file.
                | __str__ - str dunder method for object Object2Yaml.
    '''

    __FORMAT = 'yaml'

    def __init__(self, configuration_file, verbose=False):
        '''
            Initial constructor.

            :param configuration_file: configuration file path.
            :type configuration_file: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:configuration_file', configuration_file)
        ])
        if status == ATSChecker.type_error:
            raise ATSTypeError(error)
        if status == ATSChecker.value_error:
            raise ATSBadCallError(error)
        BaseWriteConfig.__init__(self, verbose=verbose)
        self.__verbose = verbose
        self.file_path = configuration_file
        verbose_message(Object2Yaml.verbose, verbose, configuration_file)

    def write_configuration(self, configuration, verbose=False):
        '''
            Write configuration to a yaml file.

            :param configuration: configuration object | None.
            :type configuration: <Python object(s)> | <NoneType>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exception: None
        '''
        status = False
        verbose_message(Object2Yaml.verbose, verbose, configuration)
        if configuration is None:
            return status
        with ConfigFile(self.file_path, 'w', Object2Yaml.__FORMAT) as yaml:
            if bool(yaml):
                dump(configuration, yaml, default_flow_style=False)
                status = True
        return status

    def __str__(self):
        '''
            Dunder str method for Object2Yaml.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, BaseWriteConfig.__str__(self),
            str(self.__verbose)
        )
