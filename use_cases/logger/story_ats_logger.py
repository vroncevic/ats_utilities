# -*- coding: utf-8 -*-

'''
Module
    story_ats_logger.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
Info
    Use cases for ATS logger.
'''

from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
from loguru import logger as loguru_native
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.logger.logger_bundle import LoggerBundle
from ats_utilities.logger.logger_registry import LoggerRegistry
from ats_utilities.logger.engine import Logger

#
# default logging [logging]
# ==========================
#
logger_default: Logger = Logger(component_bundle=LoggerRegistry.create_default_logger_bundle())
logger_default.write_log("debug test", DEBUG)
logger_default.write_log("info test", INFO)
logger_default.write_log("warning test", WARNING)
logger_default.write_log("error test", ERROR)
logger_default.write_log("critical test", CRITICAL)

#
# 3rd party [loguru]
# ===================
#


class LoguruATSAdapter(ILogger):
    '''Loguru adapter implementing ILogger interface.'''

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self._map = {
            DEBUG: loguru_native.debug,
            INFO: loguru_native.info,
            WARNING: loguru_native.warning,
            ERROR: loguru_native.error,
            CRITICAL: loguru_native.critical,
        }

    def write_log(self, message: str, ctrl: int) -> None:
        log_func = self._map.get(ctrl)
        if log_func and message:
            log_func(message)

    def is_initialized(self) -> bool:
        return True

    def set_level(self, level: int) -> None:
        pass

    def set_log_file(self, log_file: str) -> None:
        pass

    def stop_buffering(self) -> None:
        pass

    def __str__(self) -> str:
        return 'LoguruATSAdapter'


custom_logger = LoguruATSAdapter()
bundle: LoggerBundle = LoggerBundle(logger=custom_logger, log_file='run.log', log_level=DEBUG)
logger_custom: Logger = Logger(component_bundle=bundle)
logger_custom.write_log("debug test", DEBUG)
logger_custom.write_log("info test", INFO)
logger_custom.write_log("warning test", WARNING)
logger_custom.write_log("error test", ERROR)
logger_custom.write_log("critical test", CRITICAL)
