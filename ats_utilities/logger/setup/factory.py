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
    Factory for creating the logger bundle.
'''

from __future__ import annotations

from sys import stdout
from logging import getLogger, basicConfig, INFO
from re import Pattern

from ats_utilities.logger.setup.bundle import LoggerBundle
from ats_utilities.logger.setup.registry import LoggerBundleRegistry
from ats_utilities.logger.setup.dependencies import LoggerBundleDependencies
from ats_utilities.logger.setup.options import LoggerBundleOptions
from ats_utilities.logger.setup.keys import LoggerBundleKeys
from ats_utilities.logger.setup.opt_validator import LoggerBundleOptionsValidator
from ats_utilities.logger.formatter.engine import LogFormatter
from ats_utilities.logger.buffer.engine import LogBuffer
from ats_utilities.logger.handler.engine import LogHandlerManager
from ats_utilities.logger.processor.engine import MessageProcessor
from ats_utilities.logger.underlying.engine import LoggerAdapter

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class LoggerBundleFactory:
    '''
        Factory for creating the logger bundle.

        It defines:

            :methods:
                | create_bundle - Creates the logger bundle with optional pre-configured options.
    '''

    @classmethod
    def create_bundle(cls, options: LoggerBundleOptions | None = None) -> LoggerBundle:
        '''
            Creates the logger bundle with optional pre-configured options.

            :param options: The pre-configured options for the bundle.
            :return: The logger bundle.
            :exceptions:
                | ATSValueError: The logger bundle options must be provided and have proper values.
                | ATSTypeError:  The logger bundle options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The logger bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The logger bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The logger bundle must be provided and have proper values.
                | ATSTypeError:  The logger bundle must be an instance of LoggerBundle and
                |                its attributes must be instances of their respective types.
        '''
        if options is not None:
            LoggerBundleOptionsValidator.validate(options)

        log_file: str | None = options.get(LoggerBundleKeys.OPTION_LOG_FILE) if options else None
        log_level: int = options.get(LoggerBundleKeys.OPTION_LOG_LEVEL) if options else INFO
        log_format: str = options.get(LoggerBundleKeys.OPTION_LOG_FORMAT) if options else '%(asctime)s - %(levelname)s - %(message)s'
        log_datefmt: str = options.get(LoggerBundleKeys.OPTION_LOG_DATEFMT) if options else '%m/%d/%Y %I:%M:%S %p'
        log_buffer_size: int = options.get(LoggerBundleKeys.OPTION_LOG_BUFFER_SIZE) if options else 200
        log_message_pattern: Pattern[str] | None = options.get(LoggerBundleKeys.OPTION_LOG_MESSAGE_PATTERN) if options else None

        logger = getLogger()

        if not logger.hasHandlers():
            log_config: dict[str, object] = {
                'format': log_format,
                'datefmt': log_datefmt,
                'level': log_level
            }

            if log_file:
                log_config['filename'] = log_file
            else:
                log_config['stream'] = stdout

            basicConfig(**log_config)

        formatter: LogFormatter = LogFormatter(log_format=log_format, log_datefmt=log_datefmt)
        underlying_logger: LoggerAdapter = LoggerAdapter(logger=logger, formatter=formatter)
        buffer: LogBuffer = LogBuffer(limit=log_buffer_size)
        handler_manager: LogHandlerManager = LogHandlerManager(logger=underlying_logger)
        message_processor: MessageProcessor = MessageProcessor(pattern=log_message_pattern)

        return LoggerBundleRegistry.create_bundle(
            dependencies=LoggerBundleDependencies(
                logger=underlying_logger,
                has_file_handler=log_file is not None,
                formatter=formatter,
                buffer=buffer,
                handler_manager=handler_manager,
                message_processor=message_processor
            )
        )
