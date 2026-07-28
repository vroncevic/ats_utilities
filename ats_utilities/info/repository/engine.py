# -*- coding: UTF-8 -*-

'''
Module
    engine.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class Repository with attribute(s) and method(s).
    Provides an API for the repository in one property object.
'''

from __future__ import annotations

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.validator import ContextValidator
from ats_utilities.utils.reflection import to_str
from ats_utilities.checker.proxy_validator import mcheck
from ats_utilities.reporter.proxy_reporter import vreport

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class Repository:
    '''
        Defines class Repository with attribute(s) and method(s).
        Provides an API for the repository in one property object.
        Note: Repository is only prepared when it is set by user (not None).

        It defines:

            :attributes:
                | _repository - The repository for App/Tool/Script (default None).
            :methods:
                | __init__ - Initializes Repository constructor.
                | repository - Property methods for set/get repository.
                | not_none - Checks is repository not None.
                | __str__ - Returns the repository as string representation.
    '''

    _repository: str | None
    _context: ContextBundle

    def __init__(self, context_bundle: ContextBundle) -> None:
        '''
            Initializes Repository constructor.

            :param context_bundle: Context bundle for repository.
            :exceptions:
                | ATSValueError:  Context bundle must be provided and have proper values.
                | ATSTypeError:   Context bundle must be an instance of ContextBundle
                |                 and its attributes must be instances of their
                |                 respective types.
        '''
        ContextValidator.validate(context_bundle)
        self._context = context_bundle
        self._repository = None

    @property
    @vreport('getting repository {repository}')
    def repository(self) -> str | None:
        '''
            Property method for getting repository.
            Note: Repository is only prepared when it is set by user (not None).

            :return: The repository in string format | None.
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._repository

    @repository.setter
    @mcheck([('str:repository', None)])
    @vreport('setting repository {repository}')
    def repository(self, repository: str) -> None:
        '''
            Property method for setting repository.
            Note: Repository is only prepared when it is set by user (not None).

            :param repository: The repository in string format.
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: Decorator used on a non-class method.
                | ATSAttributeError: Class does not provide a '_checker' object.
        '''
        self._repository = repository

    @vreport('checking repository {repository}')
    def not_none(self) -> bool:
        '''
            Checks is repository not None.
            Note: Repository is only prepared when it is set by user (not None).

            :return: True if successfully, otherwise False.
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._repository is not None

    def __str__(self) -> str:
        '''
            Returns the Repository as string representation.

            :return: The Repository as string representation.
            :exceptions: None.
        '''
        return to_str(self)
