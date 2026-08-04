# -*- coding: UTF-8 -*-

'''
Module
    files.py
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
    Defines factory file utility functions.
'''

from __future__ import annotations

from collections.abc import Sequence, Mapping
from fnmatch import fnmatch
from pathlib import Path, PurePosixPath
from re import compile, escape, Match, IGNORECASE

from ats_utilities.exceptions import ATSValueError
from ats_utilities.validation.context_error import raise_error
from ats_utilities.validation.check_type import istype

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


def check_file_exists(
    file_path: str,
    exc_context: str | None = None,
    exc_message: str | None = None,
    exc_class: type[BaseException] = ATSValueError
) -> None:
    '''
        Checks if a file exists.

        :param file_path: The path to the file.
        :param exc_context: The context representation in string format.
        :param exc_message: The message to include in the exception message.
        :param exc_class: The exception class to raise if value is None.
        :exceptions:
            | ATSTypeError: Parameter type validation failed.
            | Dynamically raises the provided exc_class (e.g., ATSValueError).
    '''
    if not file_path:
        raise_error(
            fallback_context='files::check_file_exists(...)',
            fallback_msg='the file path must be provided',
            exc_context=exc_context,
            exc_message=exc_message,
            exc_class=exc_class
        )

    istype(file_path, str, exc_context, exc_message)

    if not Path(file_path).exists():
        raise_error(
            fallback_context='files::check_file_exists(...)',
            fallback_msg=f'the file at the provided path does not exist: {file_path}',
            exc_context=exc_context,
            exc_message=exc_message,
            exc_class=exc_class
        )


def normalize_path(
    file_path: str,
    exc_context: str | None = None,
    exc_message: str | None = None,
    exc_class: type[BaseException] = ATSValueError
) -> str:
    '''
        Normalizes file paths and strips leading directory prefixes.

        :param file_path: The original path to clean up.
        :param exc_context: The context representation in string format.
        :param exc_message: The message to include in the exception message.
        :param exc_class: The exception class to raise if file_path is None.
        :return: The cleaned up relative path.
        :exceptions:
            | ATSTypeError: Parameter type validation failed.
            | Dynamically raises the provided exc_class (e.g., ATSValueError).
    '''
    if not file_path:
        raise_error(
            fallback_context='files::normalize_path(...)',
            fallback_msg='the file path must be provided',
            exc_context=exc_context,
            exc_message=exc_message,
            exc_class=exc_class
        )

    istype(file_path, str, exc_context, exc_message)

    path_obj = PurePosixPath(file_path.replace('\\', '/'))

    if path_obj.drive:
        path_obj = PurePosixPath(*path_obj.parts[1:])

    clean_file_path = path_obj.as_posix()

    if clean_file_path.startswith('/'):
        clean_file_path = clean_file_path[1:]

    return clean_file_path


def resolve_relative_path(
    normalized_name: str,
    source_dir_clean: str,
    exc_context: str | None = None,
    exc_message: str | None = None,
    exc_class: type[BaseException] = ATSValueError
) -> str | None:
    '''
        Calculates relative path to the specified source directory.

        :param normalized_name: The cleaned name of the archive member.
        :param source_dir_clean: The cleaned source directory name.
        :param exc_context: The context representation in string format.
        :param exc_message: The message to include in the exception message.
        :param exc_class: The exception class to raise if value is None.
        :return: The relative path inside the source dir, or None if not matching.
        :exceptions:
            | ATSTypeError: Parameter type validation failed.
            | Dynamically raises the provided exc_class (e.g., ATSValueError).
    '''
    istype(normalized_name, str, exc_context, exc_message)
    istype(source_dir_clean, str, exc_context, exc_message)

    if not normalized_name:
        raise_error(
            fallback_context='files::resolve_relative_path(...)',
            fallback_msg='the normalized name must be provided',
            exc_context=exc_context,
            exc_message=exc_message,
            exc_class=exc_class
        )

    if not source_dir_clean:
        raise_error(
            fallback_context='files::resolve_relative_path(...)',
            fallback_msg='the source directory name must be provided',
            exc_context=exc_context,
            exc_message=exc_message,
            exc_class=exc_class
        )

    if normalized_name == source_dir_clean:
        return ''

    try:
        target = PurePosixPath(normalized_name)
        base = PurePosixPath(source_dir_clean)
        
        return target.relative_to(base).as_posix()

    except ValueError:
        return None


def is_excluded_path(
    rel_path: str,
    exclude_patterns: Sequence[str],
    exc_context: str | None = None,
    exc_message: str | None = None,
    exc_class: type[BaseException] = ATSValueError
) -> bool:
    '''
        Checks if a relative path matches any exclusion patterns.

        :param rel_path: The relative path to inspect.
        :param exclude_patterns: The sequence of glob patterns to exclude.
        :param exc_context: The context representation in string format.
        :param exc_message: The message to include in the exception message.
        :param exc_class: The exception class to raise if value is None.
        :return: True if the path should be excluded, False otherwise.
        :exceptions:
            | ATSTypeError: Parameter type validation failed.
            | Dynamically raises the provided exc_class (e.g., ATSValueError).
    '''
    if not rel_path:
        raise_error(
            fallback_context='files::is_excluded_path(...)',
            fallback_msg='the relative path must be provided',
            exc_context=exc_context,
            exc_message=exc_message,
            exc_class=exc_class
        )

    if not exclude_patterns:
        raise_error(
            fallback_context='files::is_excluded_path(...)',
            fallback_msg='the exclude patterns must be provided',
            exc_context=exc_context,
            exc_message=exc_message,
            exc_class=exc_class
        )

    istype(rel_path, str, exc_context, exc_message)
    istype(exclude_patterns, Sequence, exc_context, exc_message)

    path_obj = Path(rel_path)
    parts = path_obj.parts

    for pattern in exclude_patterns:
        posix_path = path_obj.as_posix()

        if fnmatch(posix_path, pattern) or any(fnmatch(part, pattern) for part in parts):
            return True

    return False


def format_casing_by_match(
    clean_str: str,
    default_val: str,
    upper_val: str,
    camel_val: str,
    dashed_val: str,
    exc_context: str | None = None,
    exc_message: str | None = None,
    exc_class: type[BaseException] = ATSValueError
) -> str:
    '''
        Formats a replacement value according to the casing style matched in clean_str.

        :param clean_str: The cleaned matched substring to analyze.
        :param default_val: The default replacement value.
        :param upper_val: The value in UPPER_CASE.
        :param camel_val: The value in CamelCase/PascalCase.
        :param dashed_val: The value in dashed-case.
        :param exc_context: The context representation in string format.
        :param exc_message: The message to include in the exception message.
        :param exc_class: The exception class to raise if value is None.
        :return: The replacement formatted in matching casing style.
        :exceptions:
            | ATSTypeError: Parameter type validation failed.
            | Dynamically raises the provided exc_class (e.g., ATSValueError).
    '''
    if not clean_str:
        raise_error(
            fallback_context='files::format_casing_by_match(...)',
            fallback_msg='the clean string must be provided',
            exc_context=exc_context,
            exc_message=exc_message,
            exc_class=exc_class
        )

    if not default_val:
        raise_error(
            fallback_context='files::format_casing_by_match(...)',
            fallback_msg='the default value must be provided',
            exc_context=exc_context,
            exc_message=exc_message,
            exc_class=exc_class
        )

    if not upper_val:
        raise_error(
            fallback_context='files::format_casing_by_match(...)',
            fallback_msg='the UPPERCASE value must be provided',
            exc_context=exc_context,
            exc_message=exc_message,
            exc_class=exc_class
        )

    if not camel_val:
        raise_error(
            fallback_context='files::format_casing_by_match(...)',
            fallback_msg='the camelCase/PascalCase value must be provided',
            exc_context=exc_context,
            exc_message=exc_message,
            exc_class=exc_class
        )

    if not dashed_val:
        raise_error(
            fallback_context='files::format_casing_by_match(...)',
            fallback_msg='the dashed-case value must be provided',
            exc_context=exc_context,
            exc_message=exc_message,
            exc_class=exc_class
        )

    istype(clean_str, str, exc_context, exc_message)
    istype(default_val, str, exc_context, exc_message)
    istype(upper_val, str, exc_context, exc_message)
    istype(camel_val, str, exc_context, exc_message)
    istype(dashed_val, str, exc_context, exc_message)

    if clean_str.isupper():
        return upper_val
    elif clean_str and clean_str[0].isupper():
        return camel_val
    elif '-' in clean_str:
        return dashed_val
    else:
        return default_val


def write_content(
    file_path: str,
    content: str | bytes,
    exc_context: str | None = None,
    exc_message: str | None = None,
    exc_class: type[BaseException] = ATSValueError
) -> None:
    '''
        Writes string or bytes content to a file.

        :param file_path: The path to the target file.
        :param content: The text string or raw bytes to write.
        :param exc_context: The context representation in string format.
        :param exc_message: The message to include in the exception message.
        :param exc_class: The exception class to raise if value is None.
        :exceptions:
            | ATSTypeError: Parameter type validation failed.
            | Dynamically raises the provided exc_class (e.g., ATSValueError).
    '''
    if not file_path:
        raise_error(
            fallback_context='files::write_content(...)',
            fallback_msg='the file path must be provided',
            exc_context=exc_context,
            exc_message=exc_message,
            exc_class=exc_class
        )

    if not content:
        raise_error(
            fallback_context='files::write_content(...)',
            fallback_msg='the content must be provided',
            exc_context=exc_context,
            exc_message=exc_message,
            exc_class=exc_class
        )

    istype(file_path, str, exc_context, exc_message)
    istype(content, (str, bytes), exc_context, exc_message)

    target_path = Path(file_path)
    target_path.parent.mkdir(parents=True, exist_ok=True)

    if isinstance(content, str):
        target_path.write_text(content, encoding='utf-8')
    else:
        target_path.write_bytes(content)


def apply_path_replacements(
    rel_path: str,
    path_replacements: Mapping[str, str],
    vals: Mapping[str, str],
    exc_context: str | None = None,
    exc_message: str | None = None,
    exc_class: type[BaseException] = ATSValueError
) -> str:
    '''
        Applies path replacements to a relative path using casing heuristics.

        :param rel_path: The original relative path.
        :param path_replacements: The string replacements mapping.
        :param vals: The computed template values.
        :param exc_context: The context representation in string format.
        :param exc_message: The message to include in the exception message.
        :param exc_class: The exception class to raise if value is None.
        :return: The replaced relative path.
        :exceptions:
            | ATSTypeError: Parameter type validation failed.
            | Dynamically raises the provided exc_class (e.g., ATSValueError).
    '''
    if not rel_path:
        raise_error(
            fallback_context='files::apply_path_replacements(...)',
            fallback_msg='the relative path must be provided',
            exc_context=exc_context,
            exc_message=exc_message,
            exc_class=exc_class
        )

    if not path_replacements:
        raise_error(
            fallback_context='files::apply_path_replacements(...)',
            fallback_msg='the path replacements must be provided',
            exc_context=exc_context,
            exc_message=exc_message,
            exc_class=exc_class
        )

    if not vals:
        raise_error(
            fallback_context='files::apply_path_replacements(...)',
            fallback_msg='the vals must be provided',
            exc_context=exc_context,
            exc_message=exc_message,
            exc_class=exc_class
        )

    istype(rel_path, str, exc_context, exc_message)
    istype(path_replacements, Mapping, exc_context, exc_message)
    istype(vals, Mapping, exc_context, exc_message)

    dest_rel_path = rel_path

    for old_str, var_name in path_replacements.items():
        replacement_val = vals.get(var_name)

        if replacement_val is None:
            continue

        words = [w for w in old_str.replace('-', '_').split('_') if w]

        if not words:
            dest_rel_path = dest_rel_path.replace(old_str, replacement_val)
            continue

        pattern_str = r'[-_]?'.join(escape(w) for w in words)
        pattern = compile(rf'\b{pattern_str}\b', IGNORECASE)

        def replace_match(match: Match) -> str:
            clean_str = match.group(0).lstrip('-_')

            return format_casing_by_match(
                clean_str=clean_str,
                default_val=replacement_val,
                upper_val=vals.get(f'{var_name}_upper', replacement_val.upper()),
                camel_val=vals.get(f'{var_name}_camel', replacement_val),
                dashed_val=vals.get(f'{var_name}_dashed', replacement_val.replace('_', '-')),
                exc_context=exc_context
            )

        dest_rel_path = pattern.sub(replace_match, dest_rel_path)

    return dest_rel_path
