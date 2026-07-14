# -*- coding: UTF-8 -*-

'''
Module
    ats_tar_processor_test.py
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
    Creates test cases for checking TarProcessor and related bundles.
Execute
    python3 -m unittest -v tests/generator/tar/ats_tar_processor_test.py
'''

from __future__ import annotations

from unittest import TestCase, main, mock
from unittest.mock import MagicMock
from tarfile import TarFile, TarInfo

from ats_utilities.generator.tar.tar_processor import TarProcessor
from ats_utilities.generator.tar.tar_process_bundle import TarProcessBundle
from ats_utilities.generator.tar.tar_process_member_bundle import TarProcessMemberBundle
from ats_utilities.exceptions import ATSGeneratorError, ATSValueError, ATSTypeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class TarProcessorTestCase(TestCase):
    '''Test cases for TarProcessor and related bundles.'''

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

    def test_process_member_not_file_or_dir(self) -> None:
        '''Test process_tar_member when it is neither directory nor file.'''
        proc = TarProcessor()
        mock_member = MagicMock()
        mock_member.isdir.return_value = False
        mock_member.isfile.return_value = False
        
        bundle = TarProcessMemberBundle(
            tar=MagicMock(),
            member=mock_member,
            dest_full_path='some_dest',
            vals={}
        )
        proc.process_tar_member(bundle)

    def test_process_member_extract_none(self) -> None:
        '''Test process_tar_member when extractfile returns None.'''
        proc = TarProcessor()
        mock_member = MagicMock()
        mock_member.isdir.return_value = False
        mock_member.isfile.return_value = True
        
        mock_tar = MagicMock()
        mock_tar.extractfile.return_value = None
        
        bundle = TarProcessMemberBundle(
            tar=mock_tar,
            member=mock_member,
            dest_full_path='some_dir/some_dest',
            vals={}
        )

        with mock.patch('ats_utilities.generator.tar.tar_processor.makedirs') as mock_makedirs:
            proc.process_tar_member(bundle)
            mock_makedirs.assert_called_once_with('some_dir', exist_ok=True)


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

    def test_tar_process_bundle_merge_type_check(self) -> None:
        '''Test that merge raises error if other is not a TarProcessBundle.'''
        bundle = TarProcessBundle(
            archive_path='a.tgz',
            target_dir='tmp',
            source_dir='src',
            path_replacements={},
            exclude_patterns=[],
            vals={}
        )
        with self.assertRaises(ATSTypeError):
            bundle.merge("not_a_tar_process_bundle")

    def test_tar_process_bundle_merge_with_none(self) -> None:
        '''Test TarProcessBundle merge with None values.'''
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
            target_dir='tmp2',
            source_dir='src2',
            path_replacements={},
            exclude_patterns=[],
            vals={}
        )
        bundle2.archive_path = None
        bundle1.merge(bundle2)
        self.assertEqual(bundle1.archive_path, 'a.tgz')


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

    def test_tar_process_member_bundle_merge_type_check(self) -> None:
        '''Test that merge raises error if other is not a TarProcessMemberBundle.'''
        mock_tar = MagicMock(spec=TarFile)
        mock_tar.__class__ = TarFile
        mock_member = MagicMock(spec=TarInfo)
        mock_member.__class__ = TarInfo
        bundle = TarProcessMemberBundle(
            tar=mock_tar,
            member=mock_member,
            dest_full_path='dest',
            vals={}
        )
        with self.assertRaises(ATSTypeError):
            bundle.merge("not_a_tar_process_member_bundle")

    def test_tar_process_member_bundle_merge_with_none(self) -> None:
        '''Test TarProcessMemberBundle merge with None values.'''
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
        bundle2 = TarProcessMemberBundle(
            tar=mock_tar,
            member=mock_member,
            dest_full_path='dest2',
            vals={}
        )
        bundle2.dest_full_path = None
        bundle1.merge(bundle2)
        self.assertEqual(bundle1.dest_full_path, 'dest')



if __name__ == '__main__':
    main()
