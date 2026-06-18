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
    Defines class CfgStorer with attribute(s) and method(s).
    Stores the ATS configuration for the ATS.
'''

from typing import Any, Dict, List, Optional
from ats_utilities.config_io.iwrite import IWrite
from ats_utilities.config_io.cfg.icfg_storer import ICfgStorer
from ats_utilities.config_io.config_file_bundle import ATSConfigFileBundle
from ats_utilities.config_io.cfg.object2cfg import Object2Cfg
from ats_utilities.config_io.cfg.cfg_processor import ATSCFGProcessor
from ats_utilities.config_io.cfg.icfg_processor import ICFGProcessor
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.factory_class import format_instance_to_string

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class CfgStorer(ICfgStorer):
    '''
        Defines class CfgStorer with attribute(s) and method(s).
        Stores the ATS configuration for the ATS.
        CFG configuration-based storage support.

        It defines:

            :attributes:
                | __checker - Factoriezed parameters checker (default ATSChecker).
                | __reporter - Factoriezed reporter for messaging (default ATSReporter).
                | __verbose - Factoriezed Enable/Disable verbose option (default False).
                | __processor - Processor for CFG content (default ATSCFGProcessor).
                | __obj2cfg - Out API for information (default Object2Cfg).
            :methods:
                | __init__ - Initials CfgStorer constructor.
                | store_configuration - Stores the ATS configuration.
                | __str__ - Returns the string representation of cfgstorer.
    '''

    def __init__(
        self,
        info_file: Optional[str] = None,
        object2cfg: Optional[IWrite] = None,
        config_bundle: Optional[ATSConfigFileBundle] = None,
        cfg_processor: Optional[ICFGProcessor] = None
    ) -> None:
        '''
            Initials CfgStorer constructor.

            :param info_file: Path to the info file | None
            :type info_file: <Optional[str]>
            :param object2cfg: Out API for information (default set Object2Cfg) | None
            :type object2cfg: <Optional[IWrite]>
            :param config_bundle: Configuration bundle (default set ATSConfigFileBundle) | None
            :type config_bundle: <Optional[ATSConfigFileBundle]>
            :param cfg_processor: Processor for CFG content | None
            :type cfg_processor: <Optional[ICFGProcessor]>
            :exceptions: ATSTypeError by validate_component()
        '''
        config_file_bundle: ATSConfigFileBundle = config_bundle or ATSConfigFileBundle()
        factory_context_bundle(self, config_file_bundle.context)
        self.__processor: ICFGProcessor = make_component(cfg_processor, ATSCFGProcessor, None)
        validate_component(self.__processor, type(self.__processor), type(self.__processor).__name__)
        self.__obj2cfg: IWrite = make_component(object2cfg, Object2Cfg, {
            'config_file': info_file, 'config_bundle': config_file_bundle
        })
        validate_component(self.__obj2cfg, type(self.__obj2cfg), type(self.__obj2cfg).__name__)

    def store_configuration(self, config: Dict[Any, Any]) -> bool:
        '''
            Stores the ATS configuration from dictionary format.

            :param config: Dictionary with CFG information
            :type config: <Dict[Any, Any]>
            :return: True (success) | False (fail)
            :rtype: <bool>
            :exceptions: None
        '''
        lines: List[str] = [f"{k} = {v}\n" for k, v in config.items()]
        self.__processor.from_lines(lines)
        return self.__obj2cfg.write_configuration(self.__processor)

    def __str__(self) -> str:
        '''
            Returns the string representation of CFG storer object.

            :return: The CFG storer object as string representation
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
