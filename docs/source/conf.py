# -*- coding: utf-8 -*-

'''
Module
    conf.py
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
    Defines configuration for ats_utilities sphinx-doc.
'''

import sys
from os.path import abspath
from typing import Any

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Updated'

sys.path.insert(0, abspath('../../'))

project: str = 'ats_utilities'
project_copyright: str = '2026, https://vroncevic.github.io/ats_utilities'
author: str = 'Vladimir Roncevic <elektron.ronca@gmail.com>'
version: str = '3.4.2'
release: str = 'https://github.com/vroncevic/ats_utilities/releases'
extensions: list[str] = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', ]
templates_path: list[str] = ['_templates']
source_suffix: str = '.rst'
master_doc: str = 'index'
language: str = 'en'
html_static_path: list[str] = ['_static']
exclude_patterns: list[str] = []
pygments_style: str = 'sphinx'
html_theme: str = 'classic'
html_static_path: list[str] = ['_static']
htmlhelp_basename: str = 'ats_utilitiesdoc'
latex_elements: dict[Any, Any] = {}
latex_documents: list[tuple[Any, ...]] = [(
    master_doc, 'ats_utilities.tex', 'ats\\_utilities Documentation',
    'Vladimir Roncevic \\textless{}elektron.ronca@gmail.com\\textgreater{}',
    'manual'
)]
man_pages: list[tuple[Any, ...]] = [(
    master_doc, 'ats_utilities', 'ats_utilities Documentation', [author], 1
)]
texinfo_documents: list[tuple[Any, ...]] = [(
    master_doc, 'ats_utilities', 'ats_utilities Documentation',
    author, 'ats_utilities', 'One line description of project.',
    'Miscellaneous'
)]
epub_title: str = project
epub_exclude_files: list[str] = ['search.html']
