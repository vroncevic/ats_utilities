# -*- coding: UTF-8 -*-

'''
Module
    cfg_storer.py
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
    Defines class CFGStorer with attribute(s) and method(s).
    Stores the ATS configuration for the ATS.
'''

from ats_utilities.config_io.iwrite import IWrite
from ats_utilities.config_io.istorer import IStorer
from ats_utilities.config_io.config_file_bundle import ATSConfigFileBundle
from ats_utilities.config_io.cfg.object2cfg import Object2Cfg
from ats_utilities.config_io.cfg.cfg_processor import CFGProcessor
from ats_utilities.config_io.cfg.icfg_processor import ICFGProcessor
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.checker.proxy_validator import validator
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.factory_class import format_instance_to_string

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class CFGStorer(IStorer):
    '''
        Defines class CFGStorer with attribute(s) and method(s).
        Stores the ATS configuration for the ATS.
        CFG configuration-based storage support.

        It defines:

            :attributes:
                | _checker - Factoriezed parameters checker (default Checker).
                | _reporter - Factoriezed reporter for messaging (default Reporter).
                | _verbose - Factoriezed Enable/Disable verbose option (default False).
                | _processor - Processor for CFG content (default CFGProcessor).
                | _obj2cfg - Out API for information (default Object2Cfg).
            :methods:
                | __init__ - Initializes CFGStorer constructor.
                | store_configuration - Stores the ATS configuration.
                | __str__ - Returns the CFGStorer as string representation.
    '''

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    def __init__(
        self,
        info_file: str | None = None,
        object2cfg: IWrite | None = None,
        config_bundle: ATSConfigFileBundle | None = None,
        cfg_processor: ICFGProcessor | None = None
    ) -> None:
        '''
            Initializes CFGStorer constructor.

            :param info_file: Path to the info file | None.
            :type info_file: <str | None>
            :param object2cfg: An API for information | None.
            :type object2cfg: <IWrite | None>
            :param config_bundle: Configuration bundle | None.
            :type config_bundle: <ATSConfigFileBundle | None>
            :param cfg_processor: Processor for CFG content | None.
            :type cfg_processor: <ICFGProcessor | None>
            :exceptions: ATSTypeError.
        '''
        config_file_bundle: ATSConfigFileBundle = config_bundle or ATSConfigFileBundle()
        factory_context_bundle(self, config_file_bundle.context)
        self._processor: ICFGProcessor = make_component(cfg_processor, CFGProcessor, None)
        validate_component(self._processor, type(self._processor), type(self._processor).__name__)
        self._obj2cfg: IWrite = make_component(object2cfg, Object2Cfg, {
            'config_file': info_file, 'config_bundle': config_file_bundle
        })
        validate_component(self._obj2cfg, type(self._obj2cfg), type(self._obj2cfg).__name__)

    @validator([('dict:config', None)])
    def store_configuration(self, config: dict[str, str]) -> bool:
        '''
            Stores the ATS configuration from dictionary format.

            :param config: Dictionary with CFG information.
            :type config: <dict[str, str]>
            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: ATSTypeError, ATSValueError, ATSRuntimeError, ATSAttributeError..
        '''
        lines: list[str] = [f"{k} = {v}\n" for k, v in config.items()]
        self._processor.from_lines(lines)
        return self._obj2cfg.write_configuration(self._processor)

    def __str__(self) -> str:
        '''
            Returns the CFGStorer as string representation.

            :return: The CFGStorer as string representation.
            :rtype: <str>
            :exceptions: None..
        '''
        return format_instance_to_string(self)
