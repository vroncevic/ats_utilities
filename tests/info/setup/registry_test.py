# -*- coding: UTF-8 -*-

'''
Module
    registry_test.py
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
    Unit tests for InfoRegistry class.
'''

from __future__ import annotations

import unittest

from ats_utilities.context.factory import ContextFactory
from ats_utilities.info.setup.bundle import InfoBundle
from ats_utilities.info.setup.registry import InfoRegistry
from ats_utilities.info.setup.dependencies import InfoDependencies
from ats_utilities.info.setup.factory import InfoFactory

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class InfoRegistryTest(unittest.TestCase):
    '''
        Defines class InfoRegistryTest with attribute(s) and method(s).
        Tests InfoRegistry logic.
    '''

    def test_create_bundle(self) -> None:
        context_bundle = ContextFactory.create_default_bundle()
        info_data = {
            'ats_name': 'ats_utilities',
            'ats_version': '3.4.4',
            'ats_licence': 'GPLv3',
            'ats_build_date': '2026-07-18',
            'ats_repository': 'https://github.com/vroncevic/ats_utilities',
            'ats_organization': 'vroncevic',
            'ats_use_github_infrastructure': 'True',
            'ats_logo_path': '/path/to/logo.png',
            'ats_log_file': '/path/to/run.log',
            'ats_info_ok': True
        }
        # Build components using Factory
        factory_bundle = InfoFactory.create_info_bundle_from_dict(info_data, context_bundle)

        params = InfoDependencies(
            context_bundle=context_bundle,
            name=factory_bundle.name,
            version=factory_bundle.version,
            licence=factory_bundle.licence,
            build_date=factory_bundle.build_date,
            repository=factory_bundle.repository,
            organization=factory_bundle.organization,
            use_github=factory_bundle.use_github,
            logo=factory_bundle.logo,
            log_file=factory_bundle.log_file,
            info_ok=factory_bundle.info_ok
        )
        bundle = InfoRegistry.create_bundle(params)
        self.assertIsInstance(bundle, InfoBundle)
        self.assertEqual(bundle.name.name, 'ats_utilities')


if __name__ == "__main__":
    unittest.main()
