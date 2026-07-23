# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
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
    Unit tests for ProjectFactory class.
'''

from __future__ import annotations

import unittest

from ats_utilities.context.factory import ContextFactory
from ats_utilities.generator.project.setup.bundle import ProjectBundle
from ats_utilities.generator.project.setup.factory import ProjectFactory
from ats_utilities.generator.project.setup.dependencies import ProjectOptions

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ProjectFactoryTest(unittest.TestCase):
    '''
        Defines class ProjectFactoryTest with attribute(s) and method(s).
        Tests ProjectFactory static factory logic.
    '''

    def test_create_default_project_bundle(self) -> None:
        '''Tests create_default_project_bundle.'''
        setup = {
            "pro_name": "my_test_project",
            "pro_config": {"key": "val"},
            "template_dir": "/tmp/templates"
        }
        context_bundle = ContextFactory.create_default_bundle()

        bundle = ProjectFactory.create_default_project_bundle(
            setup=setup,
            context_bundle=context_bundle
        )

        self.assertIsInstance(bundle, ProjectBundle)
        self.assertEqual(bundle.pro_name.pro_name, "my_test_project")
        self.assertEqual(bundle.pro_config.config, {"key": "val"})
        self.assertEqual(bundle.template_dir.template_dir, "/tmp/templates")
        self.assertIs(bundle.context_bundle, context_bundle)

    def test_create_default_project_setup_bundle_compat(self) -> None:
        '''Tests create_default_project_setup_bundle compatibility wrapper.'''
        setup = {
            "pro_name": "my_test_project2",
            "pro_config": {"key2": "val2"},
            "template_dir": "/tmp/templates2"
        }
        context_bundle = ContextFactory.create_default_bundle()

        bundle = ProjectFactory.create_default_project_setup_bundle(
            setup=setup,
            context_bundle=context_bundle
        )

        self.assertIsInstance(bundle, ProjectBundle)
        self.assertEqual(bundle.pro_name.pro_name, "my_test_project2")
        self.assertEqual(bundle.pro_config.config, {"key2": "val2"})
        self.assertEqual(bundle.template_dir.template_dir, "/tmp/templates2")
        self.assertIs(bundle.context_bundle, context_bundle)

    def test_create_default_bundle(self) -> None:
        '''Tests create_default_bundle.'''
        setup = {
            "pro_name": "my_test_project",
            "pro_config": {"key": "val"},
            "template_dir": "/tmp/templates"
        }
        context_bundle = ContextFactory.create_default_bundle()

        bundle = ProjectFactory.create_default_bundle(
            ProjectOptions(setup=setup, context_bundle=context_bundle)
        )

        self.assertIsInstance(bundle, ProjectBundle)
        self.assertEqual(bundle.pro_name.pro_name, "my_test_project")
        self.assertEqual(bundle.pro_config.config, {"key": "val"})
        self.assertEqual(bundle.template_dir.template_dir, "/tmp/templates")
        self.assertIs(bundle.context_bundle, context_bundle)


if __name__ == "__main__":
    unittest.main()
