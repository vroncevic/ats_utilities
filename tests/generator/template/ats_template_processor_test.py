# -*- coding: UTF-8 -*-

'''
Module
    ats_template_processor_test.py
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
    Creates test cases for checking TemplateProcessor.
Execute
    python3 -m unittest -v tests/generator/template/ats_template_processor_test.py
'''

from __future__ import annotations

from unittest import TestCase, main

from ats_utilities.generator.template.template_processor import TemplateProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class TemplateProcessorTestCase(TestCase):
    '''Test cases for TemplateProcessor.'''

    def test_template_processor_binary_content(self) -> None:
        '''Test TemplateProcessor fallback for binary content.'''
        proc = TemplateProcessor()
        res = proc.render(b'\xff\xfe\xfd', {})
        self.assertEqual(res, b'\xff\xfe\xfd')


if __name__ == '__main__':
    main()
