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
    Creates an API for the configuration context manager.
'''

from typing import Any, override
from ats_utilities.config_io.iconf_file import IConfFile
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.proxy_reporter import vreporter
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.config_io.iconf_file import File
from ats_utilities.config_io.file_bundle import ATSFileBundle
from ats_utilities.config_io.config_file_bundle import ATSConfigFileBundle
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.factory_class import format_instance_to_string

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ConfFile(IConfFile):
    '''
        Defines class ConfFile with attribute(s) and method(s).
        Creates an API for the configuration context manager.
        Configuration file context manager.

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _file_path - Configuration file path (default None).
                | _file_mode - Configuration file mode (default None).
                | _file - File object (default None).
                | _verbose - Enable/Disable verbose option (default False).
            :methods:
                | __init__ - Initializes ConfFile constructor.
                | __enter__ - Opens configuration file in mode.
                | __exit__ - Closes configuration file.
                | __str__ - Returns the ConfFile as string representation.
    '''

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    def __init__(
        self,
        file_bundle: ATSFileBundle | None = None,
        config_file_bundle: ATSConfigFileBundle | None = None
    ) -> None:
        '''
            Initializes ConfFile constructor.

            :param file_bundle: File bundle parameters | None.
            :type file_bundle: <ATSFileBundle | None>
            :param config_file_bundle: File configuration bundle parameters | None.
            :type config_file_bundle: <ATSConfigFileBundle | None>
            :exceptions:
                | ATSValueError: Missing file path.
                | ATSValueError: Missing file mode.
                | ATSValueError: Missing file format.
        '''
        bundle: ATSFileBundle = file_bundle or ATSFileBundle()
        config_bundle: ATSConfigFileBundle = config_file_bundle or ATSConfigFileBundle()
        factory_context_bundle(self, config_bundle.context)
        shared_bundle: ContextBundle = ContextBundle(
            checker=self._checker, reporter=self._reporter, verbose=self._verbose
        )
        file_checker: IFileCheck = make_component(config_bundle.file_checker, FileCheck, {'config_bundle': shared_bundle})
        validate_component(file_checker, FileCheck)

        if not bool(bundle.file_path):
            raise ATSValueError('missing file path')

        if not bool(bundle.file_mode):
            raise ATSValueError('missing file mode')

        if not bool(bundle.file_format):
            raise ATSValueError('missing file format')

        self._file: File | None = None
        self._file_path: str | None = None
        self._file_mode: str | None = None

        file_checker.check_path(bundle.file_path)
        file_checker.check_mode(bundle.file_mode)
        file_checker.check_format(bundle.file_path, bundle.file_format)

        if file_checker.is_file_ok():
            self._file_path = bundle.file_path
            self._file_mode = bundle.file_mode

    @vreporter('open file {file_path} with mode {file_mode}')
    @override
    def __enter__(self) -> File | None:
        '''
            Opens configuration file in mode.

            :return: File IO object | None.
            :rtype: <File>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @verboser decorator.
        '''
        if self._file_path and self._file_mode:
            self._file = open(self._file_path, self._file_mode, encoding='utf-8')

        return self._file

    @vreporter('close file {file_path}')
    @override
    def __exit__(self, *args: tuple[Any, ...], **kwargs: dict[Any, Any]) -> None:
        '''
            Closes configuration file.

            :param args: List of arguments.
            :type args: <tuple[Any, ...]>
            :param kwargs: Dictionary of mapped arguments.
            :type kwargs: <dict[Any, Any]>
            :exceptions:
                | ATSRuntimeError: Decorator cannot be used on a standalone function.
                | ATSAttributeError: Class is required to provide a '_reporter' object to
                |                    use the @verboser decorator.
        '''
        if self._file and not self._file.closed:
            self._file.close()

    @override
    def __str__(self) -> str:
        '''
            Returns the ConfFile as string representation.

            :return: The ConfFile as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
