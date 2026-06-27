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

from typing import Any, override
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
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.exceptions.ats_runtime_error import ATSRuntimeError
from ats_utilities.exceptions.ats_attribute_error import ATSAttributeError
from ats_utilities.factory_context_bundle import factory_context_bundle
from ats_utilities.factory_class import get_class_name, format_instance_to_string
from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.factory_file_utils import check_file_exists

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
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

            :attributes:
                | _checker - Injected parameters checker (default Checker).
                | _reporter - Injected reporter for messaging (default Reporter).
                | _verbose - Injected Enable/Disable verbose option (default False).
                | _is_initialized - Indicates if the splasher component is initialized (default False).
            :methods:
                | __init__ - Initials Splasher constructor.
                | center - Centers console line.
                | is_initialized - Checks if splasher component is initialized.
                | __str__ - Returns the string representation of Splasher.
    '''

    _checker: IChecker
    _reporter: IReporter
    _verbose: bool

    def __init__(self, component_bundle: SplashComponentBundle | None = None) -> None:
        '''
            Initials Splasher constructor.

            :param component_bundle: Splash screen component bundle | None.
            :type component_bundle: <SplashComponentBundle | None>
            :exceptions: None.
        '''
        # No dependency injection then use default ones.
        bundle: SplashComponentBundle = component_bundle or SplashComponentBundle()
        factory_context_bundle(self, bundle.context_bundle)
        factory_args: dict[str, Any] = {'context_bundle': bundle.context_bundle}
        self._is_initialized: bool = False

        try:
            property_splash: ISplashProperty = make_component(bundle.splash_property, SplashProperty, factory_args)
            validate_component(property_splash, SplashProperty)
            property_splash.splash_property = bundle.prop

            if property_splash.validates():
                terminal_property: ITerminalProperties = make_component(bundle.terminal_property, TerminalProperties, factory_args)
                validate_component(terminal_property, TerminalProperties)
                size: tuple[Any, ...] = terminal_property.size()
                splash_center_bundle: SplashCenterBundle = SplashCenterBundle()

                if bool(bundle.prop[SplashKeys.ATS_USE_GITHUB_INFRASTRUCTURE]):
                    check_file_exists(bundle.prop[SplashKeys.ATS_LOGO_PATH])
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
                    validate_component(github, GitHubInfrastructure)
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
                    validate_component(ext, ExtInfrastructure)
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

                self._is_initialized = True

        except (ATSTypeError, ATSValueError, ATSRuntimeError, ATSAttributeError) as exc:
            self._reporter.error([f'{get_class_name(self)} {exc}'])
        except Exception as exc:
            self._reporter.error([f'{get_class_name(self)} unexpected exception: {exc}'])

    @override
    def center(self, splash_center_bundle: SplashCenterBundle | None = None) -> None:
        '''
            Centers console line.

            :param splash_center_bundle: Splash center bundle for centering console output | None.
            :type splash_center_bundle: <SplashCenterBundle | None>
            :exceptions:
                | ATSTypeError - columns count 'columns' is not an integer.
                | ATSValueError - columns count 'columns' is less than 0.
                | ATSTypeError - additional shifter 'additional_shifter' is not an integer.
                | ATSValueError - additional shifter 'additional_shifter' is less than 0.
                | ATSTypeError - text 'text' is not a string or None.
                | ATSValueError - text 'text' is empty.
        '''
        bundle: SplashCenterBundle = splash_center_bundle or SplashCenterBundle()
        bundle.validate()
        start_position: float = (bundle.columns / 2) - 30
        number_of_tabs = int((start_position / 8) - 1 + bundle.additional_shifter)
        print('{0}{1}'.format('\011' * number_of_tabs, bundle.text))

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if splasher component is initialized.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        return self._is_initialized

    @override
    def __str__(self) -> str:
        '''
            Returns the string representation of Splasher.

            :return: The Splasher as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
