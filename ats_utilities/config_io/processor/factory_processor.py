# -*- coding: UTF-8 -*-

'''
Module
    factory_processor.py
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
    Defines class ConfigProcessorFactory with attribute(s) and method(s).
    Creates an API for creating an file processor instance based on the file extension.
    1th level of configuration loader/storer implementation.
'''

from __future__ import annotations

from collections.abc import Mapping
from typing import override
from pathlib import Path

from ats_utilities.config_io.processor.ifactory_processor import IConfigProcessorFactory
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor
from ats_utilities.config_io.processor.cfg_processor import CFGProcessor
from ats_utilities.config_io.processor.ini_processor import INIProcessor
from ats_utilities.config_io.processor.json_processor import JSONProcessor
from ats_utilities.config_io.processor.xml_processor import XMLProcessor
from ats_utilities.config_io.processor.yaml_processor import YAMLProcessor
from ats_utilities.utils.files import check_file_exists
from ats_utilities.utils.component import make_component, validate_component
from ats_utilities.validation.check_value import not_none, not_satisfied
from ats_utilities.validation.check_type import istype

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


class ConfigProcessorFactory(IConfigProcessorFactory):
    '''
        Defines class ConfigProcessorFactory with attribute(s) and method(s).
        Creates an API for creating an file processor instance based on the file extension.
        1th level of configuration loader/storer implementation.

        It defines:

            :attributes:
                | _PROCESSOR_MAP - Mapping of file extensions to processor classes.
            :methods:
                | get_processor_class - Returns the processor class for a specific file extension.
                | create_from_extension - Creates a processor instance based on a raw extension string.
                | create_from_file_path - Creates a processor instance based on a file path.
    '''

    _PROCESSOR_MAP: Mapping[str, type[IConfigProcessor]] = {
        '.cfg': CFGProcessor,
        '.ini': INIProcessor,
        '.json': JSONProcessor,
        '.xml': XMLProcessor,
        '.yml': YAMLProcessor,
        '.yaml': YAMLProcessor
    }

    @classmethod
    @override
    def get_processor_class(cls, extension: str) -> type[IConfigProcessor]:
        '''
            Returns the processor class for a specific file extension.

            :param extension: File extension (e.g., '.json', '.cfg', '.xml', '.ini', '.yml', '.yaml').
            :type extension: <str>
            :return: Processor class.
            :rtype: <type[IConfigProcessor]>
            :exceptions:
                | ATSValueError: Extension must be provided.
                | ATSTypeError: Extension must be a string.
                | ATSValueError: Extension is not supported.
        '''
        not_none(extension, r'extension must be provided')
        istype(extension, str, r'extension must be a string')

        formatted_ext: str = extension.lower()

        if not formatted_ext.startswith('.'):
            formatted_ext = f'.{formatted_ext}'

        not_satisfied(
            formatted_ext not in cls._PROCESSOR_MAP.keys(), f'The extension {extension} is not supported'
        )

        return cls._PROCESSOR_MAP[formatted_ext]

    @classmethod
    @override
    def create_from_extension(
        cls, 
        extension: str | None = None,
        scheme: Mapping[str, str] | None = None,
        processor: IConfigProcessor | None = None
    ) -> IConfigProcessor:
        '''
            Creates a processor instance based on a raw extension string.
            Uses get_processor_class utility.
            Uses make_component and validate_component utilities.

            :param extension: File extension (e.g., '.json', '.cfg', '.xml', '.ini', '.yml', '.yaml') | None.
            :type extension: <str | None>
            :param scheme: Scheme for the processor | None.
            :type scheme: <Mapping[str, str] | None>
            :param processor: Instance to be used as the processor | None.
            :type processor: <IConfigProcessor | None>
            :return: Processor instance.
            :rtype: <IConfigProcessor>
            :exceptions:
                | ATSValueError: Extension must be provided.
                | ATSTypeError: Extension must be a string.
                | ATSValueError: Extension is not supported.
                | ATSTypeError: Validation of processor instance failed.
        '''
        if processor is not None:
            validate_component(
                instance=processor,
                expected_class=IConfigProcessor,
                exc_message=r'The provided processor must implement IConfigProcessor'
            )

            return processor

        processor_class = cls.get_processor_class(extension)

        resolved_processor = make_component(
            passed_obj=processor,
            default_class=processor_class,
            factory_args={'scheme': scheme} if scheme else None
        )

        validate_component(
            instance=resolved_processor,
            expected_class=IConfigProcessor,
            exc_message=f'The processor for extension {extension} must implement IConfigProcessor'
        )

        return resolved_processor

    @classmethod
    @override
    def create_from_file_path(
        cls, 
        file_path: str | None = None,
        scheme: Mapping[str, str] | None = None,
        processor: IConfigProcessor | None = None
    ) -> IConfigProcessor:
        '''
            Creates a processor instance based on a file path.
            Uses create_from_extension method.
            Note: If processor provided, it is returned immediately.
            If processor is not provided, creation is done from the file path extension.

            :param file_path: Path to the configuration file | None.
            :type file_path: <str | None>
            :param scheme: Scheme for the processor | None.
            :type scheme: <Mapping[str, str] | None>
            :param processor: Instance to be used as the processor | None.
            :type processor: <IConfigProcessor | None>
            :return: Processor instance.
            :rtype: <IConfigProcessor>
            :exceptions:
                | ATSValueError: File path must be provided when processor is None.
                | ATSTypeError: File path must be a string.
                | ATSValueError: File does not exist.
                | ATSValueError: Extension must be provided.
                | ATSTypeError: Extension must be a string.
                | ATSValueError: Extension is not supported.
                | ATSTypeError: Validation of processor instance failed.
        '''
        if processor is not None:
            return cls.create_from_extension(processor=processor)

        not_none(file_path, r'file_path must be provided when processor is None')
        istype(file_path, str, r'file_path must be a string')
        check_file_exists(file_path, f'file at {file_path} does not exist')

        return cls.create_from_extension(
            extension=Path(file_path).suffix,
            scheme=scheme,
            processor=processor
        )
