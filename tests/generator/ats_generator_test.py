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
from unittest.mock import MagicMock
from tarfile import TarFile, TarInfo

from ats_utilities.context_bundle import ContextBundle
from ats_utilities.generator.engine import Generator
from ats_utilities.generator.generator_bundle import GeneratorBundle
from ats_utilities.generator.component_bundle import GeneratorComponentBundle
from ats_utilities.generator.scheme.scheme_loader import SchemeLoader
from ats_utilities.generator.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generator.tar.tar_processor import TarProcessor
from ats_utilities.generator.tar.itar_processor import ITarProcessor
from ats_utilities.generator.template.template_processor import TemplateProcessor
from ats_utilities.generator.template.itemplate_processor import ITemplateProcessor
from ats_utilities.generator.tar.tar_process_bundle import TarProcessBundle
from ats_utilities.generator.tar.tar_process_member_bundle import TarProcessMemberBundle
from ats_utilities.exceptions import ATSGeneratorError, ATSTypeError, ATSValueError

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'


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
        self.archive_path = os.path.join(os.path.dirname(__file__), 'config', 'hexagonal_templates.tgz')
        self.scheme_path = os.path.join(os.path.dirname(__file__), 'config', 'hexagonal_templates.json')
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

    @mock.patch('ats_utilities.generator.component_bundle.make_component')
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
            with mock.patch('ats_utilities.generator.scheme.scheme_loader.ConfigLoader.setup_config_loader', return_value=None):
                with self.assertRaises(ATSGeneratorError):
                    loader.load(tmp.name)

        # Failed setup config loader (raises Exception)
        with tempfile.NamedTemporaryFile(suffix='.json') as tmp:
            with mock.patch('ats_utilities.generator.scheme.scheme_loader.ConfigLoader.setup_config_loader', side_effect=Exception('Load failed')):
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

    def test_get_shared_context(self) -> None:
        '''Test get_shared_context returns ContextBundle.'''
        from ats_utilities.context_bundle import ContextBundle
        context = self.generator.get_shared_context()
        self.assertIsInstance(context, ContextBundle)

    def test_generator_component_bundle(self) -> None:
        '''Test GeneratorComponentBundle methods.'''
        mock_scheme_loader = MagicMock(spec=ISchemeLoader)
        mock_tar_processor = MagicMock(spec=ITarProcessor)
        mock_template_processor = MagicMock(spec=ITemplateProcessor)
        mock_context_bundle = ContextBundle()

        bundle1 = GeneratorComponentBundle()
        bundle2 = GeneratorComponentBundle(
            scheme_loader=mock_scheme_loader,
            tar_processor=mock_tar_processor,
            template_processor=mock_template_processor,
            context_bundle=mock_context_bundle
        )

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.scheme_loader, mock_scheme_loader)
        self.assertEqual(bundle1.tar_processor, mock_tar_processor)
        self.assertEqual(bundle1.template_processor, mock_template_processor)
        self.assertEqual(bundle1.context_bundle, mock_context_bundle)

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['scheme_loader'], mock_scheme_loader)

    def test_generator_component_bundle_validation_errors(self) -> None:
        '''Test GeneratorComponentBundle validation exceptions.'''
        mock_scheme_loader = MagicMock(spec=ISchemeLoader)
        mock_tar_processor = MagicMock(spec=ITarProcessor)
        mock_template_processor = MagicMock(spec=ITemplateProcessor)
        mock_context_bundle = ContextBundle()

        fields = {
            'scheme_loader': mock_scheme_loader,
            'tar_processor': mock_tar_processor,
            'template_processor': mock_template_processor,
            'context_bundle': mock_context_bundle
        }

        for field in fields:
            bundle = GeneratorComponentBundle(
                scheme_loader=mock_scheme_loader,
                tar_processor=mock_tar_processor,
                template_processor=mock_template_processor,
                context_bundle=mock_context_bundle
            )
            setattr(bundle, field, None)
            with self.assertRaises(ATSValueError):
                bundle.validate()

    def test_generator_bundle_methods(self) -> None:
        '''Test GeneratorBundle methods.'''
        bundle1 = GeneratorBundle(
            archive_path='a.tgz',
            target_dir='tmp',
            template_key='key',
            scheme={},
            template_values={}
        )
        bundle2 = GeneratorBundle(
            archive_path='b.tgz',
            target_dir='out',
            template_key='key2',
            scheme={'a': 'b'},
            template_values={'x': 'y'}
        )

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.archive_path, 'b.tgz')
        self.assertEqual(bundle1.target_dir, 'out')

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['archive_path'], 'b.tgz')

    def test_generator_bundle_validation_errors(self) -> None:
        '''Test GeneratorBundle validation exceptions.'''
        # Missing values (None)
        fields = {
            'archive_path': 'a.tgz',
            'target_dir': 'tmp',
            'template_key': 'key',
            'scheme': {},
            'template_values': {}
        }
        for field in fields:
            kwargs = fields.copy()
            kwargs[field] = None
            bundle = GeneratorBundle(**kwargs)
            with self.assertRaises(ATSValueError):
                bundle.validate()

        # Type errors
        type_checks = {
            'archive_path': 123,
            'target_dir': 123,
            'template_key': 123,
            'scheme': 123,
            'template_values': 123
        }
        for field, invalid_val in type_checks.items():
            kwargs = fields.copy()
            kwargs[field] = invalid_val
            bundle = GeneratorBundle(**kwargs)
            with self.assertRaises(ATSTypeError):
                bundle.validate()

    def test_tar_process_bundle(self) -> None:
        '''Test TarProcessBundle methods.'''
        bundle1 = TarProcessBundle(
            archive_path='a.tgz',
            target_dir='tmp',
            source_dir='src',
            path_replacements={},
            exclude_patterns=[],
            vals={}
        )
        bundle2 = TarProcessBundle(
            archive_path='b.tgz',
            target_dir='out',
            source_dir='src2',
            path_replacements={'x': 'y'},
            exclude_patterns=['*.py'],
            vals={'k': 'v'}
        )

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.archive_path, 'b.tgz')

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['archive_path'], 'b.tgz')

    def test_tar_process_bundle_validation_errors(self) -> None:
        '''Test TarProcessBundle validation exceptions.'''
        fields = {
            'archive_path': 'a.tgz',
            'target_dir': 'tmp',
            'source_dir': 'src',
            'path_replacements': {},
            'exclude_patterns': [],
            'vals': {}
        }
        for field in fields:
            kwargs = fields.copy()
            kwargs[field] = None
            bundle = TarProcessBundle(**kwargs)
            with self.assertRaises(ATSValueError):
                bundle.validate()

    def test_tar_process_member_bundle(self) -> None:
        '''Test TarProcessMemberBundle methods.'''
        mock_tar = MagicMock(spec=TarFile)
        mock_tar.__class__ = TarFile
        mock_member = MagicMock(spec=TarInfo)
        mock_member.__class__ = TarInfo
        bundle1 = TarProcessMemberBundle(
            tar=mock_tar,
            member=mock_member,
            dest_full_path='dest',
            vals={}
        )
        mock_tar2 = MagicMock(spec=TarFile)
        mock_tar2.__class__ = TarFile
        mock_member2 = MagicMock(spec=TarInfo)
        mock_member2.__class__ = TarInfo
        bundle2 = TarProcessMemberBundle(
            tar=mock_tar2,
            member=mock_member2,
            dest_full_path='dest2',
            vals={'x': 'y'}
        )

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.tar, mock_tar2)
        self.assertEqual(bundle1.member, mock_member2)
        self.assertEqual(bundle1.dest_full_path, 'dest2')

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['dest_full_path'], 'dest2')

    def test_tar_process_member_bundle_validation_errors(self) -> None:
        '''Test TarProcessMemberBundle validation exceptions.'''
        mock_tar = MagicMock(spec=TarFile)
        mock_tar.__class__ = TarFile
        mock_member = MagicMock(spec=TarInfo)
        mock_member.__class__ = TarInfo
        fields = {
            'tar': mock_tar,
            'member': mock_member,
            'dest_full_path': 'dest',
            'vals': {}
        }
        for field in fields:
            kwargs = fields.copy()
            kwargs[field] = None
            bundle = TarProcessMemberBundle(**kwargs)
            with self.assertRaises(ATSValueError):
                bundle.validate()


if __name__ == '__main__':
    main()
