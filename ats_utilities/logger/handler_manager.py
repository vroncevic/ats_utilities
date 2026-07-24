# -*- coding: UTF-8 -*-

'''
Module
    handler_manager.py
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
    Manager for logger output handlers.
'''

from __future__ import annotations

from logging import FileHandler, Formatter, StreamHandler
from os import makedirs
from os.path import dirname, exists
from sys import stdout, stderr
from typing import Any, override

from ats_utilities.logger.ihandler_manager import ILogHandlerManager

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.4'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class LogHandlerManager(ILogHandlerManager):
    '''
        Manager for logger output handlers.

        It defines:

            :methods:
                | set_log_file - Configures file output handler.
                | set_stdout - Configures stdout stream handler.
                | set_stderr - Configures stderr stream handler.
    '''

    def __init__(self, logger: Any) -> None:
        self._logger = logger

    @override
    def set_log_file(self, log_file: str) -> bool:
        '''
            Configures file output handler.

            :param log_file: Log file path.
            :type log_file: str
            :return: True if configured successfully, otherwise False.
            :rtype: bool
        '''
        if hasattr(self._logger, 'set_log_file'):
            self._logger.set_log_file(log_file)
            return True
        elif hasattr(self._logger, 'addHandler'):
            log_dir = dirname(log_file)

            if log_dir and not exists(log_dir):
                makedirs(log_dir, exist_ok=True)

            for handler in list(self._logger.handlers):
                if isinstance(handler, FileHandler):
                    self._logger.removeHandler(handler)

            file_handler = FileHandler(log_file)
            file_handler.setFormatter(Formatter(
                '%(asctime)s - %(levelname)s - %(message)s',
                datefmt='%m/%d/%Y %I:%M:%S %p'
            ))
            self._logger.addHandler(file_handler)
            return True

        return False

    @override
    def set_stdout(self) -> bool:
        '''
            Configures stdout stream handler.

            :return: True if configured successfully, otherwise False.
            :rtype: bool
        '''
        if hasattr(self._logger, 'set_stdout'):
            self._logger.set_stdout()
            return True
        elif hasattr(self._logger, 'addHandler'):
            for handler in list(self._logger.handlers):
                if isinstance(handler, FileHandler):
                    self._logger.removeHandler(handler)
                elif isinstance(handler, StreamHandler) and getattr(handler, 'stream', None) is not stdout:
                    self._logger.removeHandler(handler)

            has_stdout = any(
                isinstance(h, StreamHandler) and getattr(h, 'stream', None) is stdout
                for h in self._logger.handlers
            )

            if not has_stdout:
                stream_handler = StreamHandler(stdout)
                stream_handler.setFormatter(Formatter(
                    '%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p'
                ))
                self._logger.addHandler(stream_handler)
            return True

        return False

    @override
    def set_stderr(self) -> bool:
        '''
            Configures stderr stream handler.

            :return: True if configured successfully, otherwise False.
            :rtype: bool
        '''
        if hasattr(self._logger, 'set_stderr'):
            self._logger.set_stderr()
            return True
        elif hasattr(self._logger, 'addHandler'):
            for handler in list(self._logger.handlers):
                if isinstance(handler, FileHandler):
                    self._logger.removeHandler(handler)
                elif isinstance(handler, StreamHandler) and getattr(handler, 'stream', None) is not stderr:
                    self._logger.removeHandler(handler)

            has_stderr = any(
                isinstance(h, StreamHandler) and getattr(h, 'stream', None) is stderr
                for h in self._logger.handlers
            )

            if not has_stderr:
                stream_handler = StreamHandler(stderr)
                stream_handler.setFormatter(Formatter(
                    '%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p'
                ))
                self._logger.addHandler(stream_handler)
            return True

        return False
