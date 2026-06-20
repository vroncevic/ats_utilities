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
    Defines class Splasher with method(s).
    Implements a splash screen with hyperlinks.
'''

from typing import Any, Dict, Tuple, List, Optional
from time import sleep
from ats_utilities.splasher.isplasher import ISplasher
from ats_utilities.splasher.component_bundle import SplashComponentBundle
from ats_utilities.splasher.isplash_property import ISplashProperty
from ats_utilities.splasher.splash_property import SplashProperty
from ats_utilities.splasher.splash_center_bundle import SplashCenterBundle
from ats_utilities.splasher.iterminal_properties import ITerminalProperties
from ats_utilities.splasher.terminal_properties import TerminalProperties
from ats_utilities.splasher.iext_infrastructure import IExtInfrastructure
from ats_utilities.splasher.ext_infrastructure import ExtInfrastructure
from ats_utilities.splasher.github_infrastructure import GitHubInfrastructure
from ats_utilities.splasher.iprogress_bar import IProgressBar
from ats_utilities.splasher.progress_bar import ProgressBar
from ats_utilities.splasher.splash_keys import SplashKeys
from ats_utilities.factory_class import format_instance_to_string
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.exceptions.ats_value_error import ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class Splasher(ISplasher):
    '''
        Defines class Splasher with method(s).
        Implements a splash screen with hyperlinks.

        It defines:

            :attributes: None
            :methods:
                | __init__ - Initials Splasher constructor.
                | center - Centers console line.
                | __str__ - Returns the string representation of Splasher.
    '''

    def __init__(self, component_bundle: Optional[SplashComponentBundle] = None) -> None:
        '''
            Initials Splasher constructor.

            :param component_bundle: Splash screen component bundle | None.
            :type component_bundle: <Optional[SplashComponentBundle]>
            :exceptions: ATSTypeError
        '''
        # No dependency injection then use default ones.
        bundle: SplashComponentBundle = component_bundle or SplashComponentBundle()
        factory_args: Dict[str, Any] = {'context_bundle': bundle.context_bundle}
        property_splash: ISplashProperty = make_component(bundle.splash_property, SplashProperty, factory_args)
        validate_component(property_splash, type(property_splash), type(property_splash).__name__)
        property_splash.splash_property = bundle.prop

        if property_splash.validates():
            terminal_property: ITerminalProperties = make_component(bundle.terminal_property, TerminalProperties, factory_args)
            validate_component(terminal_property, type(terminal_property), type(terminal_property).__name__)
            size: Tuple[Any, ...] = terminal_property.size()
            splash_center_bundle: SplashCenterBundle = SplashCenterBundle()

            if bool(bundle.prop[SplashKeys.ATS_USE_GITHUB_INFRASTRUCTURE]):
                print("\n")

                with open(bundle.prop[SplashKeys.ATS_LOGO_PATH], 'r', encoding='utf-8') as scr:
                    for line in scr:
                        processed_line: str = line.rstrip()

                        if bool(processed_line):
                            splash_center_bundle.columns = int(size[1])
                            splash_center_bundle.additional_shifter = 0
                            splash_center_bundle.text = processed_line
                            self.center(splash_center_bundle)

                github: IExtInfrastructure = make_component(bundle.github, GitHubInfrastructure, factory_args)
                validate_component(github, type(github), type(github).__name__)
                github.infrastructure_property = bundle.prop
                splash_center_bundle.columns = int(size[1])
                splash_center_bundle.additional_shifter = 2
                splash_center_bundle.text = github.get_info_text()
                self.center(splash_center_bundle)
                splash_center_bundle.text = github.get_issue_text()
                self.center(splash_center_bundle)
                splash_center_bundle.text = github.get_author_text()
                self.center(splash_center_bundle)
                print("\n")
            else:
                ext: IExtInfrastructure = make_component(bundle.ext, ExtInfrastructure, factory_args)
                validate_component(ext, type(ext), type(ext).__name__)
                ext.infrastructure_property = bundle.prop
                splash_center_bundle.columns = int(size[1])
                splash_center_bundle.additional_shifter = 2
                splash_center_bundle.text = ext.get_info_text()
                self.center(splash_center_bundle)
                splash_center_bundle.text = ext.get_issue_text()
                self.center(splash_center_bundle)
                splash_center_bundle.text = ext.get_author_text()
                self.center(splash_center_bundle)
                print("\n")
            pb: IProgressBar = bundle.pb or ProgressBar(int(size[1]) - int(int(size[1]) / 2))

            for i in range(0, int(size[1]) - int(int(size[1]) / 2)):
                pb.set_and_plot(i + 1, int(size[1]))
                sleep(0.01)
            del pb

    def center(self, splash_center_bundle: Optional[SplashCenterBundle] = None) -> None:
        '''
            Centers console line.

            :param splash_center_bundle: Splash center bundle for centering console output | None.
            :type splash_center_bundle: <Optional[SplashCenterBundle]>
            :exceptions: ATSTypeError, ATSValueError
        '''
        if splash_center_bundle is None:
            raise ATSTypeError("splash_center_bundle cannot be None")

        if not isinstance(splash_center_bundle, SplashCenterBundle):
            raise ATSTypeError("splash_center_bundle must be of type SplashCenterBundle")

        if not isinstance(splash_center_bundle.columns, int):
            raise ATSTypeError("columns must be of type int")

        if not isinstance(splash_center_bundle.additional_shifter, int):
            raise ATSTypeError("additional_shifter must be of type int")

        if splash_center_bundle.text is None:
            pass
        elif not isinstance(splash_center_bundle.text, str):
            raise ATSTypeError("text must be of type str")
        elif splash_center_bundle.text == '':
            raise ATSValueError("text cannot be empty")

        start_position: float = (splash_center_bundle.columns / 2) - 30
        number_of_tabs = int((start_position / 8) - 1 + splash_center_bundle.additional_shifter)
        print('{0}{1}'.format('\011' * number_of_tabs, splash_center_bundle.text))

    def __str__(self) -> str:
        '''
            Returns the string representation of Splasher.

            :return: The Splasher as string representation.
            :rtype: <str>
            :exceptions: None
        '''
        return format_instance_to_string(self)
