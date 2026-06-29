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

import sys
from typing import Any
from os.path import exists, basename
from json import load
from unittest import TestLoader, TestSuite, TextTestRunner
from pathlib import Path
from coverage import Coverage
from ats_utilities.checker.engine import Checker
from ats_utilities.checker.ichecker import ErrorChecker
from ats_utilities.reporter.engine import Reporter
from ats_utilities.option.engine import OptionManager
from ats_utilities.option.component_bundle import OptionComponentBundle
from ats_utilities.option.option_namespace import OptionNamespace
from ats_utilities.exceptions.ats_type_error import ATSTypeError
from ats_utilities.exceptions.ats_file_error import ATSFileError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_coverage'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_coverage/blob/dev/LICENSE'
__version__: str = '1.0.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


def run_coverage(pro_name: str) -> str:
    '''
        Runs coverage for project and generates report.

        :param pro_name: Project name
        :type pro_name: <str>
        :exceptions: ATSTypeError | ATSFileError
    '''
    checker: Checker = Checker()
    error_msg: str | None = None
    error_id: int | None = None
    error_msg, error_id = checker.validates_parameters([('str:pro_name', pro_name)])
    if error_id == ErrorChecker.TYPE_ERROR:
        raise ATSTypeError(error_msg)
    if not exists(f'../{pro_name}'):
        raise ATSFileError(f'missing ../{pro_name}')
    cov = Coverage(source=[f'../{pro_name}'])
    cov.start()
    tests: TestSuite = TestLoader().discover('.', pattern='*_test.py')
    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(tests)
    cov.stop()
    cov.save()
    report_file_name: str = f'{pro_name}_coverage.json'
    cov.json_report(outfile=report_file_name)
    reporter: Reporter = Reporter()
    reporter.success([f'\nats_coverage: generated coverage {report_file_name}'])
    return report_file_name


def load_report(report_file_path: str) -> dict[str, Any]:
    '''
        Loads report from report file.

        :param report_file_path: Report file path
        :type report_file_path: <str>
        :exceptions: ATSTypeError | ATSFileError
    '''
    checker: Checker = Checker()
    error_msg: str | None = None
    error_id: int | None = None
    error_msg, error_id = checker.validates_parameters([(
        'str:report_file_path', report_file_path
    )])
    if error_id == ErrorChecker.TYPE_ERROR:
        raise ATSTypeError(error_msg)
    if not exists(report_file_path):
        raise ATSFileError(f'{report_file_path} does not exist.')
    data: dict[str, Any] = {}
    with open(report_file_path, 'r', encoding='utf-8') as loaded_file:
        data = load(loaded_file)
    return data


def find_root_package(module_path: str) -> Path | None:
    '''
        Finds root package for project structure.

        :param module_path: Absolute path
        :type module_path: <str>
        :exceptions: ATSTypeError
    '''
    checker: Checker = Checker()
    error_msg: str | None = None
    error_id: int | None = None
    error_msg, error_id = checker.validates_parameters([(
        'str:module_path', module_path
    )])
    if error_id == ErrorChecker.TYPE_ERROR:
        raise ATSTypeError(error_msg)
    root: Path | None = None
    path: Path = Path(module_path).resolve()
    while path.parent != path:
        if (path / '__init__.py').exists():
            root = path
        path = path.parent
    return root


def update_readme(coverage: dict[str, Any]) -> None:
    '''
        Updates README.md file with code coverage report table.

        :param coverage: Coverage data report
        :type coverage: <dict[str, Any]>
        :exceptions: ATSTypeError
    '''
    checker: Checker = Checker()
    error_msg: str | None = None
    error_id: int | None = None
    error_msg, error_id = checker.validates_parameters([('dict:coverage', coverage)])
    if error_id == ErrorChecker.TYPE_ERROR:
        raise ATSTypeError(error_msg)
    readme_path: str = 'README.md'
    lines: list[str] = []
    with open(readme_path, 'r', encoding='utf-8') as current_file:
        lines = current_file.readlines()
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

def _build_tree(dir_path: Path, prefix: str = "") -> tuple[list[str], int, int]:
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

    # Sort entries by name, ignoring leading underscores
    entries.sort(key=lambda x: x.name.lstrip('_').lower())

    lines = []
    num_dirs = 0
    num_files = 0

    for i, entry in enumerate(entries):
        is_last = (i == len(entries) - 1)
        connector = "└── " if is_last else "├── "

        if entry.is_dir():
            num_dirs += 1
            lines.append(f"{prefix}{connector}{entry.name}/\n")
            new_prefix = prefix + ("    " if is_last else "│\xa0\xa0 ")
            sub_lines, sub_dirs, sub_files = _build_tree(entry, new_prefix)
            lines.extend(sub_lines)
            num_dirs += sub_dirs
            num_files += sub_files
        else:
            num_files += 1
            lines.append(f"{prefix}{connector}{entry.name}\n")

    return lines, num_dirs, num_files


def generate_tree_lines(pro_name: str) -> tuple[list[str], int, int]:
    '''
        Generates tree structure representation of package.

        :param pro_name: Project name.
        :type pro_name: <str>
        :return: Tuple containing tree lines list, directory count, and file count.
        :rtype: <tuple[list[str], int, int]>
        :exceptions: ATSFileError
    '''
    pro_path = Path(pro_name)
    if not pro_path.exists():
        raise ATSFileError(f'missing {pro_name} folder')

    lines = [f"    {pro_name}/\n"]
    sub_lines, num_dirs, num_files = _build_tree(pro_path, prefix="         ")
    lines.extend(sub_lines)

    # Root itself is a directory
    return lines, num_dirs + 1, num_files


def update_structure(pro_name: str) -> None:
    '''
        Updates README.md file with package directory structure.

        :param pro_name: Project name
        :type pro_name: <str>
        :exceptions: ATSTypeError | ATSFileError
    '''
    checker: Checker = Checker()
    error_msg: str | None = None
    error_id: int | None = None
    error_msg, error_id = checker.validates_parameters([('str:pro_name', pro_name)])
    if error_id == ErrorChecker.TYPE_ERROR:
        raise ATSTypeError(error_msg)

    readme_path: str = 'README.md'
    if not exists(readme_path):
        raise ATSFileError(f'{readme_path} does not exist.')

    tree_lines, num_dirs, num_files = generate_tree_lines(pro_name)

    lines: list[str] = []
    with open(readme_path, 'r', encoding='utf-8') as current_file:
        lines = current_file.readlines()

    new_lines: list[str] = []
    inside_tool_structure: bool = False
    replace_mode: bool = False

    for line in lines:
        if '### Tool structure' in line:
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

    with open(readme_path, 'w', encoding='utf-8') as update_file:
        update_file.writelines(new_lines)


if __name__ == "__main__":
    cli: OptionManager = OptionManager(OptionComponentBundle(parameters={
        'description': 'ats_coverage 2025',
        'version': '1.0.0',
        'licence': 'GPLv3'
    }))
    cli.add_operation(
        '-n', '--name', dest='name',
        help='generate coverage report for project (provide name)'
    )
    args: OptionNamespace = cli.parse_args(sys.argv)
    main_reporter: Reporter = Reporter()

    if not bool(getattr(args, "name")):
        main_reporter.error(['ats_coverage: missing name argument'])
        sys.exit(127)
    try:
        pro_report_file: str = f'{getattr(args, "name")}.json'
        report_data: dict[str, Any] = load_report(pro_report_file)
        update_readme(report_data)
        update_structure(getattr(args, "name"))
    except (ATSTypeError, ATSFileError) as e:
        main_reporter.error([f'ats_coverage: {e}'])
        sys.exit(128)
