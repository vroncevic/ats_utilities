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
    from pathlib import Path
    from six import add_metaclass
    from ats_utilities import VerboseRoot
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
    from ats_utilities.splash.progress_bar import ProgressBar
    from ats_utilities.splash.terminal_properties import TerminalProperties
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '2.0.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@add_metaclass(VerboseRoot)
class Splash:
    '''
        Defined class Splash with attribute(s) and method(s).
        Load a splash screen info and add hyperlinks.
        It defines:

            :attributes:
                | ORG - organization name.
                | REPO - repository name.
                | INFO_URL - project info link.
                | INFO_TXT - project info text.
                | ISSUE_URL - project issue link.
                | ISSUE_TXT - project issue text.
                | AUTHOR_URL - author info link.
                | AUTHOR_TXT - author info text.
                | LOGO - path to logo file.
                | __verbose - enable/disable verbose option.
            :methods:
                | __init__ - initial constructor.
                | center - center console line.
                | __str__ - dunder method for Splash.
    '''

    ORG = 'vroncevic'
    REPO = 'ats_utilities'
    INFO_URL = 'https://{0}.github.io/{1}'.format(ORG, REPO)
    INFO_TXT = 'github.io/{0}'.format(REPO)
    ISSUE_URL = 'https://github.com/{0}/{1}/issues/new/choose'.format(
        ORG, REPO
    )
    ISSUE_TXT = 'github.io/issue'
    AUTHOR_URL = 'https://{0}.github.io/bio/'.format(ORG)
    AUTHOR_TXT = '{0}.github.io'.format(ORG)
    LOGO = '/conf/ats_utilities.logo'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        self.__verbose = verbose
        terminal = TerminalProperties(self.__verbose or verbose)
        current_dir = Path(__file__).resolve().parent
        size = terminal.size()
        with open('{0}/..{1}'.format(current_dir, Splash.LOGO), 'r') as logo:
            for line in logo:
                self.center(size.columns, 0, line.rstrip())
        info_text = '\x1b]8;;{0}\a{1}\x1b]8;;\a'.format(
            Splash.INFO_URL, Splash.INFO_TXT
        )
        self.center(size.columns, 2, info_text)
        issue_text = '\x1b]8;;{0}\a{1}\x1b]8;;\a'.format(
            Splash.ISSUE_URL, Splash.ISSUE_TXT
        )
        self.center(size.columns, 2, issue_text)
        author_text = '\x1b]8;;{0}\a{1}\x1b]8;;\a'.format(
            Splash.AUTHOR_URL, Splash.AUTHOR_TXT
        )
        self.center(size.columns, 2, author_text)
        print("\n")
        pb = ProgressBar(size.columns-int(size.columns/2))
        for i in range(0, size.columns-int(size.columns/2)):
            pb.set_and_plot(i + 1, size.columns)
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
        print('\011' * number_of_tabs, text)

    def __str__(self):
        '''
            Dunder method for Splash.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(self.__class__.__name__, str(self.__verbose))
