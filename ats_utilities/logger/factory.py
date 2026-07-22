# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Factory for creating logger bundle instance.
'''

from __future__ import annotations

from sys import stdout
from logging import Logger, getLogger, basicConfig, INFO
from typing import override, Any

from ats_utilities.utils.ifactory import IFactory
from ats_utilities.logger.bundle import LoggerBundle
from ats_utilities.logger.dependencies import LoggerOptions
from ats_utilities.logger.validator import LoggerValidator

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class LoggerFactory(IFactory[LoggerBundle, LoggerOptions | None]):
    '''
        Factory for creating logger bundle instance.

        It defines:

            :methods:
                | create_default_bundle - Creates a default logger bundle with pre-configured options.
    '''

    @classmethod
    @override
    def create_default_bundle(cls, options: LoggerOptions | None = None) -> LoggerBundle:
        '''
            Creates a default logger bundle with pre-configured options.

            :param options: Pre-configured options for the bundle (default None).
            :type options: LoggerOptions | None
            :return: Default logger bundle instance.
            :rtype: LoggerBundle
            :exceptions:
                | ATSValueError: Bundle must be provided.
                | ATSValueError: Logger must be provided.
                | ATSValueError: Log file must be provided.
                | ATSValueError: Log level must be provided.
                | ATSTypeError: Bundle must be an instance of LoggerBundle.
                | ATSTypeError: Log file must be a str instance.
                | ATSTypeError: Log level must be an int instance.
                | ATSTypeError: Logger must be an ILogger or standard logging.Logger instance.
        '''
        log_file: str | None = None
        log_level: int = INFO

        if options:
            log_file = options.get('log_file')
            log_level = options.get('log_level', INFO)

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

        bundle: LoggerBundle = LoggerBundle(
            logger=logger,
            log_file=log_file or '',
            log_level=log_level
        )

        LoggerValidator.validate(bundle)

        return bundle
