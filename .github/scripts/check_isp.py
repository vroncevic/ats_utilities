# -*- coding: UTF-8 -*-

'''
Module
    check_isp.py
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
    Defines attribute(s) and function(s) for ISP check support.
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


MAX_ABSTRACT_METHODS = 9

def count_abstract_methods(class_node):
    """Count methods within a class that have the @abstractmethod decorator."""
    count = 0

    for node in class_node.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for decorator in node.decorator_list:
                if isinstance(decorator, ast.Name) and decorator.id == 'abstractmethod':
                    count += 1
                elif isinstance(decorator, ast.Attribute) and decorator.attr == 'abstractmethod':
                    count += 1

    return count

def main():
    package_dir = 'ats_utilities'
    errors = []

    for root, _, files in os.walk(package_dir):
        if 'exceptions' in root:
            continue

        for file in files:
            if not file.endswith('.py') or file == '__init__.py':
                continue

            path = os.path.join(root, file)

            try:
                with open(path, 'r', encoding='utf-8') as f:
                    tree = ast.parse(f.read(), filename=path)

                for node in ast.walk(tree):
                    if isinstance(node, ast.ClassDef):
                        is_interface_class = (
                            (node.name.startswith('I') and len(node.name) > 1 and node.name[1].isupper()) or
                            (file.startswith('i') and len(file) > 1 and file[1].isupper())
                        )

                        if is_interface_class:
                            method_count = count_abstract_methods(node)

                            if method_count > MAX_ABSTRACT_METHODS:
                                errors.append(
                                    f"❌ ISP Violation: Interface '{node.name}' in '{path}' "
                                    f"defines {method_count} abstract methods (Max allowed is {MAX_ABSTRACT_METHODS}). "
                                    f"Segregate this interface!"
                                )

            except Exception as e:
                print(f"Error parsing {path}: {e}")

    if errors:
        for err in errors:
            print(err)

        print("---")
        print("Quality Gate Failed! Fat interfaces detected based on abstract method count.")
        sys.exit(1)
    else:
        print("✅ Quality Gate Pass: Interface Segregation Principle constraints are respected.")
        sys.exit(0)

if __name__ == '__main__':
    main()
