# -*- coding: UTF-8 -*-

'''
Module
    template_dir.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    ats_utilities is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    ats_utilities is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines class TemplateDir with attribute(s) and method(s).
    Defines project template directory container.
'''

from typing import List, Optional
from ats_utilities.config_setup.itemplate_dir import ITemplateDir
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import format_instance_to_string
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.reporter.proxy_reporter import vreporter

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class TemplateDir(ITemplateDir):
    '''
        Defines class TemplateDir with attribute(s) and method(s).
        Defines project template directory container.
        Mechanism for project configuration.

        It defines:

            :attributes:
                | __checker - Factoriezed parameters checker (default ATSChecker).
                | __reporter - Factoriezed reporter for messaging (default ATSReporter).
                | __verbose - Factoriezed Enable/Disable verbose option (default False).
                | __template_dir - Project template dir path (default None).
            :methods:
                | __init__ - Initials TemplateDir constructor.
                | template_dir - Property methods for set/get operations.
                | not_none - Checks template dir is not None.
                | __str__ - Returns the string representation of ATS project template directory.
    '''

    def __init__(self, pro_config_bundle: Optional[ContextBundle] = None) -> None:
        '''
            Initials TemplateDir constructor.

            :param pro_config_bundle: Bundle with checker, reporter and verbose | None
            :type pro_config_bundle: <Optional[ContextBundle]>
            :exceptions: None
        '''
        factory_context_bundle(self, pro_config_bundle)
        self.__template_dir: Optional[str] = None

    @property
    @vreporter('get template dir {template_dir}')
    def template_dir(self) -> Optional[str]:
        '''
            Property method for getting template dir.

            :return: Formatted template dir in string format | None
            :rtype: <Optional[str]>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        return self.__template_dir

    @template_dir.setter
    @validator([('Optional[str]:dir_path', None)])
    @vreporter('get template dir {template_dir}')
    def template_dir(self, dir_path: Optional[str]) -> None:
        '''
            Property method for setting project template dir.

            :param dir_path: Project template dir path in string format | None
            :type dir_path: <Optional[str]>
            :exceptions:
                | ATSTypeError, ATSValueError by validator
                | RuntimeError, AttributeError by vreporter
        '''
        self.__template_dir = dir_path

    @vreporter('check template dir {template_dir}')
    def not_none(self) -> bool:
        '''
            Checks project template dir is not None.

            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: RuntimeError, AttributeError by vreporter
        '''
        return self.__template_dir is not None

    def __str__(self) -> str:
        '''
            Returns the string representation of ATS project template directory.

            :return: The ATS project directory as string representation
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
