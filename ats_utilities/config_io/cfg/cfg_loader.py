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
    Defines class CfgLoader with attribute(s) and method(s).
    Loads the ATS configuration for the ATS.
'''

from typing import Any, Dict, List, Optional
from ats_utilities.config_io.iread import IRead
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.config_io.cfg.icfg_loader import ICfgLoader
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.config_io.config_file_bundle import ATSConfigFileBundle
from ats_utilities.config_io.cfg.cfg2object import Cfg2Object
from ats_utilities.config_io.cfg.cfg_processor import ATSCFGProcessor
from ats_utilities.config_io.cfg.icfg_processor import ICFGProcessor
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.factory_class import get_private_attr, format_instance_to_string

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class CfgLoader(ICfgLoader):
    '''
        Defines class CfgLoader with attribute(s) and method(s).
        Loads the ATS configuration for the ATS.
        CFG configuration-based API support.

        It defines:

            :attributes:
                | __checker - Factoriezed parameters checker (default ATSChecker).
                | __reporter - Factoriezed reporter for messaging (default ATSReporter).
                | __verbose - Factoriezed Enable/Disable verbose option (default False).
            :methods:
                | __init__ - Initials CfgLoader constructor.
                | __str__ - Returns the string representation of cfgbase.
    '''

    def __init__(
        self,
        info_file: Optional[str] = None,
        cfg2object: Optional[IRead] = None,
        config_bundle: Optional[ATSConfigFileBundle] = None,
        cfg_processor: Optional[ICFGProcessor] = None
    ) -> None:
        '''
            Initials CfgLoader constructor.

            :param info_file: Path to the info file | None
            :type info_file: <Optional[str]>
            :param cfg2object: In API for information (default set Cfg2Object) | None
            :type cfg2object: <Optional[IRead]>
            :param config_bundle: Configuration bundle (default set ATSConfigFileBundle) | None
            :type config_bundle: <Optional[ATSConfigFileBundle]>
            :exceptions: ATSTypeError by validate_component()
        '''
        config_file_bundle: ATSConfigFileBundle = config_bundle or ATSConfigFileBundle()
        factory_context_bundle(self, config_file_bundle.context)
        context_bundle_shared: ContextBundle = ContextBundle(
            checker=get_private_attr(self, 'checker'),
            reporter=get_private_attr(self, 'reporter'),
            verbose=get_private_attr(self, 'verbose')
        )
        file_checker: IFileCheck = make_component(
            config_file_bundle.file_checker, FileCheck, {'config_bundle': context_bundle_shared}
        )
        validate_component(file_checker, type(file_checker), type(file_checker).__name__)
        processor: ICFGProcessor = make_component(cfg_processor, ATSCFGProcessor, None)
        validate_component(processor, type(processor), type(processor).__name__)
        cfg2obj: IRead = make_component(cfg2object, Cfg2Object, {
            'config_file': info_file, 'config_bundle': config_file_bundle, 'cfg_processor': processor
        })
        validate_component(cfg2obj, type(cfg2obj), type(cfg2obj).__name__)
        self.__information: Optional[ICFGProcessor] = None

        if bool(cfg2obj):
            self.__information = cfg2obj.read_configuration()

    def get_configuration(self) -> Dict[Any, Any]:
        '''
            Gets the ATS configuration in dictionary format.

            :return: Dictionary with CFG information
            :rtype: <Dict[Any, Any]>
            :exceptions: None
        '''
        if not self.__information:
            return {}

        return self.__information.to_dict()

    def __str__(self) -> str:
        '''
            Returns the string representation of CFG base object.

            :return: The CFG base object as string representation
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
