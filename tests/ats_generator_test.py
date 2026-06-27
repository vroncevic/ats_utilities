# -*- coding: UTF-8 -*-

'''
Module
    ats_generator_test.py
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
    Defines classes GeneratorTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of Generator.
Execute
    python3 -m unittest -v ats_generator_test
'''

import os
import tempfile
from unittest import TestCase, main, mock
from ats_utilities.generator.engine import Generator
from ats_utilities.generator.generator_bundle import GeneratorBundle
from ats_utilities.generator.scheme_loader import SchemeLoader
from ats_utilities.generator.template_processor import TemplateProcessor
from ats_utilities.generator.tar_processor import TarProcessor
from ats_utilities.generator.tar_process_bundle import TarProcessBundle
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.exceptions.ats_generator_error import ATSGeneratorError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class GeneratorTestCase(TestCase):
    '''
        Defines class GeneratorTestCase with attribute(s) and method(s).
        Creates test cases for checking Generator interfaces.
        Generator unit tests.

        It defines:

            :attributes:
                | archive_path - Path to the hexagonal templates archive.
                | scheme_path - Path to the hexagonal templates scheme.
                | generator - Generator instance to test.
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_generator_initialization - Test is generator initialized.
                | test_generate_invalid_inputs - Test validation with invalid inputs.
                | test_generate_success - Test successful generation of a project.
                | test_str - Test string representation of Generator.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.archive_path = 'config/hexagonal_templates.tgz'
        self.scheme_path = 'config/hexagonal_templates.json'
        self.generator = Generator()

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_generator_initialization(self) -> None:
        '''Test is generator initialized'''
        self.assertIsNotNone(self.generator)
        self.assertTrue(self.generator.is_initialized())

    def test_generate_invalid_inputs(self) -> None:
        '''Test validation with invalid inputs'''
        # Invalid type for archive_path
        with self.assertRaises(ATSTypeError):
            bundle = GeneratorBundle(
                archive_path=123,  # type: ignore
                target_dir='/tmp',
                template_key='gen_standalone',
                scheme={},
                template_values={'project_name': 'test_app'}
            )
            self.generator.generate(bundle)

        # Invalid type for scheme
        with self.assertRaises(ATSTypeError):
            bundle = GeneratorBundle(
                archive_path=self.archive_path,
                target_dir='/tmp',
                template_key='gen_standalone',
                scheme=123,  # type: ignore
                template_values={'project_name': 'test_app'}
            )
            self.generator.generate(bundle)

        # Archive does not exist
        with self.assertRaises(ATSValueError):
            bundle = GeneratorBundle(
                archive_path='nonexistent_archive.tgz',
                target_dir='/tmp',
                template_key='gen_standalone',
                scheme={},
                template_values={'project_name': 'test_app'}
            )
            self.generator.generate(bundle)

        # Scheme file does not exist
        with self.assertRaises(ATSValueError):
            bundle = GeneratorBundle(
                archive_path=self.archive_path,
                target_dir='/tmp',
                template_key='gen_standalone',
                scheme='nonexistent_scheme.json',
                template_values={'project_name': 'test_app'}
            )
            self.generator.generate(bundle)

        # template_key not in scheme
        with self.assertRaises(ATSValueError):
            bundle = GeneratorBundle(
                archive_path=self.archive_path,
                target_dir='/tmp',
                template_key='invalid_key',
                scheme=self.scheme_path,
                template_values={'project_name': 'test_app'}
            )
            self.generator.generate(bundle)

        # Missing project_name
        with self.assertRaises(ATSValueError):
            bundle = GeneratorBundle(
                archive_path=self.archive_path,
                target_dir='/tmp',
                template_key='gen_standalone',
                scheme=self.scheme_path,
                template_values={}
            )
            self.generator.generate(bundle)

    def test_generate_success(self) -> None:
        '''Test successful generation of a project'''
        with tempfile.TemporaryDirectory() as tmp_dir:
            bundle = GeneratorBundle(
                archive_path=self.archive_path,
                target_dir=tmp_dir,
                template_key='gen_standalone',
                scheme=self.scheme_path,
                template_values={'project_name': 'my_awesome_app'}
            )
            result = self.generator.generate(bundle)
            self.assertTrue(result)

            # Check that files were created and renamed correctly
            expected_files = [
                'main.py',
                'run.sh',
                'run_coverage.py',
                'my_awesome_app/__init__.py',
                'my_awesome_app/engine.py',
                'my_awesome_app/my_awesome_app_bundle.py',
                'my_awesome_app/imy_awesome_app.py',
                'my_awesome_app/domain/models.py',
                'tests/test_engine.py'
            ]
            for rel_file in expected_files:
                full_file_path = os.path.join(tmp_dir, rel_file)
                self.assertTrue(
                    os.path.exists(full_file_path),
                    f"File not found: {full_file_path}"
                )

            # Check that template placeholders were substituted
            engine_py_path = os.path.join(tmp_dir, 'my_awesome_app/engine.py')
            with open(engine_py_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Verify standard replacement of TaskCLI -> MyAwesomeApp
                self.assertIn('class MyAwesomeApp(IMyAwesomeApp):', content)
                self.assertIn('my_awesome_app', content)
                self.assertNotIn('task_cli', content)
                self.assertNotIn('TaskCLI', content)

    def test_str(self) -> None:
        '''Test string representation of Generator'''
        self.assertIsInstance(str(self.generator), str)

    def test_prepare_template_values(self) -> None:
        '''Test prepare_template_values method with various inputs.'''
        # Test missing project_name
        with self.assertRaises(ATSValueError):
            self.generator.prepare_template_values({})

        # Test project_name present but name case variations also present (triggers False branch of ifs)
        vals = {
            'project_name': 'my_project',
            'project_name_dashed': 'custom-dashed',
            'project_name_camel': 'CustomCamel',
            'project_name_upper': 'CUSTOM_UPPER'
        }
        res = self.generator.prepare_template_values(vals)
        self.assertEqual(res['project_name_dashed'], 'custom-dashed')
        self.assertEqual(res['project_name_camel'], 'CustomCamel')
        self.assertEqual(res['project_name_upper'], 'CUSTOM_UPPER')

    @mock.patch('ats_utilities.generator.engine.make_component')
    def test_generator_initialization_failures(self, mock_make_component) -> None:
        '''Test Generator initialization with errors.'''
        # Test ATSTypeError
        mock_make_component.side_effect = ATSTypeError('Failed type')
        invalid_generator = Generator()
        self.assertFalse(invalid_generator._is_initialized)

        # Test unexpected Exception
        mock_make_component.side_effect = Exception('Unexpected')
        invalid_generator = Generator()
        self.assertFalse(invalid_generator._is_initialized)

    def test_scheme_loader_failures(self) -> None:
        '''Test SchemeLoader error handling and edge cases.'''
        loader = SchemeLoader()

        # Wrong type
        with self.assertRaises(ATSTypeError):
            loader.load(123)  # type: ignore

        # Non-existent path
        with self.assertRaises(ATSValueError):
            loader.load('non_existent.json')

        # Unsupported format (suffix not .json)
        with tempfile.NamedTemporaryFile(suffix='.txt') as tmp:
            with self.assertRaises(ATSValueError):
                loader.load(tmp.name)

        # Failed setup config loader (returns None)
        with tempfile.NamedTemporaryFile(suffix='.json') as tmp:
            with mock.patch('ats_utilities.generator.scheme_loader.ConfigLoader.setup_config_loader', return_value=None):
                with self.assertRaises(ATSGeneratorError):
                    loader.load(tmp.name)

        # Failed setup config loader (raises Exception)
        with tempfile.NamedTemporaryFile(suffix='.json') as tmp:
            with mock.patch('ats_utilities.generator.scheme_loader.ConfigLoader.setup_config_loader', side_effect=Exception('Load failed')):
                with self.assertRaises(ATSGeneratorError):
                    loader.load(tmp.name)

        # Return dict when dict is passed
        self.assertEqual(loader.load({'a': 'b'}), {'a': 'b'})

    def test_template_processor_binary_content(self) -> None:
        '''Test TemplateProcessor fallback for binary content.'''
        proc = TemplateProcessor()
        res = proc.render(b'\xff\xfe\xfd', {})
        self.assertEqual(res, b'\xff\xfe\xfd')

    def test_generate_failures(self) -> None:
        '''Test Generator.generate failure paths.'''
        # Template key not found
        bundle = GeneratorBundle(
            archive_path=self.archive_path,
            target_dir='/tmp',
            template_key='non_existent',
            scheme=self.scheme_path,
            template_values={'project_name': 'test'}
        )
        with self.assertRaises(ATSValueError):
            self.generator.generate(bundle)

        # Source dir not specified in scheme configuration
        with mock.patch.object(self.generator._scheme_loader, 'load', return_value={'gen_standalone': {'dummy': 'value'}}):
            bundle = GeneratorBundle(
                archive_path=self.archive_path,
                target_dir='/tmp',
                template_key='gen_standalone',
                scheme=self.scheme_path,
                template_values={'project_name': 'test'}
            )
            with self.assertRaises(ATSValueError):
                self.generator.generate(bundle)

        # Unexpected exception during generation
        with mock.patch.object(self.generator._tar_processor, 'process', side_effect=Exception('process failed')):
            bundle = GeneratorBundle(
                archive_path=self.archive_path,
                target_dir='/tmp',
                template_key='gen_standalone',
                scheme=self.scheme_path,
                template_values={'project_name': 'test'}
            )
            with self.assertRaises(ATSGeneratorError):
                self.generator.generate(bundle)

    def test_tar_processor_failures(self) -> None:
        '''Test TarProcessor exception handling.'''
        proc = TarProcessor()
        bundle = TarProcessBundle(
            archive_path='a.tgz',
            target_dir='tmp',
            source_dir='src',
            path_replacements={},
            exclude_patterns=[],
            vals={}
        )
        with mock.patch('tarfile.open', side_effect=Exception('tar open failed')):
            with self.assertRaises(ATSGeneratorError):
                proc.process(bundle)

    def test_generate_with_exclude_patterns(self) -> None:
        '''Test generation while excluding specific files.'''
        with tempfile.TemporaryDirectory() as tmp_dir:
            bundle = GeneratorBundle(
                archive_path=self.archive_path,
                target_dir=tmp_dir,
                template_key='gen_standalone',
                scheme={
                    'gen_standalone': {
                        'source_dir': 'gen_standalone_templates',
                        'path_replacements': {'task_cli': 'project_name'},
                        'exclude': ['*run.sh*']
                    }
                },
                template_values={'project_name': 'my_awesome_app'}
            )
            result = self.generator.generate(bundle)
            self.assertTrue(result)
            self.assertFalse(os.path.exists(os.path.join(tmp_dir, 'run.sh')))
            self.assertTrue(os.path.exists(os.path.join(tmp_dir, 'main.py')))


if __name__ == '__main__':
    main()
