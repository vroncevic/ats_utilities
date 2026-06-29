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

from os.path import exists, normpath
from fnmatch import fnmatch
from re import compile, escape, Match, IGNORECASE
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.exceptions.ats_value_error import ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


def check_file_exists(file_path: str) -> None:
    '''
        Checks if a file exists.

        :param file_path: Path to the file.
        :type file_path: <str>
        :exceptions:
            | ATSTypeError: Expected str for 'file_path', got <type>.
            | ATSValueError: File at the provided path does not exist.
    '''
    if not isinstance(file_path, str):
        raise ATSTypeError(f"expected str for 'file_path', got {type(file_path).__name__}")

    if not exists(file_path):
        raise ATSValueError(f"file at the provided path does not exist: {file_path}")


def normalize_path(path: str) -> str:
    '''
        Normalizes file paths and strips leading directory prefixes.

        :param path: The original path to clean up.
        :type path: <str>
        :return: The cleaned up relative path.
        :rtype: <str>
        :exceptions:
            | ATSTypeError: Expected str for 'path', got <type>.
    '''
    if not isinstance(path, str):
        raise ATSTypeError(f"expected str for 'path', got {type(path).__name__}")

    clean_path = normpath(path).replace('\\', '/')

    if clean_path.startswith('./'):
        clean_path = clean_path[2:]

    if clean_path.startswith('/'):
        clean_path = clean_path[1:]

    return clean_path


def resolve_relative_path(normalized_name: str, source_dir_clean: str) -> str | None:
    '''
        Calculates relative path to the specified source directory.

        :param normalized_name: The cleaned name of the archive member.
        :type normalized_name: <str>
        :param source_dir_clean: Cleaned source directory name.
        :type source_dir_clean: <str>
        :return: The relative path inside the source dir, or None if not matching.
        :rtype: <str | None>
        :exceptions:
            | ATSTypeError: Expected str for parameters, got <type>.
    '''
    if not isinstance(normalized_name, str):
        raise ATSTypeError(f"expected str for 'normalized_name', got {type(normalized_name).__name__}")

    if not isinstance(source_dir_clean, str):
        raise ATSTypeError(f"expected str for 'source_dir_clean', got {type(source_dir_clean).__name__}")

    if normalized_name == source_dir_clean:
        return ""
    elif normalized_name.startswith(source_dir_clean + '/'):
        return normalized_name[len(source_dir_clean) + 1:]

    return None


def is_excluded_path(rel_path: str, exclude_patterns: list[str]) -> bool:
    '''
        Checks if a relative path matches any exclusion patterns.

        :param rel_path: The relative path to inspect.
        :type rel_path: <str>
        :param exclude_patterns: List of glob patterns to exclude.
        :type exclude_patterns: <list[str]>
        :return: True if the path should be excluded, False otherwise.
        :rtype: <bool>
        :exceptions:
            | ATSTypeError: Expected str and list parameters, got <type>.
    '''
    if not isinstance(rel_path, str):
        raise ATSTypeError(f"expected str for 'rel_path', got {type(rel_path).__name__}")

    if not isinstance(exclude_patterns, list):
        raise ATSTypeError(f"expected list for 'exclude_patterns', got {type(exclude_patterns).__name__}")

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
    dashed_val: str
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
        :return: The replacement formatted in matching casing style.
        :rtype: <str>
        :exceptions:
            | ATSTypeError: Expected str parameters, got <type>.
    '''
    if not all(isinstance(arg, str) for arg in (clean_str, default_val, upper_val, camel_val, dashed_val)):
        raise ATSTypeError("All parameters must be of type str")

    if clean_str.isupper():
        return upper_val
    elif clean_str and clean_str[0].isupper():
        return camel_val
    elif '-' in clean_str:
        return dashed_val
    else:
        return default_val


def write_content(file_path: str, content: str | bytes) -> None:
    '''
        Writes string or bytes content to a file.

        :param file_path: Path to the target file.
        :type file_path: <str>
        :param content: Text string or raw bytes to write.
        :type content: <str | bytes>
        :exceptions:
            | ATSTypeError: Expected str for 'file_path', or str/bytes for 'content'.
    '''
    if not isinstance(file_path, str):
        raise ATSTypeError(f"expected str for 'file_path', got {type(file_path).__name__}")

    if not isinstance(content, (str, bytes)):
        raise ATSTypeError(f"expected str or bytes for 'content', got {type(content).__name__}")

    if isinstance(content, str):
        with open(file_path, 'w', encoding='utf-8') as out_f:
            out_f.write(content)
    else:
        with open(file_path, 'wb') as out_f:
            out_f.write(content)


def apply_path_replacements(
    rel_path: str,
    path_replacements: dict[str, str],
    vals: dict[str, str]
) -> str:
    '''
        Applies path replacements to a relative path using casing heuristics.

        :param rel_path: The original relative path.
        :type rel_path: <str>
        :param path_replacements: String replacements mapping.
        :type path_replacements: <dict[str, str]>
        :param vals: Computed template values.
        :type vals: <dict[str, str]>
        :return: The replaced relative path.
        :rtype: <str>
        :exceptions:
            | ATSTypeError: Expected str parameters, got <type>.
    '''
    if not isinstance(rel_path, str):
        raise ATSTypeError(f"expected str for 'rel_path', got {type(rel_path).__name__}")

    if not isinstance(path_replacements, dict):
        raise ATSTypeError(f"expected dict for 'path_replacements', got {type(path_replacements).__name__}")

    if not isinstance(vals, dict):
        raise ATSTypeError(f"expected dict for 'vals', got {type(vals).__name__}")

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
                upper_val=vals.get(f"{var_name}_upper", replacement_val.upper()),
                camel_val=vals.get(f"{var_name}_camel", replacement_val),
                dashed_val=vals.get(f"{var_name}_dashed", replacement_val.replace('_', '-'))
            )

        dest_rel_path = pattern.sub(replace_match, dest_rel_path)

    return dest_rel_path
