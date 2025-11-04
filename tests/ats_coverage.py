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
from typing import Any, Dict, List, Optional
from os.path import exists, basename
from json import load
from unittest import TestLoader, TestSuite, TextTestRunner
from argparse import Namespace

try:
    from pathlib import Path
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.success import success_message
    from ats_utilities.console_io.error import error_message
    from ats_utilities.option import ATSOptionParser
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_file_error import ATSFileError
    from coverage import Coverage
except ImportError as ats_error_message:  # pragma: no cover
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')  # pragma: no cover

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_coverage'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
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
    checker: ATSChecker = ATSChecker()
    error_msg: Optional[str] = None
    error_id: Optional[int] = None
    error_msg, error_id = checker.check_params([('str:pro_name', pro_name)])
    if error_id == checker.TYPE_ERROR:
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
    success_message([f'\nats_coverage: generated coverage {report_file_name}'])
    return report_file_name


def load_report(report_file_path: str) -> Dict[str, Any]:
    '''
        Loads report from report file.

        :param report_file_path: Report file path
        :type report_file_path: <str>
        :exceptions: ATSTypeError | ATSFileError
    '''
    checker: ATSChecker = ATSChecker()
    error_msg: Optional[str] = None
    error_id: Optional[int] = None
    error_msg, error_id = checker.check_params([(
        'str:report_file_path', report_file_path
    )])
    if error_id == checker.TYPE_ERROR:
        raise ATSTypeError(error_msg)
    if not exists(report_file_path):
        raise ATSFileError(f'{report_file_path} does not exist.')
    data: Dict[str, Any] = {}
    with open(report_file_path, 'r', encoding='utf-8') as loaded_file:
        data = load(loaded_file)
    return data


def find_root_package(module_path: str) -> Optional[Path]:
    '''
        Finds root package for project structure.

        :param module_path: Absolute path
        :type module_path: <str>
        :exceptions: ATSTypeError
    '''
    checker: ATSChecker = ATSChecker()
    error_msg: Optional[str] = None
    error_id: Optional[int] = None
    error_msg, error_id = checker.check_params([(
        'str:module_path', module_path
    )])
    if error_id == checker.TYPE_ERROR:
        raise ATSTypeError(error_msg)
    root: Optional[Path] = None
    path: Path = Path(module_path).resolve()
    while path.parent != path:
        if (path / '__init__.py').exists():
            root = path
        path = path.parent
    return root


def update_readme(coverage: Dict[str, Any]) -> None:
    '''
        Updates README.md file with code coverage report table.

        :param coverage: Coverage data report
        :type coverage: <Dict[str, Any]>
        :exceptions: ATSTypeError
    '''
    checker: ATSChecker = ATSChecker()
    error_msg: Optional[str] = None
    error_id: Optional[int] = None
    error_msg, error_id = checker.check_params([('dict:coverage', coverage)])
    if error_id == checker.TYPE_ERROR:
        raise ATSTypeError(error_msg)
    readme_path: str = '../README.md'
    start_marker: str = '### Code coverage'
    end_marker: str = '### Docs'
    lines: List[str] = []
    with open(readme_path, 'r', encoding='utf-8') as current_file:
        lines = current_file.readlines()
    new_lines: List[str] = []
    inside_block: bool = False
    stmts: str = 'num_statements'
    miss: str = 'missing_lines'
    cover: str = 'percent_covered_display'
    for line in lines:
        if start_marker in line:
            inside_block = True
            new_lines.append(line)
            new_lines.append('\n')
            new_lines.append('| Name | Stmts | Miss | Cover |\n')
            new_lines.append('|------|-------|------|-------|\n')
            file_names: List[str] = coverage['files']
            for name in file_names:
                root_package: Optional[Path] = find_root_package(name)
                module: str = ''
                if name.startswith(str(root_package)):
                    result: str = name[len(str(root_package)):]
                    result = result.lstrip('/')
                    module = f'{basename(str(root_package))}/{result}'
                file_summary: Dict[str, Any] = coverage['files'][name]
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
        elif end_marker in line:
            inside_block = False
            new_lines.append('\n')
            new_lines.append(line)
            continue
        if not inside_block:
            new_lines.append(line)
    with open(readme_path, 'w', encoding='utf-8') as update_file:
        update_file.writelines(new_lines)


if __name__ == "__main__":
    cli: ATSOptionParser = ATSOptionParser(
        'ats_coverage 2025', '1.0.0', 'GPLv3', False
    )
    cli.add_operation(
        '-n', '--name', dest='name',
        help='generate coverage report for project (provide name)'
    )
    args: Namespace = cli.parse_args(sys.argv)
    if not bool(getattr(args, "name")):
        error_message(['ats_coverage: missing name argument'])
        sys.exit(127)
    try:
        pro_report_file: str = f'{getattr(args, "name")}_coverage.json'
        report_data: Dict[str, Any] = load_report(pro_report_file)
        update_readme(report_data)
    except (ATSTypeError, ATSFileError) as e:
        error_message([f'ats_coverage: {e}'])
        sys.exit(128)
