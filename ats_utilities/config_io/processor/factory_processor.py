# -*- coding: UTF-8 -*-

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Any

from ats_utilities.factory_component import make_component, validate_component
from ats_utilities.config_io.processor.iconfig_processor import IConfigProcessor
from ats_utilities.config_io.processor.cfg_processor import CFGProcessor
from ats_utilities.config_io.processor.ini_processor import INIProcessor
from ats_utilities.config_io.processor.json_processor import JSONProcessor
from ats_utilities.config_io.processor.xml_processor import XMLProcessor
from ats_utilities.config_io.processor.yaml_processor import YAMLProcessor


class ConfigProcessorFactory:
    '''
    Factory class to instantiate the appropriate IConfigProcessor 
    based on the file extension.
    '''

    # Mapiramo ekstenzije fajlova direktno na klase procesora
    _PROCESSOR_MAP: Mapping[str, type[IConfigProcessor]] = {
        '.cfg': CFGProcessor,
        '.ini': INIProcessor,
        '.json': JSONProcessor,
        '.xml': XMLProcessor,
        '.yml': YAMLProcessor,
        '.yaml': YAMLProcessor
    }

    @classmethod
    def register_processor(cls, extension: str, processor_class: type[IConfigProcessor]) -> None:
        '''
        Registers a new processor class for a specific file extension.
        '''
        formatted_ext = extension.lower()
        if not formatted_ext.startswith('.'):
            formatted_ext = f'.{formatted_ext}'
            
        cls._processors[formatted_ext] = processor_class

    @classmethod
    def create_from_extension(
        cls, 
        extension: str, 
        scheme: Mapping[str, str] | None = None,
        existing_instance: IConfigProcessor | None = None
    ) -> IConfigProcessor:
        '''
        Creates a processor instance based on a raw extension string.
        Uses make_component and validate_component helper utilities.
        '''
        formatted_ext = extension.lower()
        if not formatted_ext.startswith('.'):
            formatted_ext = f'.{formatted_ext}'

        # 1. Pronalaženje odgovarajuće klase u mapi registrovanih
        processor_class = cls._processors.get(formatted_ext)

        if processor_class is None and existing_instance is None:
            raise ValueError(
                f"Unsupported configuration extension: {extension}. "
                f"Please register a compatible IConfigProcessor first."
            )

        # 2. Kreiranje komponente pomoću make_component helpera
        # Ako je prosleđen existing_instance, on će samo biti vraćen.
        # U suprotnom, pravi se nova instanca processor_class sa 'scheme' argumentom.
        resolved_processor = make_component(
            passed_obj=existing_instance,
            default_class=processor_class,
            factory_args={'scheme': scheme} if scheme else None
        )

        # 3. Validacija komponente pomoću validate_component helpera
        # Osiguravamo da kreirani objekat uvek nasleđuje IConfigProcessor interfejs.
        validate_component(
            instance=resolved_processor,
            expected_class=IConfigProcessor,
            exc_message=f"The resolved processor for extension '{extension}' must implement IConfigProcessor"
        )

        return resolved_processor

    @classmethod
    def create_from_file_path(
        cls, 
        file_path: str | Path, 
        scheme: Mapping[str, str] | None = None,
        existing_instance: IConfigProcessor | None = None
    ) -> IConfigProcessor:
        '''
        Helper method to automatically extract the extension from a file path
        and build the appropriate config processor.
        '''
        path = Path(file_path)
        return cls.create_from_extension(
            extension=path.suffix, 
            scheme=scheme, 
            existing_instance=existing_instance
        )
