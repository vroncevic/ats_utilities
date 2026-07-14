# -*- coding: UTF-8 -*-

'''
Module
    ats_base_test.py
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
    Defines classes BaseTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of Base.
Execute
    python3 -m unittest -v ats_base_test
'''

from unittest.mock import MagicMock, patch
from unittest import TestCase, main, mock
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from os.path import dirname
from ats_utilities.base.engine import Base
from ats_utilities.base.component_bundle import BaseComponentBundle
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.splasher.engine import Splasher
from ats_utilities.config_io.loader.iconfig_loader import IConfigLoadManager
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.option.ioption_manager import IOptionManager
from ats_utilities.splasher.isplasher import ISplasher
from ats_utilities.generator.igenerator import IGenerator

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class BaseAPI(Base):
    '''Simple Class for checking Base.'''

    _CONFIG: str = '/assets/config/correct/ats_cli_cfg_api.cfg'
    _OPS: list[str] = ['-t', '--test', '-v']

    def __init__(self, verbose: bool = False) -> None:
        '''Initial constructor.'''
        current_dir: str = dirname(dirname(__file__))
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


class BaseTestCase(TestCase):
    '''
        Defines class BaseTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of Base.
        Base unit tests.

        It defines:

            :attributes:
                | base_api - API for checking Base.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_not_none - Test is BaseAPI not None.
                | test_is_initialized - Test is BaseAPI initialized.
                | test_initialization_failure - Test base initialization failure.
                | test_process - Test for process.
                | test_add_new_option_called - Test is add new option called.
                | test_parse_args_called - Test is parse args called.
                | test_parse_wrong_args_called - Test parse without args.
                | test_str - Test string representation of BaseAPI.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.base_api: BaseAPI = BaseAPI()
        self.mock_add_new = MagicMock()
        self.mock_pars_arg = MagicMock()
        self.base_api.add_new_option = self.mock_add_new
        self.base_api.parse_args = self.mock_pars_arg

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_not_none(self) -> None:
        '''Test for create'''
        self.assertIsNotNone(self.base_api)

    def test_is_initialized(self) -> None:
        '''Test is_initialized method.'''
        self.assertTrue(self.base_api.is_initialized())

    @mock.patch('ats_utilities.base.component_bundle.make_component')
    def test_initialization_failure(self, mock_make_component) -> None:
        '''Test base initialization failure.'''
        mock_make_component.side_effect = ATSTypeError('Failed to initialize component')
        invalid_base = BaseAPI()
        self.assertFalse(invalid_base.is_initialized())
        # Force options parser to be not None for the decorator but make is_initialized return False:
        invalid_base._is_initialized = False
        invalid_base._options_parser = MagicMock()
        self.assertIsNone(invalid_base.parse_args(['-v']))

    @mock.patch('ats_utilities.base.component_bundle.make_component')
    def test_initialization_unexpected_exception(self, mock_make_component) -> None:
        '''Test base initialization unexpected exception.'''
        mock_make_component.side_effect = Exception('Unexpected error')
        invalid_base = BaseAPI()
        self.assertFalse(invalid_base.is_initialized())

    @mock.patch('ats_utilities.base.engine.factory_context_bundle')
    def test_base_initialization_failure_direct(self, mock_factory_context_bundle) -> None:
        '''Test ATSTypeError block inside Base.__init__.'''
        mock_factory_context_bundle.side_effect = ATSTypeError('test type error')
        invalid_base = BaseAPI()
        self.assertFalse(invalid_base.is_initialized())

    @mock.patch('ats_utilities.base.engine.factory_context_bundle')
    def test_base_initialization_unexpected_exception_direct(self, mock_factory_context_bundle) -> None:
        '''Test generic Exception block inside Base.__init__.'''
        mock_factory_context_bundle.side_effect = Exception('unexpected')
        invalid_base = BaseAPI()
        self.assertFalse(invalid_base.is_initialized())

    def test_base_generator_disabled(self) -> None:
        '''Test Base.__init__ when generator is disabled.'''
        current_dir = dirname(dirname(__file__))
        base_info = f'{current_dir}/assets/config/correct/ats_cli_cfg_api.cfg'
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
            invalid_base = BaseAPI()
        invalid_base._options_parser = MagicMock()
        invalid_base.add_new_option('-t', '--test')
        invalid_base._options_parser.add_operation.assert_not_called()

    def test_process(self) -> None:
        '''Test for process.'''
        self.assertTrue(self.base_api.process())

    def test_add_new_option_called(self) -> None:
        '''Test add new option for option parser'''
        self.base_api.add_new_option('arg1', 'arg2', option='value')
        self.mock_add_new.assert_called_once()

    def test_parse_args_called(self) -> None:
        '''Test parse args'''
        self.base_api.add_new_option('arg1', 'arg2', option='value')
        self.base_api.parse_args(['arg1', 'arg2'])
        self.mock_pars_arg.assert_called_once()

    def test_parse_wrong_args_called(self) -> None:
        '''Test parse without args'''
        self.base_api.add_new_option('arg1', 'arg2', option='value')
        self.assertIsNotNone(self.base_api.parse_args(None))

    def test_str(self) -> None:
        '''Test string representation of BaseAPI.'''
        self.assertIsInstance(str(self.base_api), str)

    def test_parse_args_real(self) -> None:
        '''Test actual parse_args logic.'''
        api = BaseAPI()
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
        context = self.base_api.get_shared_context()
        self.assertIsInstance(context, ContextBundle)

    def test_base_component_bundle(self) -> None:
        '''Test BaseComponentBundle methods.'''
        bundle1 = BaseComponentBundle()
        mock_config_loader = MagicMock(spec=IConfigLoadManager)
        mock_config_loader.__class__ = IConfigLoadManager
        mock_info_manager = MagicMock(spec=IInfoManager)
        mock_info_manager.__class__ = IInfoManager
        mock_options_parser = MagicMock(spec=IOptionManager)
        mock_options_parser.__class__ = IOptionManager
        mock_splasher = MagicMock(spec=ISplasher)
        mock_splasher.__class__ = ISplasher

        bundle2 = BaseComponentBundle(
            info_file='config_file',
            config_loader=mock_config_loader,
            info_manager=mock_info_manager,
            options_parser=mock_options_parser,
            splasher=mock_splasher,
            context_bundle=ContextBundle()
        )

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.info_file, 'config_file')

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['info_file'], 'config_file')

    def test_base_component_bundle_validation_errors(self) -> None:
        '''Test BaseComponentBundle validation exceptions.'''
        bundle = BaseComponentBundle(info_file=None)
        with self.assertRaises(ValueError):
            bundle.validate()

    @patch('ats_utilities.base.component_bundle.exists', return_value=True)
    def test_base_component_bundle_generator(self, mock_exists) -> None:
        '''Test BaseComponentBundle with generator enabled.'''
        mock_config_loader = MagicMock(spec=IConfigLoadManager)
        mock_config_loader.__class__ = IConfigLoadManager
        mock_info_manager = MagicMock(spec=IInfoManager)
        mock_info_manager.__class__ = IInfoManager
        mock_options_parser = MagicMock(spec=IOptionManager)
        mock_options_parser.__class__ = IOptionManager
        mock_splasher = MagicMock(spec=ISplasher)
        mock_splasher.__class__ = ISplasher
        mock_generator = MagicMock(spec=IGenerator)
        mock_generator.__class__ = IGenerator

        bundle = BaseComponentBundle(
            info_file='config_file',
            config_loader=mock_config_loader,
            info_manager=mock_info_manager,
            options_parser=mock_options_parser,
            splasher=mock_splasher,
            generator=mock_generator,
            use_generator=True
        )
        bundle.validate()
        self.assertTrue(bundle.use_generator)

        # Merge with other bundle using generator
        other = BaseComponentBundle(use_generator=True, generator=mock_generator)
        bundle.merge(other)
        self.assertTrue(bundle.use_generator)

    @patch('ats_utilities.base.component_bundle.exists', return_value=True)
    def test_base_component_bundle_build_exceptions(self, mock_exists) -> None:
        '''Test build exceptions in BaseComponentBundle.'''
        # Force ATSTypeError in _build_components by providing wrong type
        bundle = BaseComponentBundle(info_file='config_file', config_loader="not_a_loader")
        # Post init should print error but not raise
        self.assertEqual(bundle.config_loader, "not_a_loader")

        # Test merge build exception handling
        other = BaseComponentBundle(info_file='config_file', config_loader="not_a_loader")
        with self.assertRaises(ATSValueError):
            bundle.merge(other)

        # Force generic Exception
        with patch('ats_utilities.base.component_bundle.make_component', side_effect=RuntimeError("unexpected")):
            bundle2 = BaseComponentBundle(info_file='config_file')
            with self.assertRaises(ATSValueError):
                bundle2.merge(bundle)


if __name__ == '__main__':
    main()
