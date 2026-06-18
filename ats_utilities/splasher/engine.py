# -*- coding: UTF-8 -*-

'''
Module
    engine.py
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
    Defines class Splasher with attribute(s) and method(s).
    Loads a splash screen info and adds hyperlinks.
'''

from typing import Any, Dict, Tuple, List, Optional
from time import sleep
from ats_utilities.factory_class import format_instance_to_string
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.splasher.isplasher import ISplasher
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.splasher.component_bundle import ATSSplashComponentBundle
from ats_utilities.splasher.iext_infrastructure import IExtInfrastructure
from ats_utilities.splasher.github_infrastructure import GitHubInfrastructure
from ats_utilities.splasher.ext_infrastructure import ExtInfrastructure
from ats_utilities.splasher.iprogress_bar import IProgressBar
from ats_utilities.splasher.progress_bar import ProgressBar
from ats_utilities.splasher.iterminal_properties import ITerminalProperties
from ats_utilities.splasher.terminal_properties import TerminalProperties
from ats_utilities.splasher.isplash_property import ISplashProperty
from ats_utilities.splasher.splash_property import SplashProperty

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class Splasher(ISplasher):
    '''
        Defines class Splasher with attribute(s) and method(s).
        Loads a splash screen info and adds hyperlinks.
        API splash component.

        It defines:

            :attributes: None
            :methods:
                | __init__ - Initials Splasher constructor.
                | center - Center console line.
                | __str__ - Returns the string representation of splash.
    '''

    def __init__(
        self,
        prop: Dict[Any, Any],
        component_bundle: Optional[ATSSplashComponentBundle] = None,
        splash_bundle: Optional[ContextBundle] = None
    ) -> None:
        '''
            Initials Splasher constructor.

            :param prop: Splasher property in dict format
            :type prop: <Dict[Any, Any]>
            :param component_bundle: Bundle with components | None
            :type component_bundle: <Optional[ATSSplashComponentBundle]>
            :param splash_bundle: Bundle with checker, reporter and verbose | None
            :type splash_bundle: <Optional[ContextBundle]>
            :exceptions: None
        '''
        context_bundle: ContextBundle = splash_bundle or ContextBundle()
        bundle: ATSSplashComponentBundle = component_bundle or ATSSplashComponentBundle()
        factory_args: Dict[str, Any] = {'splash_bundle': context_bundle}
        property_splash: ISplashProperty = make_component(bundle.splash_property, SplashProperty, factory_args)
        validate_component(property_splash, type(property_splash), type(property_splash).__name__)
        property_splash.splash_property = prop

        if property_splash.validates():
            terminal_property: ITerminalProperties = make_component(bundle.terminal_property, TerminalProperties, factory_args)
            validate_component(terminal_property, type(terminal_property), type(terminal_property).__name__)
            size: Tuple[Any, ...] = terminal_property.size()

            if bool(prop['ats_use_github_infrastructure']):
                print("\n")

                with open(prop['ats_logo_path'], 'r', encoding='utf-8') as scr:
                    for line in scr:
                        processed_line: str = line.rstrip()

                        if bool(processed_line):
                            self.center(int(size[1]), 0, processed_line)

                github: IExtInfrastructure = make_component(bundle.github, GitHubInfrastructure, factory_args)
                validate_component(github, type(github), type(github).__name__)
                github.infrastructure_property = prop
                self.center(int(size[1]), 2, github.get_info_text())
                self.center(int(size[1]), 2, github.get_issue_text())
                self.center(int(size[1]), 2, github.get_author_text())
                print("\n")
            else:
                ext: IExtInfrastructure = make_component(bundle.ext, ExtInfrastructure, factory_args)
                validate_component(ext, type(ext), type(ext).__name__)
                ext.infrastructure_property = prop
                self.center(int(size[1]), 2, ext.get_info_text())
                self.center(int(size[1]), 2, ext.get_issue_text())
                self.center(int(size[1]), 2, ext.get_author_text())
                print("\n")
            pb: IProgressBar = bundle.pb or ProgressBar(int(size[1]) - int(int(size[1]) / 2))

            for i in range(0, int(size[1]) - int(int(size[1]) / 2)):
                pb.set_and_plot(i + 1, int(size[1]))
                sleep(0.01)
            del pb

    def center(
        self,
        columns: int,
        additional_shifter: int,
        text: Optional[str]
    ) -> None:
        '''
            Center console line.

            :param columns: Colums for console session
            :type columns: <int>
            :param additional_shifter: Additional shifters
            :type additional_shifter: <int>
            :param text: Text for console session | None
            :type text: <Optional[str]>
            :exceptions: ATSTypeError | ATSValueError
        '''
        start_position: float = (columns / 2) - 30
        number_of_tabs = int((start_position / 8) - 1 + additional_shifter)
        print('{0}{1}'.format('\011' * number_of_tabs, text))

    def __str__(self) -> str:
        '''
            Returns the string representation of splash.

            :return: The splash as string representation
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
