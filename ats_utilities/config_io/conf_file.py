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
    Provides an API for configuration file context manager.
    0th level of configuration loader/storer implementation.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.config_io.data import FileData
from ats_utilities.config_io.data_validator import FileDataValidator
from ats_utilities.config_io.setup.types import File
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.exceptions import ATSValueError
from ats_utilities.reporter.proxy_reporter import vreport
from ats_utilities.utils.reflection import to_str
from ats_utilities.utils.files import check_file_exists
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class ConfFile:
    '''
        Defines class ConfFile with attribute(s) and method(s).
        Provides an API for configuration file context manager.
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
                | __str__ - Returns configuration context manager as string.
    '''

    _file: File | None
    _file_path: str
    _file_mode: str
    _context: ContextBundle

    def __init__(self, file_data: FileData) -> None:
        '''
            Initializes ConfFile constructor.

            :param file_data: File data.
            :exceptions:
                | ATSValueError: File data must be provided and have proper values.
                | ATSTypeError:  File data must be an instance of FileData and its
                |                attributes must be instances of their respective types.
        '''
        FileDataValidator.validate(file_data)
        self._context = file_data.context_bundle
        self._file = None
        self._file_path = file_data.file_path
        self._file_mode = file_data.file_mode

    @vreport('open file {file_path} with mode {file_mode}')
    def __enter__(self) -> File:
        '''
            Opens configuration file in mode.

            :return: File IO object.
            :exceptions:
                | ATSRuntimeError:   Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
                | ATSValueError:     File path must be provided.
                | ATSValueError:     File does not exist (when opening in read mode).
                | ATSTypeError:      File path and mode must be strings.
        '''
        ctx: str = 'conf_file::enter(...)'
        msg_file_path_none: str = 'file path must be provided'
        msg_file_mode_none: str = 'file mode must be provided'
        msg_file_path_istype: str = 'file path must be a string'
        msg_file_mode_istype: str = 'file mode must be a string'
        msg_file_path_not_exist: str = 'file path does not exist'

        not_none(self._file_path, ctx, msg_file_path_none)
        not_none(self._file_mode, ctx, msg_file_mode_none)
        istype(self._file_path, str, ctx, msg_file_path_istype)
        istype(self._file_mode, str, ctx, msg_file_mode_istype)

        try:
            if 'r' in self._file_mode:
                check_file_exists(self._file_path, ctx, msg_file_path_not_exist)

            self._file = open(self._file_path, self._file_mode, encoding='utf-8')

        except ATSValueError:
            self._file = None

        except Exception:
            self._file = None

        return self._file

    @vreport('close file {file_path}')
    def __exit__(self, *args: tuple[object, ...], **kwargs: Mapping[object, object]) -> None:
        '''
            Closes configuration file.

            :param args: List of arguments.
            :param kwargs: Dictionary of mapped arguments.
            :exceptions:
                | ATSRuntimeError:   Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @vreport decorator.
        '''
        try:
            if self._file is not None and not self._file.closed:
                self._file.close()

        except Exception:
            ...
        finally:
            self._file = None

    def __str__(self) -> str:
        '''
            Returns configuration context manager as string representation.

            :return: Configuration context manager as string representation.
            :exceptions: None.
        '''
        return to_str(self)
