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
from logging import getLogger, basicConfig, INFO
from typing import Any

from ats_utilities.logger.setup.bundle import LoggerBundle
from ats_utilities.logger.setup.registry import LoggerRegistry
from ats_utilities.logger.setup.dependencies import LoggerDependencies
from ats_utilities.logger.setup.options import LoggerOptions
from ats_utilities.logger.setup.keys import LoggerKeys
from ats_utilities.logger.setup.opt_validator import LoggerOptionsValidator
from ats_utilities.logger.formatter.engine import LogFormatter
from ats_utilities.logger.buffer.engine import LogBuffer
from ats_utilities.logger.handler.engine import LogHandlerManager

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class LoggerFactory:
    '''
        Factory for creating logger bundle instance.

        It defines:

            :methods:
                | create_bundle - Creates a logger bundle with optional pre-configured options.
    '''

    @classmethod
    def create_bundle(cls, options: LoggerOptions | None = None) -> LoggerBundle:
        '''
            Creates a logger bundle with optional pre-configured options.

            :param options: Pre-configured options for the bundle.
            :return: Logger bundle instance.
            :exceptions:
                | ATSValueError: Options must be provided and have proper values.
                | ATSTypeError:  Options must be an instance of LoggerOptions
                |                and its attributes must be instances of their
                |                respective types.
        '''
        if options is not None:
            LoggerOptionsValidator.validate(options)

        log_file: str | None = None
        log_level: int = INFO
        log_format: str = '%(asctime)s - %(levelname)s - %(message)s'
        log_datefmt: str = '%m/%d/%Y %I:%M:%S %p'
        log_buffer_size: int = 200

        if options:
            log_file = options.get(LoggerKeys.OPTION_LOG_FILE)
            log_level = options.get(LoggerKeys.OPTION_LOG_LEVEL, INFO)
            log_format = options.get(LoggerKeys.OPTION_LOG_FORMAT, log_format)
            log_datefmt = options.get(LoggerKeys.OPTION_LOG_DATEFMT, log_datefmt)
            log_buffer_size = options.get(LoggerKeys.OPTION_LOG_BUFFER_SIZE, log_buffer_size)

        logger = getLogger()

        if not logger.hasHandlers():
            log_config: dict[str, Any] = {
                'format': log_format,
                'datefmt': log_datefmt,
                'level': log_level
            }

            if log_file:
                log_config['filename'] = log_file
            else:
                log_config['stream'] = stdout

            basicConfig(**log_config)

        formatter: LogFormatter = LogFormatter()
        buffer: LogBuffer = LogBuffer(limit=log_buffer_size)
        handler_manager: LogHandlerManager = LogHandlerManager(logger)

        return LoggerRegistry.create_bundle(
            dependencies=LoggerDependencies(
                logger=logger,
                has_file_handler=log_file is not None,
                formatter=formatter,
                buffer=buffer,
                handler_manager=handler_manager
            )
        )
