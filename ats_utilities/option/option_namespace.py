# -*- coding: UTF-8 -*-

'''
Module
    option_namespace.py
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
    Defines abstract class IATSOptionParser with attribute(s) and method(s).
    Creates an interfaces for ATS option parsing.
'''

from typing import Any, Dict, List, Tuple, Optional, Sequence, TypeAlias, Protocol

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class OptionNamespace(Protocol):
    '''
        Defines class OptionNamespace with attribute(s) and method(s).
        Creates protocol representing a Namespace-like result from an option parser.

        Implementations only need to provide a `__dict__` mapping (e.g. argparse.Namespace,
        types.SimpleNamespace, or a custom object) so callers can access attributes
        and call `vars()` to obtain a dict.

        It defines:
            :attributes:
                | __dict__ - A dictionary mapping attribute names to their values.
            :methods: None
    '''

    __dict__: Dict[str, Any]

# Type alias for optional sequence of strings representing command-line arguments
OptArgs: TypeAlias = Optional[Sequence[str]]

# Type alias for tuple containing an option namespace and a list of unknown arguments
KnownArgs: TypeAlias = Tuple[OptionNamespace, List[str]]
