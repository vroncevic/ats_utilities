# -*- coding: UTF-8 -*-

'''
Module
    ats_cli_test.py
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
    Defines classes CLITestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of CLI.
Execute
    python3 -m unittest -v ats_cli_cfg_test
'''

from unittest.mock import MagicMock
from unittest import TestCase, main, mock
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from os.path import dirname
from ats_utilities.base.engine import Base
from ats_utilities.base.component_bundle import BaseComponentBundle
from ats_utilities.splasher.engine import Splasher

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


class ATSCliCfgAPI(Base):
    '''Simple Class for checking CfgCLI.'''

    _CONFIG: str = '/config/correct/ats_cli_cfg_api.cfg'
    _OPS: list[str] = ['-t', '--test', '-v']

    def __init__(self, verbose: bool = False) -> None:
        '''Initial constructor.'''
        current_dir: str = dirname(__file__)
        base_info: str = f'{current_dir}{self._CONFIG}'
        mock_splasher = MagicMock(spec=Splasher)
        bundle = BaseComponentBundle(info_file=base_info, splasher=mock_splasher, use_generator=True)
        super().__init__(bundle)
        if self.is_initialized():
            self.add_new_option(
                self._OPS[0], self._OPS[1], dest='test',
                help='flag'
            )
            self.add_new_option(
                self._OPS[2], action='store_true', default=False,
                help='activate verbose mode'
            )

    def process(self, verbose: bool = False) -> bool:
        '''Process and run operation.'''
        return self.is_initialized()


class CLITestCase(TestCase):
    '''
        Defines class CLITestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ATS CLI interfaces.
        CfgCLI unit tests.

        It defines:

            :attributes:
                | ats_cli_cfg_api - API for checking Cfg CLI.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is ATSCliCfgAPI not None.
                | test_is_initialized - Test is ATSCliCfgAPI initialized.
                | test_initialization_failure - Test base initialization failure.
                | test_process - Test for process.
                | test_add_new_option_called - Test is add new option called.
                | test_parse_args_called - Test is parse args called.
                | test_parse_wrong_args_called - Test parse without args.
                | test_str - Test string representation of ATSCliCfgAPI.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.ats_cli_api: ATSCliCfgAPI = ATSCliCfgAPI()
        self.mock_add_new = MagicMock()
        self.mock_pars_arg = MagicMock()
        self.ats_cli_api.add_new_option = self.mock_add_new
        self.ats_cli_api.parse_args = self.mock_pars_arg

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test for create'''
        self.assertIsNotNone(self.ats_cli_api)

    def test_is_initialized(self) -> None:
        '''Test is_initialized method.'''
        self.assertTrue(self.ats_cli_api.is_initialized())

    @mock.patch('ats_utilities.base.component_bundle.make_component')
    def test_initialization_failure(self, mock_make_component) -> None:
        '''Test base initialization failure.'''
        mock_make_component.side_effect = ATSTypeError('Failed to initialize component')
        invalid_base = ATSCliCfgAPI()
        self.assertFalse(invalid_base.is_initialized())
        # Force options parser to be not None for the decorator but make is_initialized return False:
        invalid_base._is_initialized = False
        invalid_base._options_parser = MagicMock()
        self.assertIsNone(invalid_base.parse_args(['-v']))

    @mock.patch('ats_utilities.base.component_bundle.make_component')
    def test_initialization_unexpected_exception(self, mock_make_component) -> None:
        '''Test base initialization unexpected exception.'''
        mock_make_component.side_effect = Exception('Unexpected error')
        invalid_base = ATSCliCfgAPI()
        self.assertFalse(invalid_base.is_initialized())

    @mock.patch('ats_utilities.base.engine.factory_context_bundle')
    def test_base_initialization_failure_direct(self, mock_factory_context_bundle) -> None:
        '''Test ATSTypeError block inside Base.__init__.'''
        mock_factory_context_bundle.side_effect = ATSTypeError('test type error')
        invalid_base = ATSCliCfgAPI()
        self.assertFalse(invalid_base.is_initialized())

    @mock.patch('ats_utilities.base.engine.factory_context_bundle')
    def test_base_initialization_unexpected_exception_direct(self, mock_factory_context_bundle) -> None:
        '''Test generic Exception block inside Base.__init__.'''
        mock_factory_context_bundle.side_effect = Exception('unexpected')
        invalid_base = ATSCliCfgAPI()
        self.assertFalse(invalid_base.is_initialized())

    def test_base_generator_disabled(self) -> None:
        '''Test Base.__init__ when generator is disabled.'''
        current_dir = dirname(__file__)
        base_info = f'{current_dir}/config/correct/ats_cli_cfg_api.cfg'
        mock_splasher = MagicMock(spec=Splasher)
        bundle = BaseComponentBundle(info_file=base_info, splasher=mock_splasher, use_generator=False)
        class DummyBase(Base):
            def process(self, verbose: bool = False) -> bool:
                return True
        base = DummyBase(bundle)
        self.assertTrue(base.is_initialized())
        self.assertFalse(hasattr(base, '_generator'))

    def test_add_new_option_when_not_initialized(self) -> None:
        '''Test that add_new_option does nothing when not initialized.'''
        # We need a base that is not initialized
        with mock.patch('ats_utilities.base.engine.factory_context_bundle', side_effect=ATSTypeError('fail')):
            invalid_base = ATSCliCfgAPI()
        invalid_base._options_parser = MagicMock()
        invalid_base.add_new_option('-t', '--test')
        invalid_base._options_parser.add_operation.assert_not_called()

    def test_process(self) -> None:
        '''Test for process.'''
        self.assertTrue(self.ats_cli_api.process())

    def test_add_new_option_called(self) -> None:
        '''Test add new option for option parser'''
        self.ats_cli_api.add_new_option('arg1', 'arg2', option='value')
        self.mock_add_new.assert_called_once()

    def test_parse_args_called(self) -> None:
        '''Test parse args'''
        self.ats_cli_api.add_new_option('arg1', 'arg2', option='value')
        self.ats_cli_api.parse_args(['arg1', 'arg2'])
        self.mock_pars_arg.assert_called_once()

    def test_parse_wrong_args_called(self) -> None:
        '''Test parse without args'''
        self.ats_cli_api.add_new_option('arg1', 'arg2', option='value')
        self.assertIsNotNone(self.ats_cli_api.parse_args(None))

    def test_str(self) -> None:
        '''Test string representation of ATSCliCfgAPI.'''
        self.assertIsInstance(str(self.ats_cli_api), str)

    def test_parse_args_real(self) -> None:
        '''Test actual parse_args logic.'''
        api = ATSCliCfgAPI()
        # Test normal parsing:
        parsed = api.parse_args(['-v'])
        self.assertIsNotNone(parsed)
        # Test with _options_parser is None:
        api._options_parser = None
        with self.assertRaises(ATSValueError):
            api.parse_args(['-v'])

    def test_get_shared_context(self) -> None:
        '''Test get_shared_context returns ContextBundle.'''
        from ats_utilities.context_bundle import ContextBundle
        context = self.ats_cli_api.get_shared_context()
        self.assertIsInstance(context, ContextBundle)



if __name__ == '__main__':
    main()
