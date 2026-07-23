# -*- coding: utf-8 -*-

'''
Module
    story_context_bundle.py
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
    Use cases for ATS context bundle.
'''

from dataclasses import FrozenInstanceError

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.factory import ContextFactory

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'

#
# default [without DI]
# ======================
#
ats_context_bundle: ContextBundle = ContextFactory.create_default_bundle()
print(ats_context_bundle)
print(ats_context_bundle.checker)
print(ats_context_bundle.reporter)
print(ats_context_bundle.verbose)
print(100 * '=')

#
# Anti-pattern - modification of immutable instance
#
try:
    object.__setattr__(ats_context_bundle, 'checker', None)
    object.__setattr__(ats_context_bundle, 'reporter', None)
    object.__setattr__(ats_context_bundle, 'verbose', 2)
except (AttributeError, FrozenInstanceError) as exc:
    print(f'{exc}')

print(ats_context_bundle)
print(ats_context_bundle.checker)
print(ats_context_bundle.reporter)
print(ats_context_bundle.verbose)
print(100 * '=')


#
# Protection using descriptors
# =============================
#

from typing import Any

from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.utils.reflection import instance_to_dict


class ReadOnlyAttribute:
    '''Descriptor that completely blocks any attribute modification.'''

    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, instance: Any, owner: Any = None) -> Any:
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance: Any, value: Any) -> None:
        ctx: str = r'context_bundle::__setattr__(...)'
        raise ATSValueError(f'{ctx} cannot modify immutable attribute: {self.name}')


class ContextBundle:
    '''
    Immutable ContextBundle where even object.__setattr__ fails.
    '''

    checker = ReadOnlyAttribute('checker')
    logger = ReadOnlyAttribute('logger')
    reporter = ReadOnlyAttribute('reporter')
    verbose = ReadOnlyAttribute('verbose')

    def __init__(
        self,
        *,
        checker: IChecker,
        logger: ILogger,
        reporter: IReporter,
        verbose: bool
    ) -> None:
        self.__dict__['checker'] = checker
        self.__dict__['logger'] = logger
        self.__dict__['reporter'] = reporter
        self.__dict__['verbose'] = verbose

    def to_dict(self) -> dict[str, Any]:
        return instance_to_dict(self)


#
# Protection using metaclass
# ==========================
#

from typing import Any
from dataclasses import dataclass
from ats_utilities.exceptions.ats_value_error import ATSValueError


class ImmutableMeta(type):
    '''Metaclass that enforces strict immutability.'''

    def __setattr__(cls, name: str, value: Any) -> None:
        ctx: str = r'context_bundle::__setattr__(...)'
        raise ATSValueError(f'{ctx} cannot modify immutable attribute: {name}')


@dataclass(slots=True, kw_only=True)
class ContextBundle(metaclass=ImmutableMeta):
    checker: IChecker
    logger: ILogger
    reporter: IReporter
    verbose: bool

    def __setattr__(self, name: str, value: Any) -> None:
        ctx: str = r'context_validator::__setattr__(...)'
        raise ATSValueError(f'{ctx} cannot modify immutable attribute: {name}')


#
# Protection using slots and __slots__
# ====================================
#

from typing import Any
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.exceptions.ats_value_error import ATSValueError


class ContextBundle:
    __slots__ = ('_checker', '_logger', '_reporter', '_verbose')

    def __init__(
        self,
        *,
        checker: IChecker,
        logger: ILogger,
        reporter: IReporter,
        verbose: bool
    ) -> None:
        object.__setattr__(self, '_checker', checker)
        object.__setattr__(self, '_logger', logger)
        object.__setattr__(self, '_reporter', reporter)
        object.__setattr__(self, '_verbose', verbose)

    @property
    def checker(self) -> IChecker:
        return self._checker

    @property
    def logger(self) -> ILogger:
        return self._logger

    @property
    def reporter(self) -> IReporter:
        return self._reporter

    @property
    def verbose(self) -> bool:
        return self._verbose

    def __setattr__(self, name: str, value: Any) -> None:
        ctx: str = r'context_bundle::__setattr__(...)'
        raise ATSValueError(f'{ctx} cannot modify immutable attribute: {name}')
