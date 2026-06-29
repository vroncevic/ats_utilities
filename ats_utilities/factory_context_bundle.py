# -*- coding: UTF-8 -*-

'''
Module
    factory_context_bundle.py
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
    Factory universally injects components (checker, reporter, verbose).
    Encapsulates core utilities to minimize constructor overhead.
    Provides a simple factory mechanism for dependency injection.
'''

from typing import Any
from ats_utilities.factory_class import inject
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.engine import Checker
from ats_utilities.reporter.engine import Reporter
from ats_utilities.reporter.component_bundle import ReporterComponentBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


def factory_context_bundle(instance: Any, context: ContextBundle | None = None):
    '''
        Factory universally injects components (checker, reporter, verbose).

        :param instance: The object instance (self) to inject attributes into.
        :type instance: <Any>
        :param context: Context bundle of checker, reporter and verbose | None.
        :type context: <ContextBundle | None>
        :exceptions: None.
    '''
    # No dependency injection then use default ones.
    if not bool(context):
        context: ContextBundle = ContextBundle()

    if context.checker is None:
        context.checker: Checker = Checker()

    if context.reporter is None:
        reporter_bundle: ReporterComponentBundle = ReporterComponentBundle(checker=context.checker)
        context.reporter: Reporter = Reporter(component_bundle=reporter_bundle)

    inject(
        instance,
        ('checker', context.checker, Checker, None),
        ('reporter', context.reporter, Reporter, ['checker']),
        ('verbose', context.verbose, False, None)
    )
