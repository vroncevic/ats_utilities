# -*- coding: UTF-8 -*-

'''
 Module
     __init__.py
 Copyright
     Copyright (C) 2021 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class Splash with attribute(s) and method(s).
     Load a splash screen info and add hyperlinks.
'''

import sys
from time import sleep

try:
    from six import add_metaclass
    from ats_utilities import VerboseRoot
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
    from ats_utilities.splash.progress_bar import ProgressBar
    from ats_utilities.splash.terminal_properties import TerminalProperties
    from ats_utilities.splash.splash_property import SplashProperty
    from ats_utilities.splash.github_infrastructure import GitHubInfrastructure
    from ats_utilities.splash.ext_infrastructure import ExtInfrastructure
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.5.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@add_metaclass(VerboseRoot)
class Splash(SplashProperty):
    '''
        Defined class Splash with attribute(s) and method(s).
        Load a splash screen info and add hyperlinks.
        It defines:

            :attributes:
                | __verbose - enable/disable verbose option.
            :methods:
                | __init__ - initial constructor.
                | center - center console line.
                | __str__ - dunder method for Splash.
    '''

    def __init__(self, ats_splash_property, verbose=False):
        '''
            Initial constructor.

            :param ats_splash_property: splash property in dict form.
            :type ats_splash_property: <dict>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('dict:ats_splash_property', ats_splash_property)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        SplashProperty.__init__(self, ats_splash_property, verbose)
        self.__verbose = verbose
        if self.validate(self.__verbose or verbose):
            terminal = TerminalProperties(self.__verbose or verbose)
            size = terminal.size(self.__verbose or verbose)
            if ats_splash_property['ats_use_github_infrastructure']:
                with open(ats_splash_property['ats_logo_path'], 'r') as logo:
                    for line in logo:
                        processed_line = line.rstrip()
                        if bool(processed_line):
                            self.center(int(size[1]), 0, processed_line)
                infrastructure = GitHubInfrastructure(
                    ats_splash_property, self.__verbose or verbose
                )
                self.center(int(size[1]), 2, infrastructure.get_info_text())
                self.center(int(size[1]), 2, infrastructure.get_issue_text())
                self.center(int(size[1]), 2, infrastructure.get_author_text())
                print("\n")
            else:
                infrastructure = ExtInfrastructure(
                    ats_splash_property, self.__verbose or verbose
                )
                self.center(int(size[1]), 2, infrastructure.get_info_text())
                self.center(int(size[1]), 2, infrastructure.get_issue_text())
                self.center(int(size[1]), 2, infrastructure.get_author_text())
                print("\n")
            pb = ProgressBar(int(size[1])-int(int(size[1])/2))
            for i in range(0, int(size[1])-int(int(size[1])/2)):
                pb.set_and_plot(i + 1, int(size[1]))
                sleep(0.01)
            del pb

    def center(self, columns, additional_shifter, text, verbose=False):
        '''
            Center console line.

            :param columns: colums for open console session.
            :type columns: <int>
            :param additional_shifter: additional shifters.
            :type additional_shifter: <int>
            :param text: text for console session.
            :type text: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('int:columns', columns),
            ('int:additional_shifter', additional_shifter),
            ('str:text', text)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        verbose_message(
            Splash.VERBOSE, self.__verbose or verbose,
            columns, additional_shifter, text
        )
        start_position = (columns/2) - 21
        number_of_tabs = int((start_position/8) - 1 + additional_shifter)
        print('{0}{1}'.format('\011' * number_of_tabs, text))

    def __str__(self):
        '''
            Dunder method for Splash.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(self.__class__.__name__, str(self.__verbose))
