# -*- coding: UTF-8 -*-

'''
Module
    cfg_initializer.py
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
    Defines class CfgInitializer with attribute(s) and method(s).
    Loads the ATS configuration for the ATS.
'''

from typing import List, Optional
from ats_utilities.factory_class import (
    inject, get_private_attr, make_component, validate_component, format_instance_to_string
)
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.checker.engine import ATSChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.engine import ATSReporter
from ats_utilities.config_io.iread import IRead
from ats_utilities.config_io.ifile_check import IFileCheck
from ats_utilities.config_io.file_check import FileCheck
from ats_utilities.config_io.config_bundle import ATSConfigBundle
from ats_utilities.config_io.cfg.cfg2object import Cfg2Object
from ats_utilities.config_io.cfg.cfg_processor import ATSCFGProcessor
from ats_utilities.config_io.cfg.icfg_processor import ICFGProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class CfgInitializer:
    '''
        Defines class CfgInitializer with attribute(s) and method(s).
        Loads the ATS configuration for the ATS.
        CFG configuration-based API support.

        It defines:

            :attributes:
                | __checker - Parameters checker (default set ATSChecker).
                | __reporter - Reporter for messaging (default ATSReporter).
                | __verbose - Enable/Disable verbose option (default False).
            :methods:
                | __init__ - Initials CfgInitializer constructor.
                | _checker - Property method for getting the internal checker instance.
                | _reporter - Property method for getting the internal reporter instance.
                | _verbose - Property method for getting the internal verbose flag.
                | __str__ - Returns the string representation of cfgbase.
    '''

    def __init__(
        self,
        info_file: Optional[str] = None,
        cfg2object: Optional[IRead] = None,
        config_bundle: Optional[ATSConfigBundle] = None
    ) -> None:
        '''
            Initials CfgInitializer constructor.

            :param info_file: Path to the info file | None
            :type info_file: <Optional[str]>
            :param cfg2object: In API for information (default set Cfg2Object) | None
            :type cfg2object: <Optional[IRead]>
            :param config_bundle: Configuration bundle (default set ATSConfigBundle) | None
            :type config_bundle: <Optional[ATSConfigBundle]>
            :exceptions: None
        '''
        # No dependency injection then use default ones.
        if not bool(config_bundle):
            config_bundle = ATSConfigBundle()

        inject(
            self,
            ('checker', config_bundle.checker, ATSChecker, None),
            ('reporter', config_bundle.reporter, ATSReporter, ['checker']),
            ('verbose', config_bundle.verbose, False, None)
        )

        file_checker: IFileCheck = make_component(config_bundle.file_checker, FileCheck, {
            'checker': self._checker, 'reporter': self._reporter, 'verbose': self._verbose
        })
        validate_component(file_checker, IFileCheck, 'file_checker')

        #self.__option_parser: Optional[IATSOptionParser] = None

        cfg2obj: IRead = make_component(cfg2object, Cfg2Object, {
            'config_file': info_file,
            'cfg_processor': ATSCFGProcessor(),
            'checker': self._checker,
            'reporter': self._reporter,
            'file_checker': file_checker,
            'verbose': self._verbose
        })
        validate_component(cfg2obj, IRead, 'cfg2object')

        information: Optional[ICFGProcessor] = None

        if bool(cfg2obj):
            information = cfg2obj.read_configuration(self._verbose)

    @property
    def _checker(self) -> IChecker:
        '''
            Property method for getting the internal checker instance.

            :return: The checker instance in IChecker format
            :rtype: <IChecker>
            :exceptions: None
        '''
        return get_private_attr(self, 'checker')

    @property
    def _reporter(self) -> IReporter:
        '''
            Property method for getting the internal reporter instance.

            :return: The reporter instance in IReporter format
            :rtype: <IReporter>
            :exceptions: None
        '''
        return get_private_attr(self, 'reporter')

    @property
    def _verbose(self) -> bool:
        '''
            Property method for getting the internal verbose flag.

            :return: The verbose flag in bool format
            :rtype: <bool>
            :exceptions: None
        '''
        return get_private_attr(self, 'verbose')

    def __str__(self) -> str:
        '''
            Returns the string representation of CFG base object.

            :return: The CFG base object as string representation
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
