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

from __future__ import annotations

from typing import Any

from ats_utilities.factory_class import inject
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.engine import Checker
from ats_utilities.reporter.engine import Reporter

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


def factory_context_bundle(instance: Any, context: ContextBundle | None = None):
    '''
        Factory universally injects components (checker, reporter, verbose).

        :param instance: The object instance (self) to inject attributes into.
        :type instance: <Any>
        :param context: Context bundle (checker, reporter and verbose) | None.
        :type context: <ContextBundle | None>
        :exceptions: None.
    '''
    # Uses provided bundle or creates a default one.
    ctx: ContextBundle = context or ContextBundle()

    inject(
        instance,
        ('checker', ctx.checker, Checker, None),
        ('reporter', ctx.reporter, Reporter, ['checker']),
        ('verbose', ctx.verbose, False, None)
    )
