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
from ats_utilities.logger.underlying.iunderlying import IUnderlyingLogger
from ats_utilities.logger.setup.bundle import LoggerBundle
from ats_utilities.logger.setup.factory import LoggerBundleFactory
from ats_utilities.logger.engine import Logger

#
# default logging [logging]
# ==========================
#
logger_default: Logger = Logger(own=LoggerBundleFactory.create_bundle())
logger_default.write_log(DEBUG, "debug test")
logger_default.write_log(INFO, "info test")
logger_default.write_log(WARNING, "warning test")
logger_default.write_log(ERROR, "error test")
logger_default.write_log(CRITICAL, "critical test")

#
# 3rd party [loguru]
# ===================
#


class LoguruATSAdapter:
    '''Loguru adapter implementing IUnderlyingLogger interface.'''

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self._map = {
            DEBUG: loguru_native.debug,
            INFO: loguru_native.info,
            WARNING: loguru_native.warning,
            ERROR: loguru_native.error,
            CRITICAL: loguru_native.critical,
        }

    def log(self, level: int, message: str) -> None:
        log_func = self._map.get(level)
        if log_func and message:
            log_func(message)

    def set_level(self, level: int) -> None:
        ...

    def has_handlers(self) -> bool:
        return True

    def add_file_handler(self, log_file: str) -> bool:
        return True

    def add_stdout_handler(self) -> bool:
        return True

    def __str__(self) -> str:
        return 'LoguruATSAdapter'


custom_logger = LoguruATSAdapter()
default_bundle = LoggerBundleFactory.create_bundle()
bundle = LoggerBundle(
    logger=custom_logger,
    has_file_handler=default_bundle.has_file_handler,
    formatter=default_bundle.formatter,
    buffer=default_bundle.buffer,
    handler_manager=default_bundle.handler_manager,
    message_processor=default_bundle.message_processor
)
logger_custom: Logger = Logger(own=bundle)
logger_custom.write_log(DEBUG, "debug test")
logger_custom.write_log(INFO, "info test")
logger_custom.write_log(WARNING, "warning test")
logger_custom.write_log(ERROR, "error test")
logger_custom.write_log(CRITICAL, "critical test")
