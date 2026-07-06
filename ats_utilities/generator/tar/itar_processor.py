# -*- coding: UTF-8 -*-

'''
Module
    itar_processor.py
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
    Defines abstract class ITarProcessor with method(s).
    Interface for tar archive extraction and template rendering.
'''

from __future__ import annotations

from abc import ABC, abstractmethod

from ats_utilities.generator.tar.tar_process_bundle import TarProcessBundle
from ats_utilities.generator.tar.tar_process_member_bundle import TarProcessMemberBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ITarProcessor(ABC):
    '''
        Defines abstract class ITarProcessor with method(s).
        Interface for tar archive extraction and template rendering.

        It defines:

            :methods:
                | process_tar_member - Processes a single tar archive member.
                | process - Processes the tar archive members.
                | is_initialized - Checks if the processor is initialized.
                | __str__ - Returns the processor as string representation.
    '''

    @abstractmethod
    def process_tar_member(self, tar_process_member_bundle: TarProcessMemberBundle) -> None:
        '''
            Extracts and processes a single tar member (creates dirs or renders files).

            :param tar_process_member_bundle: Parameters defining what to do with the tar archive member.
            :type tar_process_member_bundle: <TarProcessMemberBundle>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def process(self, tar_process_bundle: TarProcessBundle) -> None:
        '''
            Processes the tar archive members.

            :param tar_process_bundle: Parameters defining what to do with the tar archive.
            :type tar_process_bundle: <TarProcessBundle>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def is_initialized(self) -> bool:
        '''
            Checks if component is initialized.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the component as string representation.

            :return: String representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
