# -*- coding: utf-8 -*-

'''
Module
    story_ats_logging.py
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
    Use cases for ATS logging.
'''

from loguru import logger as loguru_native
from ats_utilities.logging.logger.ilogger import ILogger, LogLevels
from ats_utilities.logging.component_bundle import LoggingComponentBundle
from ats_utilities.logging.engine import LoggerManager

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'

#
# default logging [logging]
# ==========================
#
logger_default: LoggerManager = LoggerManager()
logger_default.write_log("debug test", LogLevels.DEBUG)
logger_default.write_log("info test", LogLevels.INFO)
logger_default.write_log("warning test", LogLevels.WARNING)
logger_default.write_log("error test", LogLevels.ERROR)
logger_default.write_log("critical test", LogLevels.CRITICAL)

#
# 3rd party [loguru]
# ===================
#


class LoguruATSAdapter(ILogger):
    '''
        ...
    '''
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self._map = {
            LogLevels.DEBUG: loguru_native.debug,
            LogLevels.INFO: loguru_native.info,
            LogLevels.WARNING: loguru_native.warning,
            LogLevels.ERROR: loguru_native.error,
            LogLevels.CRITICAL: loguru_native.critical,
        }

    def write_log(self, message: str, ctrl: int) -> bool:
        log_func = self._map.get(ctrl)
        if log_func and message:
            log_func(message)
            return True
        return False

    def is_initialized(self) -> bool:
        return True

    def __str__(self) -> str:
        return 'LoguruATSAdapter'

custom_logger = LoguruATSAdapter()
bundle: LoggingComponentBundle = LoggingComponentBundle(logger=custom_logger)
logger_custome: LoggerManager = LoggerManager(component_bundle=bundle)
logger_custome.write_log("debug test", LogLevels.DEBUG)
logger_custome.write_log("info test", LogLevels.INFO)
logger_custome.write_log("warning test", LogLevels.WARNING)
logger_custome.write_log("error test", LogLevels.ERROR)
logger_custome.write_log("critical test", LogLevels.CRITICAL)
