# -*- coding: UTF-8 -*-

'''
Module
    ats_coverage.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    ats_coverage is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    ats_coverage is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines attribute(s) and method(s) for coverage support.
'''

from __future__ import annotations

from sys import stdout, stderr, exit
from json import load
from os.path import basename
from pathlib import Path
from typing import Any
from unittest import TestLoader, TestSuite, TextTestRunner

from coverage import Coverage

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_coverage'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_coverage/blob/dev/LICENSE'
__version__ = r'1.0.0'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


def check_exists(item_path: str, is_dir: bool = False) -> None:
    '''
        Checks if the item exists.

        :param item_path: Item path.
        :type item_path: <str>
        :param is_dir: Flag indicating if the path is a directory.
        :type is_dir: <bool>
        :exceptions:
            | TypeError: Parameter dir_path type validation failed.
            | ValueError: Parameter dir_path format validation failed.
            | ValueError: Directory with name does not exist.
    '''
    if not isinstance(item_path, str):
        raise TypeError(f'Parameter item_path must be of type str, not {type(item_path).__name__}')

    if not item_path:
        raise ValueError('Parameter item_path cannot be empty')

    if is_dir:
        if not Path(item_path).is_dir():
            raise ValueError(f'Directory with name {item_path} does not exist')
    else:
        if not Path(item_path).is_file():
            raise ValueError(f'File with name {item_path} does not exist')


def run_coverage(pro_name: str) -> None:
    '''
        Runs coverage for project and generates reports in JSON and XML formats.

        :param pro_name: Project name (is equal to directory name).
        :type pro_name: <str>
        :exceptions:
            | TypeError: Parameter pro_name type validation failed.
            | ValueError: Parameter pro_name format validation failed.
            | ValueError: Directory with name does not exist.
    '''
    check_exists(pro_name, is_dir=True)

    cov = Coverage(source=[f'{pro_name}'], config_file='.coveragerc')
    stdout.write('\n--- Starting coverage ---\n')
    cov.start()

    tests: TestSuite = TestLoader().discover('tests', pattern='*_test.py', top_level_dir='.')
    test_runner = TextTestRunner(verbosity=2)
    stdout.write('\n--- Test Report ---\n')
    test_runner.run(tests)

    cov.stop()
    cov.save()

    stdout.write('\n--- Coverage Report ---\n')
    cov.report()
    stdout.write('\n--- JSON Report ---\n')
    cov.json_report(outfile=f'{pro_name}.json')
    stdout.write(f'\n--- JSON Report saved to {pro_name}.json ---\n')
    stdout.write('\n--- XML Report ---\n')
    cov.xml_report(outfile=f'{pro_name}.xml')
    stdout.write(f'\n--- XML Report saved to {pro_name}.xml ---\n')
    stdout.write('\n--- HTML Report ---\n')
    cov.html_report(directory='htmlcov')
    stdout.write('\n--- HTML Report saved to htmlcov ---\n')


def load_report(file_path: str) -> dict[str, Any]:
    '''
        Loads coverage report from file (JSON format).

        :param file_path: Coverage report file path.
        :type file_path: <str>
        :return: Coverage data report in dict format.
        :rtype: <dict[str, Any]>
        :exceptions:
            | ATSTypeError: Parameter file_path type validation failed.
            | ATSValueError: Parameter file_path format validation failed.
            | ATSValueError: File with name does not exist.
    '''

    check_exists(file_path)

    data: dict[str, Any] = {}

    try:
        with open(file_path, 'r', encoding='utf-8') as loaded_file:
            data = load(loaded_file)

    except (OSError, UnicodeDecodeError) as exc:
        stderr.write(f'{exc}\n')
        pass

    return data


def find_root_package(module_path: str) -> Path | None:
    '''
        Finds root package for project structure.

        :param module_path: Absolute path for project package.
        :type module_path: <str>
        :return: Root package path.
        :rtype: <Path | None>
        :exceptions:
            | ATSTypeError: Parameter module_path type validation failed.
            | ATSValueError: Parameter module_path format validation failed.
    '''
    root: Path | None = None
    path: Path = Path(module_path).resolve()

    while path.parent != path:
        if (path / '__init__.py').exists():
            root = path

        path = path.parent

    return root


def update_readme(coverage: dict[str, Any], readme_path: str = 'README.md') -> None:
    '''
        Updates README.md file with code coverage report table.

        :param coverage: Coverage data report in dict format.
        :type coverage: <dict[str, Any]>
        :param readme_path: Path to README.md file.
        :type readme_path: <str>
        :exceptions:
            | ATSTypeError: Parameter coverage type validation failed.
            | ATSValueError: Parameter coverage format validation failed.
            | ATSValueError: Parameter readme_path type validation failed.
            | ATSValueError: Parameter readme_path format validation failed.
            | ATSValueError: File with name does not exist.
    '''
    check_exists(readme_path)
    lines: list[str] = []

    try:
        with open(readme_path, 'r', encoding='utf-8') as readme_file:
            lines = readme_file.readlines()

    except (OSError, UnicodeDecodeError) as exc:
        stderr.write(f'{exc}\n')
        return

    new_lines: list[str] = []
    inside_coverage: bool = False
    inside_table: bool = False
    stmts: str = 'num_statements'
    miss: str = 'missing_lines'
    cover: str = 'percent_covered_display'

    for line in lines:
        if '### Code coverage' in line:
            inside_coverage = True
            new_lines.append(line)
            continue

        if inside_coverage:
            if '### Docs' in line:
                inside_coverage = False
                inside_table = False
                new_lines.append(line)
                continue

            if '</summary>' in line:
                inside_table = True
                new_lines.append(line)
                new_lines.append('\n')
                new_lines.append('| Name | Stmts | Miss | Cover |\n')
                new_lines.append('|------|-------|------|-------|\n')
                file_names: list[str] = coverage['files']

                for name in file_names:
                    root_package: Path | None = find_root_package(name)
                    module: str = ''

                    if root_package:
                        abs_name = str(Path(name).resolve())
                        abs_root = str(root_package.resolve())

                        if abs_name.startswith(abs_root):
                            result: str = abs_name[len(abs_root):]
                            result = result.lstrip('/')
                            module = f'{basename(abs_root)}/{result}'

                    file_summary: dict[str, Any] = coverage['files'][name]
                    statements: str = file_summary['summary'][stmts]
                    missing: str = file_summary['summary'][miss]
                    covered: str = file_summary['summary'][cover]
                    new_lines.append(
                        f'| `{module}` | {statements} | {missing} | {covered}%|\n'
                    )

                total: str = '| **Total** |'
                total_statements: str = coverage['totals'][stmts]
                total_missing: str = coverage['totals'][miss]
                total_covered: str = coverage['totals'][cover]
                total += f' {total_statements} |'
                total += f' {total_missing} |'
                total += f' {total_covered}% |\n'
                new_lines.append(total)
                continue

            if '</details>' in line:
                inside_table = False
                new_lines.append('\n')
                new_lines.append(line)
                continue

            if inside_table:
                continue

        if not inside_table:
            new_lines.append(line)

    with open(readme_path, 'w', encoding='utf-8') as update_file:
        update_file.writelines(new_lines)


def _build_tree(dir_path: Path, prefix: str = '') -> tuple[list[str], int, int]:
    '''
        Recursively builds tree lines and counts files/directories.

        :param dir_path: Directory path.
        :type dir_path: <Path>
        :param prefix: Current indentation prefix.
        :type prefix: <str>
        :return: Tuple containing tree lines list, directory count, and file count.
        :rtype: <tuple[list[str], int, int]>
        :exceptions: None.
    '''
    entries = []

    for entry in dir_path.iterdir():
        if entry.name == '__pycache__' or entry.name.startswith('.'):
            continue

        entries.append(entry)

    entries.sort(key=lambda x: x.name.lstrip('_').lower())

    lines = []
    num_dirs = 0
    num_files = 0

    for i, entry in enumerate(entries):
        is_last = (i == len(entries) - 1)
        connector = '└── ' if is_last else '├── '

        if entry.is_dir():
            num_dirs += 1
            lines.append(f'{prefix}{connector}{entry.name}/\n')
            new_prefix = prefix + ('    ' if is_last else '│\xa0\xa0 ')
            sub_lines, sub_dirs, sub_files = _build_tree(entry, new_prefix)
            lines.extend(sub_lines)
            num_dirs += sub_dirs
            num_files += sub_files
        else:
            num_files += 1
            lines.append(f'{prefix}{connector}{entry.name}\n')

    return lines, num_dirs, num_files

def generate_tree_lines(pro_name: str) -> tuple[list[str], int, int]:
    '''
        Generates tree structure representation of package.

        :param pro_name: Project name.
        :type pro_name: <str>
        :return: Tuple containing tree lines list, directory count, and file count.
        :rtype: <tuple[list[str], int, int]>
        :exceptions:
            | TypeError: Parameter pro_name type validation failed.
            | ValueError: Parameter pro_name format validation failed.
            | ValueError: Directory with name does not exist.
    '''
    check_exists(pro_name, is_dir=True)

    pro_path = Path(pro_name)
    lines = [f'    {pro_name}/\n']
    sub_lines, num_dirs, num_files = _build_tree(pro_path, prefix='         ')
    lines.extend(sub_lines)

    return lines, num_dirs + 1, num_files


def update_structure(pro_name: str, section: str, readme_path: str = 'README.md') -> None:
    '''
        Updates README.md file with package directory structure.

        :param pro_name: Project name.
        :type pro_name: <str>
        :param section: Section name.
        :type section: <str>
        :param readme_path: Path to README.md file.
        :type readme_path: <str>
        :exceptions:
            | ATSTypeError: Parameter pro_name type validation failed.
            | ATSTypeError: Parameter section type validation failed.
            | ATSValueError: File with name does not exist.
    '''
    check_exists(readme_path)

    tree_lines, num_dirs, num_files = generate_tree_lines(pro_name)
    lines: list[str] = []

    try:
        with open(readme_path, 'r', encoding='utf-8') as readme_file:
            lines = readme_file.readlines()

    except (OSError, UnicodeDecodeError) as exc:
        stderr.write(f'{exc}\n')
        return

    new_lines: list[str] = []
    inside_tool_structure: bool = False
    replace_mode: bool = False
    heading: str = f'### {section}'

    for line in lines:
        if heading in line:
            inside_tool_structure = True
            new_lines.append(line)
            continue

        if inside_tool_structure:
            if '### Code coverage' in line:
                inside_tool_structure = False
                replace_mode = False
                new_lines.append(line)
                continue

            if '</summary>' in line:
                new_lines.append(line)
                new_lines.append('\n')
                new_lines.append('```bash\n')
                new_lines.extend(tree_lines)
                new_lines.append('\n')
                new_lines.append(f'     {num_dirs} directories, {num_files} files\n')
                new_lines.append('```\n')
                replace_mode = True
                continue

            if '</details>' in line:
                replace_mode = False
                new_lines.append(line)
                continue

            if replace_mode:
                continue

        new_lines.append(line)

    try:
        with open(readme_path, 'w', encoding='utf-8') as readme_file:
            readme_file.writelines(new_lines)

    except (OSError, UnicodeDecodeError) as exc:
        stderr.write(f'{exc}\n')
        return


if __name__ == "__main__":
    try:
        pro_name: str = 'ats_utilities'
        run_coverage(pro_name)
        report_data: dict[str, Any] = load_report(f'{pro_name}.json')

        if report_data:
            update_readme(report_data)
            update_structure(pro_name, 'Framework structure')
            exit(0)

        stderr.write('ats_coverage: failed to generate coverage report\n')
        exit(129)

    except (ValueError, TypeError) as exc:
        stderr.write(f'ats_coverage: {exc}\n')
        exit(128)
