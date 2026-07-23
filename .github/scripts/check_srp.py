# -*- coding: UTF-8 -*-

'''
Module
    check_srp.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines attribute(s) and function(s) for SRP check support.
'''

from __future__ import annotations

import os
import ast
import sys

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'1.0.0'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


MAX_METHODS_PER_CLASS = 12
MAX_LOGICAL_LINES_PER_METHOD = 180

def count_logical_lines(method_node) -> int:
    '''
        Counts the actual logical lines of code in a method.
        Ignores docstrings, blank lines, and comments.

        :param method_node: The method node to count lines for.
        :return: The number of logical lines in the method.
    '''
    body = method_node.body

    if not body:
        return 0

    if isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant):
        if isinstance(body[0].value.value, str):
            body = body[1:]

    if not body:
        return 0

    logical_lines = set()

    for stmt in body:
        for node in ast.walk(stmt):
            if node is not stmt and isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                continue

            if hasattr(node, 'lineno'):
                logical_lines.add(node.lineno)

    return len(logical_lines)

def main():
    package_dir = 'ats_utilities'
    errors = []

    for root, _, files in os.walk(package_dir):
        for file in files:
            if not file.endswith('.py') or file == '__init__.py':
                continue
            
            path = os.path.join(root, file)

            try:
                with open(path, 'r', encoding='utf-8') as f:
                    tree = ast.parse(f.read(), filename=path)

                for node in ast.walk(tree):
                    if isinstance(node, ast.ClassDef):
                        methods = [
                            n for n in node.body 
                            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
                        ]
                        
                        if len(methods) > MAX_METHODS_PER_CLASS:
                            errors.append(
                                f"❌ SRP Violation: Class '{node.name}' in '{path}' has {len(methods)} methods "
                                f"(Max allowed is {MAX_METHODS_PER_CLASS}). Split the class!"
                            )

                        for method in methods:
                            lines = count_logical_lines(method)
                            if lines > MAX_LOGICAL_LINES_PER_METHOD:
                                errors.append(
                                    f"❌ SRP Violation: Method '{method.name}' in class '{node.name}' ('{path}') "
                                    f"is too long ({lines} logical lines, Max allowed is {MAX_LOGICAL_LINES_PER_METHOD})."
                                )
            except Exception as e:
                print(f"Error parsing {path}: {e}")

    if errors:
        for err in errors:
            print(err)

        print("---")
        print("Quality Gate Failed! Code violates SRP bounds.")
        sys.exit(1)
    else:
        print("✅ Quality Gate Pass: SRP constraints are respected.")
        sys.exit(0)

if __name__ == '__main__':
    main()
