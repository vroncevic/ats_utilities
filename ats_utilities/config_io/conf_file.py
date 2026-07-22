# -*- coding: UTF-8 -*-

'''
Module
    conf_file.py
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
    Defines class ConfFile with attribute(s) and method(s).
    Creates an API for configuration file context manager.
    0th level of configuration loader/storer implementation.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, override

from ats_utilities.config_io.iconf_file import IConfFile
from ats_utilities.config_io.conf_file_bundle import ConfFileBundle
from ats_utilities.config_io.iconf_file import File
from ats_utilities.reporter.proxy_reporter import vreport
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.utils.reflection import to_str
from ats_utilities.utils.files import check_file_exists
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ConfFile(IConfFile):
    '''
        Defines class ConfFile with attribute(s) and method(s).
        Creates an API for configuration file context manager.
        0th level of configuration loader/storer implementation.

        It defines:

            :attributes:
                | _file - File instance (default None).
                | _file_path - Configuration file path.
                | _file_mode - Configuration file mode.
            :methods:
                | __init__ - Initializes ConfFile constructor.
                | __enter__ - Opens configuration file in mode.
                | __exit__ - Closes configuration file.
                | __str__ - Returns the ConfFile as string representation.
    '''

    _file: File | None
    _file_path: str
    _file_mode: str
    _context: ContextBundle

    def __init__(self, file_bundle: ConfFileBundle) -> None:
        '''
            Initializes ConfFile constructor.

            :param file_bundle: File configuration bundle.
            :type file_bundle: <ConfFileBundle>
            :exceptions:
                | ATSValueErro: File bundle must be provided.
                | ATSValueError: Context bundle must be provided.
                | ATSTypeError: File bundle must be an instance of ConfFileBundle.
                | ATSTypeError: Context bundle must be an instance of ContextBundle.
        '''
        context: str = r'conf_file::init(...)'
        not_none(file_bundle, context, r'file bundle must be provided')
        istype(file_bundle, ConfFileBundle, context, r'file bundle must be an instance of ConfFileBundle')
        self._context = file_bundle.context_bundle
        self._file = None
        self._file_path = file_bundle.file_path
        self._file_mode = file_bundle.file_mode

    @vreport('open file {file_path} with mode {file_mode}')
    @override
    def __enter__(self) -> File:
        '''
            Opens configuration file in mode.

            :return: File IO object.
            :rtype: <File>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSValueError: File path must be provided.
                | ATSValueError: File does not exist (when opening in read mode).
                | ATSTypeError: File path and mode must be strings.
        '''
        context: str = r'conf_file::enter(...)'
        not_none(self._file_path, context, r'file path must be provided')
        not_none(self._file_mode, context, r'file mode must be provided')
        istype(self._file_path, str, context, r'file path must be a string')
        istype(self._file_mode, str, context, r'file mode must be a string')

        if 'r' in self._file_mode:
            check_file_exists(self._file_path, context, f'file {self._file_path} does not exist')

        self._file = open(self._file_path, self._file_mode, encoding='utf-8')

        return self._file

    @vreport('close file {file_path}')
    @override
    def __exit__(self, *args: tuple[Any, ...], **kwargs: Mapping[Any, Any]) -> None:
        '''
            Closes configuration file.

            :param args: List of arguments.
            :type args: <tuple[Any, ...]>
            :param kwargs: Dictionary of mapped arguments.
            :type kwargs: <Mapping[Any, Any]>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        try:
            if self._file is not None and hasattr(self._file, 'closed') and not self._file.closed:
                self._file.close()

        except Exception:
            pass
        finally:
            self._file = None

    @override
    def __str__(self) -> str:
        '''
            Returns the ConfFile as string representation.

            :return: The ConfFile as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
