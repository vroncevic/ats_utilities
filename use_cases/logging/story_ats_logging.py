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

from typing import List
from loguru import logger as loguru_native
from ats_utilities.logging.logger import ATSLogger, LogLevels

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

#
# default logging [logging]
# ==========================
#
logger_default: ATSLogger = ATSLogger()
logger_default.write_log("debug test", LogLevels.ATS_LOG_DEBUG)
logger_default.write_log("info test", LogLevels.ATS_LOG_INFO)
logger_default.write_log("warning test", LogLevels.ATS_LOG_WARNING)
logger_default.write_log("error test", LogLevels.ATS_LOG_ERROR)
logger_default.write_log("critical test", LogLevels.ATS_LOG_CRITICAL)

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
        # Loguru je već konfigurisan na nivou korisničke aplikacije
        self._map = {
            LogLevels.ATS_LOG_DEBUG: loguru_native.debug,
            LogLevels.ATS_LOG_INFO: loguru_native.info,
            LogLevels.ATS_LOG_WARNING: loguru_native.warning,
            LogLevels.ATS_LOG_ERROR: loguru_native.error,
            LogLevels.ATS_LOG_CRITICAL: loguru_native.critical,
        }

    def write_log(self, message: str | None, ctrl: int, verbose: bool = False) -> bool:
        log_func = self._map.get(ctrl)
        if log_func and message:
            log_func(message)
            return True
        return False

custom_logger = LoguruATSAdapter()
logger_custome: ATSLogger = ATSLogger(logger_instance=custom_logger)
logger_custome.write_log("debug test", LogLevels.ATS_LOG_DEBUG)
logger_custome.write_log("info test", LogLevels.ATS_LOG_INFO)
logger_custome.write_log("warning test", LogLevels.ATS_LOG_WARNING)
logger_custome.write_log("error test", LogLevels.ATS_LOG_ERROR)
logger_custome.write_log("critical test", LogLevels.ATS_LOG_CRITICAL)
