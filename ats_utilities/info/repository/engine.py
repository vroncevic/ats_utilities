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
    Defines the Repository class with attribute(s) and method(s).
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
        Defines the Repository class with attribute(s) and method(s).
        Provides an API for the repository in one property object.
        Note: The repository is only prepared when it is set by the user (not None).

        It defines:

            :attributes:
                | _repository - The repository for the App/Tool/Script (default: None).
            :methods:
                | __init__ - Initializes the Repository.
                | repository - Property methods for setting and getting the repository.
                | not_none - Checks if the repository is not None.
                | __str__ - Returns the repository as a string representation.
    '''

    _repository: str | None
    _context: ContextBundle

    def __init__(self, context_bundle: ContextBundle) -> None:
        '''
            Initializes the Repository.

            :param context_bundle: The context bundle for repository.
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
            Property method for getting the repository.
            Note: The repository is only prepared when it is set by the user (not None).

            :return: The repository in string format | None.
            :exceptions:
                | ATSRuntimeError: The decorator cannot be used on a standalone function.
                | ATSAttributeError: The class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._repository

    @repository.setter
    @mcheck([('str:repository', None)])
    @vreport('setting repository {repository}')
    def repository(self, repository: str) -> None:
        '''
            Property method for setting the repository.
            Note: The repository is only prepared when it is set by the user (not None).

            :param repository: The repository in string format.
            :exceptions:
                | ATSRuntimeError: The decorator cannot be used on a standalone function.
                | ATSAttributeError: The class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSTypeError: Parameter type validation failed.
                | ATSValueError: Parameter format validation failed.
                | ATSRuntimeError: The decorator is used on a non-class method.
                | ATSAttributeError: The class does not provide a '_checker' object.
        '''
        self._repository = repository

    @vreport('checking repository {repository}')
    def not_none(self) -> bool:
        '''
            Checks if the repository is not None.
            Note: The repository is only prepared when it is set by the user (not None).

            :return: True if successful, otherwise False.
            :exceptions:
                | ATSRuntimeError: The decorator cannot be used on a standalone function.
                | ATSAttributeError: The class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        return self._repository is not None

    def __str__(self) -> str:
        '''
            Returns the Repository as a string representation.

            :return: The Repository as a string representation.
            :exceptions: None.
        '''
        return to_str(self)
