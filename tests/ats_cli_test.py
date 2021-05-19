# -*- coding: UTF-8 -*-

'''
 Module
     ats_cli_test.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined classes ATSCliXXXXTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of CLI.
 Execute
     python -m unittest -v ats_cli_test
'''

import sys
import unittest

try:
    from pathlib import Path
    from ats_utilities.cli.cfg_cli import CfgCLI
    from ats_utilities.cli.ini_cli import IniCLI
    from ats_utilities.cli.json_cli import JsonCLI
    from ats_utilities.cli.xml_cli import XmlCLI
    from ats_utilities.cli.yaml_cli import YamlCLI
except ImportError as test_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, test_error_message)
    sys.exit(MESSAGE)  # Force close python test ############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '1.8.7'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSCliCfgAPI(CfgCLI):
    '''Simple Class for checking CfgCLI.'''

    __CONFIG = '/config/ats_cli_cfg_api.cfg'
    __OPS = ['-t', '--test', '-v']

    def __init__(self, verbose=False):
        '''Initial constructor.'''
        current_dir = Path(__file__).resolve().parent
        base_info = '{0}{1}'.format(current_dir, ATSCliCfgAPI.__CONFIG)
        CfgCLI.__init__(self, base_info, verbose=verbose)
        if self.tool_operational:
            self.add_new_option(
                ATSCliCfgAPI.__OPS[0], ATSCliCfgAPI.__OPS[1], dest='test',
                help='flag'
            )
            self.add_new_option(
                ATSCliCfgAPI.__OPS[2], action='store_true', default=False,
                help='activate verbose mode'
            )

    def process(self, verbose=False):
        '''Process and run operation.'''
        status = False
        if self.tool_operational:
            status = True
        return status


class ATSCliIniAPI(IniCLI):
    '''Simple Class for checking IniCLI.'''

    __CONFIG = '/config/ats_cli_ini_api.ini'
    __OPS = ['-t', '--test', '-v']

    def __init__(self, verbose=False):
        '''Initial constructor.'''
        current_dir = Path(__file__).resolve().parent
        base_info = '{0}{1}'.format(current_dir, ATSCliIniAPI.__CONFIG)
        IniCLI.__init__(self, base_info, verbose=verbose)
        if self.tool_operational:
            self.add_new_option(
                ATSCliIniAPI.__OPS[0], ATSCliIniAPI.__OPS[1], dest='test',
                help='flag'
            )
            self.add_new_option(
                ATSCliIniAPI.__OPS[2], action='store_true', default=False,
                help='activate verbose mode'
            )

    def process(self, verbose=False):
        '''Process and run operation.'''
        status = False
        if self.tool_operational:
            status = True
        return status


class ATSCliJsonAPI(JsonCLI):
    '''Simple Class for checking JsonCLI.'''

    __CONFIG = '/config/ats_cli_json_api.json'
    __OPS = ['-t', '--test', '-v']

    def __init__(self, verbose=False):
        '''Initial constructor.'''
        current_dir = Path(__file__).resolve().parent
        base_info = '{0}{1}'.format(current_dir, ATSCliJsonAPI.__CONFIG)
        JsonCLI.__init__(self, base_info, verbose=verbose)
        if self.tool_operational:
            self.add_new_option(
                ATSCliJsonAPI.__OPS[0], ATSCliJsonAPI.__OPS[1], dest='test',
                help='flag'
            )
            self.add_new_option(
                ATSCliJsonAPI.__OPS[2], action='store_true', default=False,
                help='activate verbose mode'
            )

    def process(self, verbose=False):
        '''Process and run operation.'''
        status = False
        if self.tool_operational:
            status = True
        return status


class ATSCliXmlAPI(XmlCLI):
    '''Simple Class for checking XmlCLI.'''

    __CONFIG = '/config/ats_cli_xml_api.xml'
    __OPS = ['-t', '--test', '-v']

    def __init__(self, verbose=False):
        '''Initial constructor.'''
        current_dir = Path(__file__).resolve().parent
        base_info = '{0}{1}'.format(current_dir, ATSCliXmlAPI.__CONFIG)
        XmlCLI.__init__(self, base_info, verbose=verbose)
        if self.tool_operational:
            self.add_new_option(
                ATSCliXmlAPI.__OPS[0], ATSCliXmlAPI.__OPS[1], dest='test',
                help='flag'
            )
            self.add_new_option(
                ATSCliXmlAPI.__OPS[2], action='store_true', default=False,
                help='activate verbose mode'
            )

    def process(self, verbose=False):
        '''Process and run operation.'''
        status = False
        if self.tool_operational:
            status = True
        return status


class ATSCliYamlAPI(YamlCLI):
    '''Simple Class for checking YamlCLI.'''

    __CONFIG = '/config/ats_cli_yaml_api.yaml'
    __OPS = ['-t', '--test', '-v']

    def __init__(self, verbose=False):
        '''Initial constructor.'''
        current_dir = Path(__file__).resolve().parent
        base_info = '{0}{1}'.format(current_dir, ATSCliYamlAPI.__CONFIG)
        YamlCLI.__init__(self, base_info, verbose=verbose)
        if self.tool_operational:
            self.add_new_option(
                ATSCliYamlAPI.__OPS[0], ATSCliYamlAPI.__OPS[1], dest='test',
                help='flag'
            )
            self.add_new_option(
                ATSCliYamlAPI.__OPS[2], action='store_true', default=False,
                help='activate verbose mode'
            )

    def process(self, verbose=False):
        '''Process and run operation.'''
        status = False
        if self.tool_operational:
            status = True
        return status


class CfgTestCase(unittest.TestCase):
    '''
        Defined class CfgTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of ATS CLI interfaces.
        It defines:

            :attributes:
                | ats_cli_cfg_api - API for checking Cfg CLI.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_process - test for process.
    '''

    def setUp(self):
        '''Call before test case.'''
        self.ats_cli_cfg_api = ATSCliCfgAPI()

    def tearDown(self):
        '''Call after test case.'''
        self.ats_cli_cfg_api = None

    def test_process(self):
        '''Test for process.'''
        self.assertTrue(self.ats_cli_cfg_api.process())


class IniTestCase(unittest.TestCase):
    '''
        Defined class IniTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of ATS CLI interfaces.
        It defines:

            :attributes:
                | ats_cli_ini_api - API for checking Ini CLI.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_process - test for process.
    '''

    def setUp(self):
        '''Call before test case.'''
        self.ats_cli_ini_api = ATSCliIniAPI()

    def tearDown(self):
        '''Call after test case.'''
        self.ats_cli_ini_api = None

    def test_process(self):
        '''Test for process.'''
        self.assertTrue(self.ats_cli_ini_api.process())


class JsonTestCase(unittest.TestCase):
    '''
        Defined class JsonTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of ATS CLI interfaces.
        It defines:

            :attributes:
                | ats_cli_json_api - API for checking Json CLI.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_process - test for process.
    '''

    def setUp(self):
        '''Call before test case.'''
        self.ats_cli_json_api = ATSCliJsonAPI()

    def tearDown(self):
        '''Call after test case.'''
        self.ats_cli_json_api = None

    def test_process(self):
        '''Test for process.'''
        self.assertTrue(self.ats_cli_json_api.process())


class XmlTestCase(unittest.TestCase):
    '''
        Defined class XmlTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of ATS CLI interfaces.
        It defines:

            :attributes:
                | ats_cli_xml_api - API for checking Xml CLI.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_process - test for process.
    '''

    def setUp(self):
        '''Call before test case.'''
        self.ats_cli_xml_api = ATSCliXmlAPI()

    def tearDown(self):
        '''Call after test case.'''
        self.ats_cli_xml_api = None

    def test_process(self):
        '''Test for process.'''
        self.assertTrue(self.ats_cli_xml_api.process())


class YamlTestCase(unittest.TestCase):
    '''
        Defined class YamlTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of ATS CLI interfaces.
        It defines:

            :attributes:
                | ats_cli_yaml_api - API for checking Yaml CLI.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_process - test for process.
    '''

    def setUp(self):
        '''Call before test case.'''
        self.ats_cli_yaml_api = ATSCliYamlAPI()

    def tearDown(self):
        '''Call after test case.'''
        self.ats_cli_yaml_api = None

    def test_process(self):
        '''Test for process.'''
        self.assertTrue(self.ats_cli_yaml_api.process())


if __name__ == '__main__':
    unittest.main()
