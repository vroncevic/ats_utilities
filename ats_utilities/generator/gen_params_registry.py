# -*- coding: UTF-8 -*-

'''
Module
    gen_params_registry.py
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
    Encapsulates core runtime components for creation of generator parameters bundle.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, override

from ats_utilities.utils.iregistry import IRegistry
from ats_utilities.generator.gen_params_bundle import GenParamsBundle
from ats_utilities.generator.gen_params_params import GenParamsParams

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class GenParamsRegistry(IRegistry[GenParamsBundle, GenParamsParams]):
    '''
        Encapsulates core runtime components for creation of generator parameters bundle.

        It defines:

            :methods:
                | create_bundle - Creates a GenParamsBundle.
                | create_gen_params_bundle - Creates a GenParamsBundle.
    '''

    @classmethod
    @override
    def create_bundle(cls, params: GenParamsParams) -> GenParamsBundle:
        '''
            Creates a GenParamsBundle instance.

            :param params: Registry-specific orchestration parameters.
            :type params: GenParamsParams
            :return: GenParamsBundle instance.
            :rtype: <GenParamsBundle>
            :exceptions:
                | ATSValueError: Archive path must be provided.
                | ATSValueError: Target dir must be provided.
                | ATSValueError: Template key must be provided.
                | ATSValueError: Scheme must be provided.
                | ATSValueError: Template values must be provided.
                | ATSTypeError: Archive path must be a string.
                | ATSTypeError: Target dir must be a string.
                | ATSTypeError: Template key must be a string.
                | ATSTypeError: Scheme must be a string or a mapping.
                | ATSTypeError: Template values must be a mapping.
                | ATSValueError: Archive file does not exist.
                | ATSValueError: Scheme file does not exist.
        '''
        archive_path: str = params.get('archive_path')
        target_dir: str = params.get('target_dir')
        template_key: str = params.get('template_key')
        scheme: str | Mapping[str, str] = params.get('scheme')
        template_values: Mapping[str, str] = params.get('template_values')

        return cls.create_gen_params_bundle(
            archive_path=archive_path,
            target_dir=target_dir,
            template_key=template_key,
            scheme=scheme,
            template_values=template_values,
        )

    @classmethod
    def create_gen_params_bundle(
        cls,
        archive_path: str,
        target_dir: str,
        template_key: str,
        scheme: str | Mapping[str, str],
        template_values: Mapping[str, str]
    ) -> GenParamsBundle:
        '''
            Creates a GenParamsBundle with pre-configured components.

            :param archive_path: Path to the .tgz archive.
            :type archive_path: <str>
            :param target_dir: Directory where the project will be generated.
            :type target_dir: <str>
            :param template_key: Key for the template configuration.
            :type template_key: <str>
            :param scheme: Scheme configuration file path or dictionary.
            :type scheme: <str | Mapping[str, str]>
            :param template_values: Template values for name case variations.
            :type template_values: <Mapping[str, str]>
            :return: GenParamsBundle instance.
            :rtype: <GenParamsBundle>
            :exceptions:
                | ATSValueError: Archive path must be provided.
                | ATSValueError: Target dir must be provided.
                | ATSValueError: Template key must be provided.
                | ATSValueError: Scheme must be provided.
                | ATSValueError: Template values must be provided.
                | ATSTypeError: Archive path must be a string.
                | ATSTypeError: Target dir must be a string.
                | ATSTypeError: Template key must be a string.
                | ATSTypeError: Scheme must be a string or a mapping.
                | ATSTypeError: Template values must be a mapping.
                | ATSValueError: Archive file does not exist.
                | ATSValueError: Scheme file does not exist.
        '''
        return GenParamsBundle(
            archive_path=archive_path,
            target_dir=target_dir,
            template_key=template_key,
            scheme=scheme,
            template_values=template_values,
        )
