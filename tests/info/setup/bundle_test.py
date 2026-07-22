# -*- coding: UTF-8 -*-

'''
Module
    bundle_test.py
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
    Unit tests for InfoBundle class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from ats_utilities.context.bundle import ContextBundle
from ats_utilities.info.build_date.ibuild_date import IBuildDate
from ats_utilities.info.setup.bundle import InfoBundle
from ats_utilities.info.info_ok.iinfo_ok import IInfoOk
from ats_utilities.info.licence.ilicence import ILicence
from ats_utilities.info.log_file.ilog_file import ILogFile
from ats_utilities.info.logo.ilogo import ILogo
from ats_utilities.info.name.iname import IName
from ats_utilities.info.organization.iorganization import IOrganization
from ats_utilities.info.repository.irepository import IRepository
from ats_utilities.info.use_github.iuse_github import IUseGitHub
from ats_utilities.info.version.iversion import IVersion

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.3'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class InfoBundleTest(unittest.TestCase):
    '''
        Defines class InfoBundleTest with attribute(s) and method(s).
        Tests InfoBundle dataclass logic.
    '''

    def _get_mocks(self) -> dict[str, MagicMock]:
        return {
            "name": MagicMock(spec=IName),
            "version": MagicMock(spec=IVersion),
            "licence": MagicMock(spec=ILicence),
            "build_date": MagicMock(spec=IBuildDate),
            "repository": MagicMock(spec=IRepository),
            "organization": MagicMock(spec=IOrganization),
            "use_github": MagicMock(spec=IUseGitHub),
            "logo": MagicMock(spec=ILogo),
            "log_file": MagicMock(spec=ILogFile),
            "info_ok": MagicMock(spec=IInfoOk),
            "context_bundle": MagicMock(spec=ContextBundle),
        }

    def test_init_valid(self) -> None:
        mocks = self._get_mocks()
        bundle = InfoBundle(**mocks)
        for key, val in mocks.items():
            self.assertIs(getattr(bundle, key), val)

    def test_to_dict(self) -> None:
        mocks = self._get_mocks()
        bundle = InfoBundle(**mocks)
        self.assertEqual(bundle.to_dict(), mocks)


if __name__ == "__main__":
    unittest.main()
