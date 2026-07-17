# -*- coding: UTF-8 -*-

'''
Module
    tar_process_member_registry.py
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
    Encapsulates core runtime components for creation of tar process member bundle.
'''

from __future__ import annotations

from collections.abc import Mapping
from tarfile import TarFile, TarInfo

from ats_utilities.generator.tar.tar_process_member_bundle import TarProcessMemberBundle

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class TarProcessRegistry:
    '''
        Encapsulates core runtime components for creation of tar process member bundle.

        It defines:

            :methods:
                | create_tar_process_member_bundle - Creates a TarProcessMemberBundle.
    '''

    @classmethod
    def create_tar_process_member_bundle(
        cls,
        tar: TarFile,
        member: TarInfo,
        dest_full_path: str,
        vals: Mapping[str, str]
    ) -> TarProcessMemberBundle:
        '''
            Creates a TarProcessMemberBundle with pre-configured components.

            :param tar: Tar file.
            :type tar: <TarFile>
            :param member: Tar member information.
            :type member: <TarInfo>
            :param dest_full_path: Absolute destination file path.
            :type dest_full_path: <str>
            :param vals: Computed template values for substitution.
            :type vals: <Mapping[str, str]>
            :return: TarProcessMemberBundle instance.
            :rtype: <TarProcessMemberBundle>
            :exceptions:
                | ATSValueError: tar must be provided.
                | ATSValueError: member must be provided.
                | ATSValueError: dest_full_path must be provided.
                | ATSValueError: vals must be provided.
                | ATSTypeError: tar must be a TarFile instance.
                | ATSTypeError: member must be a TarInfo instance.
                | ATSTypeError: dest_full_path must be a string.
                | ATSTypeError: vals must be a mapping.
        '''
        return TarProcessMemberBundle(
            tar=tar,
            member=member,
            dest_full_path=dest_full_path,
            vals=vals,
        )
