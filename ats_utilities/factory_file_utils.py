# -*- coding: UTF-8 -*-

'''
Module
    factory_file_utils.py
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
from os.path import normpath
from pathlib import Path, PurePosixPath
from re import compile, escape, Match, IGNORECASE

from ats_utilities.exceptions import ATSValueError
from ats_utilities.factory_context_error import raise_context_error
from ats_utilities.factory_type import check_type

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.2'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


def check_file_exists(
    file_path: str,
    exc_message: str | None = None,
    exception_class: type[Exception] = ATSValueError
) -> None:
    '''
        Checks if a file exists.

        :param file_path: Path to the file.
        :type file_path: <str>
        :param exc_message: Message to include in the exception message.
        :type exc_message: <str | None>
        :param exception_class: The exception class to raise if value is None.
        :type exception_class: <type[Exception]> (default ATSValueError)
        :exceptions:
            | ATSTypeError: Parameter type validation failed.
            | Dynamically raises the provided exception_class (e.g., ATSValueError).
    '''
    if not file_path:
        raise_context_error(
            fallback_prefix=r'factory_file_utils::check_file_exists',
            fallback_msg=r'file path must be provided',
            exc_message=exc_message,
            exception_class=exception_class,
            depth=3
        )

    check_type(file_path, str, exc_message)

    if not Path(file_path).exists():
        raise_context_error(
            fallback_prefix=r'factory_file_utils::check_file_exists',
            fallback_msg=f'file at the provided path does not exist: {file_path}',
            exc_message=exc_message,
            exception_class=exception_class,
            depth=3
        )


def normalize_path(
    file_path: str,
    exc_message: str | None = None,
    exception_class: type[Exception] = ATSValueError
) -> str:
    '''
        Normalizes file paths and strips leading directory prefixes.

        :param file_path: The original path to clean up.
        :type file_path: <str>
        :param exc_message: Message to include in the exception message.
        :type exc_message: <str | None>
        :param exception_class: The exception class to raise if file_path is None.
        :type exception_class: <type[Exception]> (default ATSValueError)
        :return: The cleaned up relative path.
        :rtype: <str>
        :exceptions:
            | ATSTypeError: Parameter type validation failed.
            | Dynamically raises the provided exception_class (e.g., ATSValueError).
    '''
    check_type(file_path, str, exc_message)

    if not file_path:
        raise_context_error(
            fallback_prefix=r'factory_file_utils::normalize_path',
            fallback_msg=r'file path must be provided',
            exc_message=exc_message,
            exception_class=exception_class,
            depth=3
        )

    clean_file_path = PurePosixPath(normpath(file_path.replace('\\', '/'))).as_posix()

    if clean_file_path.startswith('/'):
        clean_file_path = clean_file_path[1:]

    return clean_file_path


def resolve_relative_path(
    normalized_name: str,
    source_dir_clean: str,
    exc_message: str | None = None,
    exception_class: type[Exception] = ATSValueError
) -> str | None:
    '''
        Calculates relative path to the specified source directory.

        :param normalized_name: The cleaned name of the archive member.
        :type normalized_name: <str>
        :param source_dir_clean: Cleaned source directory name.
        :type source_dir_clean: <str>
        :param exc_message: Message to include in the exception message.
        :type exc_message: <str | None>
        :param exception_class: The exception class to raise if value is None.
        :type exception_class: <type[Exception]> (default ATSValueError)
        :return: The relative path inside the source dir, or None if not matching.
        :rtype: <str | None>
        :exceptions:
            | ATSTypeError: Parameter type validation failed.
            | Dynamically raises the provided exception_class (e.g., ATSValueError).
    '''
    check_type(normalized_name, str, exc_message)
    check_type(source_dir_clean, str, exc_message)

    if not normalized_name:
        raise_context_error(
            fallback_prefix=r'factory_file_utils::resolve_relative_path',
            fallback_msg=r'normalized_name must be provided',
            exc_message=exc_message,
            exception_class=exception_class,
            depth=3
        )

    if not source_dir_clean:
        raise_context_error(
            fallback_prefix=r'factory_file_utils::resolve_relative_path',
            fallback_msg=r'source_dir_clean must be provided',
            exc_message=exc_message,
            exception_class=exception_class,
            depth=3
        )

    if normalized_name == source_dir_clean:
        return ''

    elif normalized_name.startswith(source_dir_clean + '/'):
        return normalized_name[len(source_dir_clean) + 1:]

    return None


def is_excluded_path(
    rel_path: str,
    exclude_patterns: Sequence[str],
    exc_message: str | None = None,
    exception_class: type[Exception] = ATSValueError
) -> bool:
    '''
        Checks if a relative path matches any exclusion patterns.

        :param rel_path: The relative path to inspect.
        :type rel_path: <str>
        :param exclude_patterns: Sequence of glob patterns to exclude.
        :type exclude_patterns: <Sequence[str]>
        :param exc_message: Message to include in the exception message.
        :type exc_message: <str | None>
        :param exception_class: The exception class to raise if value is None.
        :type exception_class: <type[Exception]> (default ATSValueError)
        :return: True if the path should be excluded, False otherwise.
        :rtype: <bool>
        :exceptions:
            | ATSTypeError: Parameter type validation failed.
            | Dynamically raises the provided exception_class (e.g., ATSValueError).
    '''
    check_type(rel_path, str, exc_message)
    check_type(exclude_patterns, Sequence, exc_message)

    if not rel_path:
        raise_context_error(
            fallback_prefix=r'factory_file_utils::is_excluded_path',
            fallback_msg=r'rel_path must be provided',
            exc_message=exc_message,
            exception_class=exception_class,
            depth=3
        )

    if not exclude_patterns:
        raise_context_error(
            fallback_prefix=r'factory_file_utils::is_excluded_path',
            fallback_msg=r'exclude_patterns must be provided',
            exc_message=exc_message,
            exception_class=exception_class,
            depth=3
        )

    parts = rel_path.split('/')

    for pattern in exclude_patterns:
        if fnmatch(rel_path, pattern) or any(fnmatch(part, pattern) for part in parts):
            return True

    return False


def format_casing_by_match(
    clean_str: str,
    default_val: str,
    upper_val: str,
    camel_val: str,
    dashed_val: str,
    exc_message: str | None = None,
    exception_class: type[Exception] = ATSValueError
) -> str:
    '''
        Formats a replacement value according to the casing style matched in clean_str.

        :param clean_str: Cleaned matched substring to analyze.
        :type clean_str: <str>
        :param default_val: Default replacement value.
        :type default_val: <str>
        :param upper_val: Value in UPPER_CASE.
        :type upper_val: <str>
        :param camel_val: Value in CamelCase/PascalCase.
        :type camel_val: <str>
        :param dashed_val: Value in dashed-case.
        :type dashed_val: <str>
        :param exc_message: Message to include in the exception message.
        :type exc_message: <str | None>
        :param exception_class: The exception class to raise if value is None.
        :type exception_class: <type[Exception]> (default ATSValueError)
        :return: The replacement formatted in matching casing style.
        :rtype: <str>
        :exceptions:
            | ATSTypeError: Parameter type validation failed.
            | Dynamically raises the provided exception_class (e.g., ATSValueError).
    '''
    check_type(clean_str, str, exc_message)
    check_type(default_val, str, exc_message)
    check_type(upper_val, str, exc_message)
    check_type(camel_val, str, exc_message)
    check_type(dashed_val, str, exc_message)

    if not clean_str:
        raise_context_error(
            fallback_prefix=r'factory_file_utils::format_casing_by_match',
            fallback_msg=r'clean_str must be provided',
            exc_message=exc_message,
            exception_class=exception_class,
            depth=3
        )

    if not default_val:
        raise_context_error(
            fallback_prefix=r'factory_file_utils::format_casing_by_match',
            fallback_msg=r'default_val must be provided',
            exc_message=exc_message,
            exception_class=exception_class,
            depth=3
        )

    if not upper_val:
        raise_context_error(
            fallback_prefix=r'factory_file_utils::format_casing_by_match',
            fallback_msg=r'upper_val must be provided',
            exc_message=exc_message,
            exception_class=exception_class,
            depth=3
        )

    if not camel_val:
        raise_context_error(
            fallback_prefix=r'factory_file_utils::format_casing_by_match',
            fallback_msg=r'camel_val must be provided',
            exc_message=exc_message,
            exception_class=exception_class,
            depth=3
        )

    if not dashed_val:
        raise_context_error(
            fallback_prefix=r'factory_file_utils::format_casing_by_match',
            fallback_msg=r'dashed_val must be provided',
            exc_message=exc_message,
            exception_class=exception_class,
            depth=3
        )

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
    exc_message: str | None = None,
    exception_class: type[Exception] = ATSValueError
) -> None:
    '''
        Writes string or bytes content to a file.

        :param file_path: Path to the target file.
        :type file_path: <str>
        :param content: Text string or raw bytes to write.
        :type content: <str | bytes>
        :param exc_message: Message to include in the exception message.
        :type exc_message: <str | None>
        :param exception_class: The exception class to raise if value is None.
        :type exception_class: <type[Exception]> (default ATSValueError)
        :exceptions:
            | ATSTypeError: Parameter type validation failed.
            | Dynamically raises the provided exception_class (e.g., ATSValueError).
    '''
    check_type(file_path, str, exc_message)
    check_type(content, (str, bytes), exc_message)

    if not file_path:
        raise_context_error(
            fallback_prefix=r'factory_file_utils::write_content',
            fallback_msg=r'file_path must be provided',
            exc_message=exc_message,
            exception_class=exception_class,
            depth=3
        )

    if not content:
        raise_context_error(
            fallback_prefix=r'factory_file_utils::write_content',
            fallback_msg=r'content must be provided',
            exc_message=exc_message,
            exception_class=exception_class,
            depth=3
        )

    if isinstance(content, str):
        with open(file_path, 'w', encoding='utf-8') as out_f:
            out_f.write(content)
    else:
        with open(file_path, 'wb') as out_f:
            out_f.write(content)


def apply_path_replacements(
    rel_path: str,
    path_replacements: Mapping[str, str],
    vals: Mapping[str, str],
    exc_message: str | None = None,
    exception_class: type[Exception] = ATSValueError
) -> str:
    '''
        Applies path replacements to a relative path using casing heuristics.

        :param rel_path: The original relative path.
        :type rel_path: <str>
        :param path_replacements: String replacements mapping.
        :type path_replacements: <Mapping[str, str]>
        :param vals: Computed template values.
        :type vals: <Mapping[str, str]>
        :param exc_message: Message to include in the exception message.
        :type exc_message: <str | None>
        :param exception_class: The exception class to raise if value is None.
        :type exception_class: <type[Exception]> (default ATSValueError)
        :return: The replaced relative path.
        :rtype: <str>
        :exceptions:
            | ATSTypeError: Parameter type validation failed.
            | Dynamically raises the provided exception_class (e.g., ATSValueError).
    '''
    check_type(rel_path, str, exc_message)
    check_type(path_replacements, Mapping, exc_message)
    check_type(vals, Mapping, exc_message)

    if not rel_path:
        raise_context_error(
            fallback_prefix=r'factory_file_utils::apply_path_replacements',
            fallback_msg=r'rel_path must be provided',
            exc_message=exc_message,
            exception_class=exception_class,
            depth=3
        )

    if not path_replacements:
        raise_context_error(
            fallback_prefix=r'factory_file_utils::apply_path_replacements',
            fallback_msg=r'path_replacements must be provided',
            exc_message=exc_message,
            exception_class=exception_class,
            depth=3
        )

    if not vals:
        raise_context_error(
            fallback_prefix=r'factory_file_utils::apply_path_replacements',
            fallback_msg=r'vals must be provided',
            exc_message=exc_message,
            exception_class=exception_class,
            depth=3
        )

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
        pattern = compile(pattern_str, IGNORECASE)

        def replace_match(match: Match) -> str:
            clean_str = match.group(0).lstrip('-_')

            return format_casing_by_match(
                clean_str=clean_str,
                default_val=replacement_val,
                upper_val=vals.get(f'{var_name}_upper', replacement_val.upper()),
                camel_val=vals.get(f'{var_name}_camel', replacement_val),
                dashed_val=vals.get(f'{var_name}_dashed', replacement_val.replace('_', '-'))
            )

        dest_rel_path = pattern.sub(replace_match, dest_rel_path)

    return dest_rel_path
