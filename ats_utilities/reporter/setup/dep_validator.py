# -*- coding: UTF-8 -*-

'''
Module
    dep_validator.py
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
    Validator for reporter dependencies.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.reporter.setup.dependencies import ReporterDependencies
from ats_utilities.reporter.setup.keys import ReporterKeys
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class ReporterDependenciesValidator:
    '''
        Validator for reporter dependencies.

        It defines:

            :methods:
                | validate - Validates reporter dependencies instance.
    '''

    @classmethod
    def validate(cls, dependencies: ReporterDependencies) -> None:
        '''
            Validates reporter dependencies instance.

            :param dependencies: Reporter dependencies instance to be validated.
            :exceptions:
                | ATSValueError: Dependencies must be provided and have proper values.
                | ATSTypeError:  Dependencies must be an instance of Mapping and its attributes
                |                must be instances of their respective types.
        '''
        ctx: str = 'reporter_dependencies_validator::validate(...)'

        not_none(dependencies, ctx, 'dependencies must be provided')
        istype(dependencies, Mapping, ctx, 'dependencies must be a Mapping')

        for attr_name, expected_type in ReporterKeys.get_dependency_to_type().items():
            value = dependencies.get(attr_name)

            if value is not None:
                err_msg = f'{attr_name.replace("_", " ")} must be an instance of {expected_type.__name__}'
                istype(value, expected_type, ctx, err_msg)
