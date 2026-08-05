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
    Defines the ConfigProcessorFactory class with attribute(s) and method(s).
    Provides an API for creating an file processor instance based on the file extension.
    1th level of configuration loader/storer implementation.
'''

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

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

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class ConfigProcessorFactory:
    '''
        Defines the ConfigProcessorFactory class with attribute(s) and method(s).
        Provides an API for creating an file processor instance based on the file extension.
        1th level of configuration loader/storer implementation.

        It defines:

            :attributes:
                | _PROCESSOR_MAP - The mapping of file extensions to processor classes.
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
    def get_processor_class(cls, extension: str) -> type[IConfigProcessor]:
        '''
            Returns the processor class for a specific file extension.

            :param extension: The file extension (e.g., '.json', '.cfg', '.xml', '.ini', '.yml', '.yaml').
            :return: The processor class.
            :exceptions:
                | ATSValueError: The extension must be provided.
                | ATSTypeError:  The extension must be a string.
                | ATSValueError: The extension is not supported.
        '''
        ctx: str = 'config_processor_factory::get_processor_class(...)'
        msg_ext_none: str = 'the extension must be provided.'
        msg_ext_istype: str = 'the extension must be a string.'
        msg_ext_unsupported: str = f'the extension {extension} is not supported'

        not_none(extension, ctx, msg_ext_none)
        istype(extension, str, ctx, msg_ext_istype)

        formatted_ext: str = extension.lower()

        if not formatted_ext.startswith('.'):
            formatted_ext = f'.{formatted_ext}'

        not_satisfied(
            formatted_ext not in cls._PROCESSOR_MAP.keys(), ctx, msg_ext_unsupported
        )

        return cls._PROCESSOR_MAP[formatted_ext]

    @classmethod
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

            :param extension: The file extension (e.g., '.json', '.cfg', '.xml', '.ini', '.yml', '.yaml') | None.
            :param scheme: Scheme for the processor | None.
            :param processor: Instance to be used as the processor | None.
            :return: The processor.
            :exceptions:
                | ATSValueError: The extension must be provided.
                | ATSTypeError:  The extension must be a string.
                | ATSValueError: The extension is not supported.
                | ATSTypeError:  The validation of the processor instance failed.
        '''
        ctx: str = 'config_processor_factory::create_from_extension(...)'
        msg_processor_none: str = 'the provided processor must implement IConfigProcessor'
        msg_processor_istype: str = f'the processor for extension {extension} must implement IConfigProcessor'

        if processor is not None:
            validate_component(
                instance=processor,
                expected_class=IConfigProcessor,
                exc_context=ctx,
                exc_message=msg_processor_none
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
            exc_context=ctx, 
            exc_message=msg_processor_istype
        )

        return resolved_processor

    @classmethod
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
            :param scheme: Scheme for the processor | None.
            :param processor: Instance to be used as the processor | None.
            :return: The processor.
            :exceptions:
                | ATSValueError: The file path must be provided when the processor is None.
                | ATSTypeError:  The file path must be a string.
                | ATSValueError: The file does not exist.
                | ATSValueError: The extension must be provided.
                | ATSTypeError:  The extension must be a string.
                | ATSValueError: The extension is not supported.
                | ATSTypeError:  The validation of the processor instance failed.
        '''
        if processor is not None:
            return cls.create_from_extension(processor=processor)

        ctx: str = 'config_processor_factory::create_from_file_path(...)'
        file_path_none: str = 'the file path must be provided when the processor is None'
        file_path_str: str = 'the file path must be a string'
        file_does_not_exist: str = f'the file at {file_path} does not exist'

        not_none(file_path, ctx, file_path_none)
        istype(file_path, str, ctx, file_path_str)
        check_file_exists(file_path, ctx, file_does_not_exist)

        return cls.create_from_extension(
            extension=Path(file_path).suffix,
            scheme=scheme,
            processor=processor
        )
