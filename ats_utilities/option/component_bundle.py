# -*- coding: UTF-8 -*-

'''
Module
    component_bundle.py
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
    Defines component bundle data classe for dependency group simplification.
    Encapsulates option components to minimize constructor overhead.
'''

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, asdict
from typing import Any

from ats_utilities.context_bundle import ContextBundle
from ats_utilities.option.strategy.iparser_strategy import IParserStrategy
from ats_utilities.option.strategy.parser_strategy import ParserStrategy
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.factory_value import require_not_none
from ats_utilities.factory_type import check_type

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


@dataclass(slots=True, kw_only=True)
class OptionComponentBundle:
    '''
        Defines component bundle data classe for dependency group simplification.
        Encapsulates option components to minimize constructor overhead.

        It defines:

            :attributes:
                | parameters - Configuration parameters (default None).
                | strategy - Strategy for argument parsing (default None).
                | context_bundle - Context bundle for dependency injection (default None).
            :methods:
                | validate - Validates that OptionComponentBundle instance is valid.
                | merge - Merges non-None values from another OptionComponentBundle instance into this one.
                | to_dict - Converts the OptionComponentBundle instance to a dictionary.
    '''

    parameters: Mapping[str, str] | None = None
    strategy: IParserStrategy | None = None
    context_bundle: ContextBundle | None = None

    def __post_init__(self) -> None:
        '''
            Post-initialization hook to set up default strategy.

            :exceptions:
                | ATSTypeError: Strategy must be an IParserStrategy instance.
        '''
        if self.context_bundle is None:
            self.context_bundle = ContextBundle()

        self.strategy = make_component(
            self.strategy, ParserStrategy, {'context_bundle': self.context_bundle}
        )
        validate_component(self.strategy, IParserStrategy, r'strategy must be an IParserStrategy instance')

    def validate(self) -> None:
        '''
            Validates that OptionComponentBundle is valid (can be called after merge).
            Performs validation of parameters, strategy and context_bundle attributes.
            Parameters must be non-None and an instance of Mapping[str, str] interface.
            Strategy must be non-None and an instance of IParserStrategy interface.
            Context bundle must be non-None and an instance.

            :exceptions:
                | ATSValueError: Parameters must be provided.
                | ATSValueError: Strategy must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: Parameters must be a Mapping[str, str] instance.
                | ATSTypeError: Strategy must be an IParserStrategy instance.
                | ATSTypeError: Context bundle must be a ContextBundle instance.
        '''
        require_not_none(self.parameters, r'parameters must be provided')
        require_not_none(self.strategy, r'strategy must be provided')
        require_not_none(self.context_bundle, r'context bundle must be provided')
        check_type(self.parameters, Mapping[str, str], r'parameters must be a Mapping[str, str] instance')
        check_type(self.strategy, IParserStrategy, r'strategy must be an IParserStrategy instance')
        check_type(self.context_bundle, ContextBundle, r'context bundle must be a ContextBundle instance')

    def merge(self, other: OptionComponentBundle) -> None:
        '''
            Merges non-None values from another OptionComponentBundle instance into this one.

            :param other: Another OptionComponentBundle instance to merge into this one.
            :type other: <OptionComponentBundle>
            :exceptions:
                | ATSTypeError: Other must be a OptionComponentBundle instance.
        '''
        check_type(other, OptionComponentBundle, r'other must be a OptionComponentBundle instance')

        for field_name in self.__dataclass_fields__:
            other_value: Any = getattr(other, field_name)

            if other_value is not None:
                setattr(self, field_name, other_value)

        self.validate()

    def to_dict(self) -> dict[str, Any]:
        '''
            Converts the bundle OptionComponentBundle instance to a dictionary.

            :return: Dictionary representation of the OptionComponentBundle instance.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return asdict(self)
