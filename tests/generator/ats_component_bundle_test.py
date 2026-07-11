# -*- coding: UTF-8 -*-

'''
Module
    ats_component_bundle_test.py
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
    Creates test cases for checking GeneratorComponentBundle.
Execute
    python3 -m unittest -v tests/generator/ats_component_bundle_test.py
'''

from __future__ import annotations

from unittest import TestCase, main
from unittest.mock import MagicMock

from ats_utilities.context_bundle import ContextBundle
from ats_utilities.generator.component_bundle import GeneratorComponentBundle
from ats_utilities.generator.scheme.ischeme_loader import ISchemeLoader
from ats_utilities.generator.tar.itar_processor import ITarProcessor
from ats_utilities.generator.template.itemplate_processor import ITemplateProcessor
from ats_utilities.exceptions import ATSValueError, ATSTypeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '1.0.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class GeneratorComponentBundleTestCase(TestCase):
    '''Test cases for GeneratorComponentBundle.'''

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

    def test_generator_component_bundle_merge_type_check(self) -> None:
        '''Test that merge raises error if other is not a GeneratorComponentBundle.'''
        bundle = GeneratorComponentBundle()
        with self.assertRaises(ATSTypeError):
            bundle.merge("not_a_generator_component_bundle")

    def test_generator_component_bundle_merge_with_none(self) -> None:
        '''Test GeneratorComponentBundle merge with None values.'''
        bundle1 = GeneratorComponentBundle()
        bundle2 = GeneratorComponentBundle()
        bundle2.scheme_loader = None
        bundle1.merge(bundle2)
        self.assertIsNotNone(bundle1.scheme_loader)



if __name__ == '__main__':
    main()
