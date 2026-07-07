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

from __future__ import annotations

from typing import override

from ats_utilities.config_setup.itemplate_dir import ITemplateDir
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import to_str
from ats_utilities.checker.proxy_validator import vcheck
from ats_utilities.reporter.proxy_reporter import vreport

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


class TemplateDir(ITemplateDir):
    '''
        Defines class TemplateDir with attribute(s) and method(s).
        Defines project template directory container.
        Mechanism for project configuration.

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _template_dir - Project template dir path (default None).
            :methods:
                | __init__ - Initializes TemplateDir constructor.
                | template_dir - Property methods for set/get operations.
                | not_none - Checks template dir is not None.
                | __str__ - Returns the ATS project template directory as string representation.
    '''

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool
    _template_dir: str | None

    def __init__(self, context_bundle: ContextBundle | None = None) -> None:
        '''
            Initializes TemplateDir constructor.

            :param context_bundle: Context bundle for template dir | None.
            :type context_bundle: <ContextBundle | None>
            :exceptions: None.
        '''
        factory_context_bundle(self, context_bundle)
        self._template_dir = None

    @property
    @vreport('get template dir {template_dir}')
    @override
    def template_dir(self) -> str:
        '''
            Property method for getting template dir.

            :return: Formatted template dir in string format.
            :rtype: <str>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._template_dir

    @template_dir.setter
    @vcheck([('str:dir_path', None)])
    @vreport('get template dir {template_dir}')
    @override
    def template_dir(self, dir_path: str) -> None:
        '''
            Property method for setting project template dir.

            :param dir_path: Project template dir path in string format.
            :type dir_path: <str>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        self._template_dir = dir_path

    @vreport('check template dir {template_dir}')
    @override
    def not_none(self) -> bool:
        '''
            Checks project template dir is not None.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._template_dir is not None

    @override
    def __str__(self) -> str:
        '''
            Returns the ATS project template directory as string representation.

            :return: The ATS project template directory as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
