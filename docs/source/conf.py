# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath('../../'))

project = 'ats_utilities'
copyright = '2017, https://vroncevic.github.io/ats_utilities'
author = 'Vladimir Roncevic <elektron.ronca@gmail.com>'
version = '2.4.5'
release = 'https://github.com/vroncevic/ats_utilities/releases'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', ]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = []
pygments_style = None
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
htmlhelp_basename = 'ats_utilitiesdoc'
latex_elements = {}
latex_documents = [(
    master_doc, 'ats_utilities.tex', 'ats\\_utilities Documentation',
    'Vladimir Roncevic \\textless{}elektron.ronca@gmail.com\\textgreater{}',
    'manual'
)]
man_pages = [(
    master_doc, 'ats_utilities', 'ats_utilities Documentation', [author], 1
)]
texinfo_documents = [(
    master_doc, 'ats_utilities', 'ats_utilities Documentation',
    author, 'ats_utilities', 'One line description of project.',
    'Miscellaneous'
)]
epub_title = project
epub_exclude_files = ['search.html']
