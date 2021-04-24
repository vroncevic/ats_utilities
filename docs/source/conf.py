# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath('../../'))

project = u'ats_utilities'
copyright = u'2017, https://vroncevic.github.io/ats_utilities'
author = u'Vladimir Roncevic <elektron.ronca@gmail.com>'
version = u'1.7.5'
release = u'https://github.com/vroncevic/ats_utilities/releases'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode',]
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
    master_doc, 'ats_utilities.tex', u'ats\\_utilities Documentation',
    u'Vladimir Roncevic \\textless{}elektron.ronca@gmail.com\\textgreater{}',
    'manual'
)]
man_pages = [(
    master_doc, 'ats_utilities', u'ats_utilities Documentation', [author], 1
)]
texinfo_documents = [(
    master_doc, 'ats_utilities', u'ats_utilities Documentation',
    author, 'ats_utilities', 'One line description of project.',
    'Miscellaneous'
)]
epub_title = project
epub_exclude_files = ['search.html']
