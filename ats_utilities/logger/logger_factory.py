# -*- coding: UTF-8 -*-

'''
Module
    logger_factory.py
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
    Factory for creating Logger components.
'''

from __future__ import annotations

from sys import stdout
from logging import Logger, getLogger, basicConfig, INFO
from typing import Any

from ats_utilities.logger.logger_bundle import LoggerBundle

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class LoggerFactory:
    '''
        Factory for creating Logger components.
    '''

    @classmethod
    def create_default_logger_bundle(
        cls,
        log_file: str | None = None,
        log_level: int = INFO
    ) -> LoggerBundle:
        '''
            Creates a default LoggerBundle with pre-configured components.

            :param log_file: Path to the log file (default None).
            :type log_file: <str | None>
            :param log_level: Log level (default 20 - INFO).
            :type log_level: <int>
            :return: Default LoggerBundle instance.
            :rtype: <LoggerBundle>
            :exceptions: None.
        '''
        if not getLogger().hasHandlers():
            log_config: dict[str, Any] = {
                'format': '%(asctime)s - %(levelname)s - %(message)s',
                'datefmt': '%m/%d/%Y %I:%M:%S %p',
                'level': log_level
            }

            if log_file:
                log_config['filename'] = log_file
            else:
                log_config['stream'] = stdout

            basicConfig(**log_config)

        logger: Logger = getLogger()

        return LoggerBundle(
            logger=logger,
            log_file=log_file or '',
            log_level=log_level
        )
