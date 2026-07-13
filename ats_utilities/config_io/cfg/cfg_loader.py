# -*- coding: UTF-8 -*-

'''
Module
    cfg_loader.py
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
    Defines class CFGLoader with attribute(s) and method(s).
    Loads the ATS configuration for the ATS.
'''

from __future__ import annotations

from typing import override

from ats_utilities.config_io.iread import IRead
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.config_io.iloader import ILoader
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.config_io.config_file_bundle import ConfigFileBundle
from ats_utilities.config_io.cfg.cfg2object import Cfg2Object
from ats_utilities.config_io.cfg.cfg_processor import CFGProcessor
from ats_utilities.config_io.cfg.icfg_processor import ICFGProcessor
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.factory_class import to_str

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class CFGLoader(ILoader):
    '''
        Defines class CFGLoader with attribute(s) and method(s).
        Loads the ATS configuration for the ATS.
        CFG configuration-based API support.

        It defines:

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _logger - Injected logger for logging (default Logger).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _configuration - CFG processor configuration (default None).
            :methods:
                | __init__ - Initializes CFGLoader constructor.
                | load_configuration - Loads the ATS configuration in dictionary format.
                | __str__ - Returns the CFGLoader as string representation.
    '''

    _checker: IChecker
    _logger: ILogger
    _reporter: IReporter
    _verbose: bool
    _configuration: ICFGProcessor | None

    def __init__(
        self,
        info_file: str | None = None,
        cfg2object: IRead | None = None,
        config_bundle: ConfigFileBundle | None = None,
        cfg_processor: ICFGProcessor | None = None
    ) -> None:
        '''
            Initializes CFGLoader constructor.

            :param info_file: Path to the info file | None.
            :type info_file: <str | None>
            :param cfg2object: An API for information | None.
            :type cfg2object: <IRead | None>
            :param config_bundle: Configuration bundle | None.
            :type config_bundle: <ConfigFileBundle | None>
            :param cfg_processor: Processor for CFG content | None.
            :type cfg_processor: <ICFGProcessor | None>
            :exceptions:
                | ATSTypeError: Invalid type in constructor arguments.
        '''
        config_file_bundle: ConfigFileBundle = config_bundle or ConfigFileBundle()
        factory_context_bundle(self, config_file_bundle.context)
        file_checker: IFileCheck = make_component(
            config_file_bundle.file_checker, FileCheck,
            {'config_bundle': ContextBundle(checker=self._checker, reporter=self._reporter, verbose=self._verbose)}
        )
        validate_component(file_checker, IFileCheck, r'file_checker must be an IFileCheck instance')
        processor: ICFGProcessor = make_component(cfg_processor, CFGProcessor, None)
        validate_component(processor, ICFGProcessor, r'processor must be an ICFGProcessor instance')
        cfg2obj: IRead = make_component(cfg2object, Cfg2Object, {
            'config_file': info_file, 'config_bundle': config_file_bundle, 'cfg_processor': processor
        })
        validate_component(cfg2obj, IRead, r'cfg2obj must be an IRead instance')
        self._configuration = None

        if bool(cfg2obj):
            self._configuration = cfg2obj.read_configuration()

    @override
    def load_configuration(self) -> dict[str, str]:
        '''
            Loads the ATS configuration in dictionary format.

            :return: Dictionary with CFG information.
            :rtype: <dict[str, str]>
            :exceptions: None.
        '''
        if not self._configuration:
            return {}

        return self._configuration.to_dict()

    @override
    def __str__(self) -> str:
        '''
            Returns the CFGLoader as string representation.

            :return: The CFGLoader as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return to_str(self)
