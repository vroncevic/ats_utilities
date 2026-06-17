# -*- coding: UTF-8 -*-

'''
Module
    ats_base_xml_test.py
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
    Defines classes XmlBaseTestCase with attribute(s) and method(s).
    Defines classes XmlBaseTestCase and XmlBaseUnitTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of Xml.
Execute
    python3 -m unittest -v ats_base_xml_test
'''

from typing import List
from unittest import TestCase, main
from unittest.mock import MagicMock
from os.path import dirname
from ats_utilities.config_io.xml.xmlbase import XmlBase
from ats_utilities.config_io.iread import IRead
from ats_utilities.config_io.iwrite import IWrite
from ats_utilities.checker.ichecker import IChecker
from ats_utilities.option.ats_option_parser import ATSOptionParser
from ats_utilities.reporter.ireporter import IReporter
from ats_utilities.reporter.engine import ATSReporter
from ats_utilities.exceptions.ats_type_error import ATSTypeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.7'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ATSBaseXml(XmlBase):
    '''Simple Class for checking XmlBase.'''

    _CONFIG: str = '/config/correct/ats_cli_xml_api.xml'
    _OPS: List[str] = ['-t', '--test', '-v']

    def __init__(self, reporter: IReporter = ATSReporter(), verbose: bool = False) -> None:
        '''Initial constructor.'''
        current_dir: str = dirname(__file__)
        base_info: str = f'{current_dir}{self._CONFIG}'
        super().__init__(info_file=base_info, verbose=verbose)
        self._verbose = verbose
        if self.is_tool_ok():
            reporter.success(['init ATS xml cli'])


class XmlBaseTestCase(TestCase):
    '''
        Defines class XmlBaseTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ATS Xml interfaces.
        XmlBase unit tests.

        It defines:

            :attributes:
                | ats_base_xml - API for checking base Xml.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is ATSBaseXml not None.
                | test_tool_operational - Test is tool operational.
                | test_none_config_path - Test for None as file path.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.ats_base_xml: ATSBaseXml = ATSBaseXml()

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test for create XmlBase'''
        self.assertIsNotNone(self.ats_base_xml)

    def test_tool_operational(self) -> None:
        '''Test is tool operational'''
        self.assertTrue(self.ats_base_xml.is_tool_ok())

    def test_none_config_path(self) -> None:
        '''Test for None as file path'''
        with self.assertRaises(ATSTypeError):
            XmlBase(None)


class XmlBaseUnitTestCase(TestCase):
    '''
        Unit tests for XmlBase class using mocks.

        It defines:

            :attributes:
                | config_path - Path for configuration file.
                | mock_checker - Mocked IChecker.
                | mock_reporter - Mocked IReporter.
                | mock_xml2obj - Mocked IRead interface.
                | mock_obj2xml - Mocked IWrite interface.
            :methods:
                | setUp - Set up test environment with mocks.
                | test_init - Test initialization.
                | test_is_tool_ok_non_operational - Test non-operational status.
                | test_option_parser_access_non_operational - Test property error.
                | test_operational_xml_base - Test operational state.
    '''

    def setUp(self) -> None:
        '''Set up test environment.'''
        self.config_path = 'ats_cli_xml_api.xml'
        self.mock_checker = MagicMock(spec=IChecker)
        self.mock_reporter = MagicMock(spec=IReporter)
        self.mock_xml2obj = MagicMock(spec=IRead)
        self.mock_obj2xml = MagicMock(spec=IWrite)

        # Setup mock behavior
        self.mock_checker.validate_parameters.return_value = ('', 0)
        self.mock_xml2obj.read_configuration.return_value = {}

        # Use keyword arguments to ensure correct dependency injection
        self.xml_base: XmlBase = XmlBase(
            info_file=self.config_path,
            xml2obj=self.mock_xml2obj,
            obj2xml=self.mock_obj2xml,
            checker=self.mock_checker,
            reporter=self.mock_reporter,
            verbose=True
        )

    def test_init(self) -> None:
        '''Test initialization of XmlBase.'''
        self.assertIsNotNone(self.xml_base)
        self.mock_xml2obj.read_configuration.assert_called_once()

    def test_is_tool_ok_non_operational(self) -> None:
        '''Test is_tool_ok status when XmlBase is not operational.'''
        self.assertFalse(self.xml_base.is_tool_ok())

    def test_option_parser_access_non_operational(self) -> None:
        '''Test if option_parser access returns None when not operational.'''
        self.assertIsNone(self.xml_base.option_parser)

    def test_operational_xml_base(self) -> None:
        '''Test XmlBase when it is operational.'''
        operational_mock_xml2obj = MagicMock(spec=IRead)
        operational_mock_obj2xml = MagicMock(spec=IWrite)
        operational_mock_checker = MagicMock(spec=IChecker)
        operational_mock_reporter = MagicMock(spec=IReporter)
        operational_mock_options_parser = MagicMock(spec=ATSOptionParser)

        operational_mock_checker.validate_parameters.return_value = ('', 0)

        # Mock the IXMLProcessor (or equivalent) that read_configuration is expected to return
        mock_xml_processor = MagicMock()
        mock_ats_info = MagicMock()

        def mock_get(key: str):
            return {
                'ats_name': 'Test Tool',
                'ats_version': '1.0.0',
                'ats_licence': 'MIT',
                'ats_build_date': '2023-01-01'
            }.get(key)

        mock_ats_info.get.side_effect = mock_get
        mock_xml_processor.get_ats_info.return_value = mock_ats_info
        operational_mock_xml2obj.read_configuration.return_value = mock_xml_processor

        operational_xml_base = XmlBase(
            info_file=self.config_path,
            xml2obj=operational_mock_xml2obj,
            obj2xml=operational_mock_obj2xml,
            options_parser=operational_mock_options_parser,
            checker=operational_mock_checker,
            reporter=operational_mock_reporter,
            verbose=True
        )

        self.assertTrue(operational_xml_base.is_tool_ok())
        self.assertIsNotNone(operational_xml_base.option_parser)
        operational_mock_xml2obj.read_configuration.assert_called_once()
        operational_mock_options_parser.add_version_operation.assert_called_once_with('1.0.0')


if __name__ == '__main__':
    main()
