# -*- coding: UTF-8 -*-

'''
Module
    conf_file_factory.py
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
    Factory for creating ConfFile components.
'''

from __future__ import annotations

from ats_utilities.config_io.conf_file import ConfFile
from ats_utilities.config_io.conf_file_bundle import ConfFileBundle
from ats_utilities.config_io.iconf_file import IConfFile
from ats_utilities.context.bundle import ContextBundle

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ConfFileFactory:
    '''
        Factory for creating ConfFile components.
    '''

    @classmethod
    def create_conf_file(
        cls,
        file_path: str,
        file_mode: str,
        context_bundle: ContextBundle
    ) -> IConfFile:
        '''
            Factory method to instantiate an IConfFile implementation.

            :param file_path: Config file path.
            :type file_path: <str>
            :param file_mode: Config file mode.
            :type file_mode: <str>
            :param context_bundle: Context bundle for dependency injection.
            :type context_bundle: <ContextBundle>
            :return: IConfFile implementation.
            :rtype: <IConfFile>
            :exceptions: None.
        '''
        bundle = ConfFileBundle(
            file_path=file_path,
            file_mode=file_mode,
            context_bundle=context_bundle
        )
        return ConfFile(bundle)
