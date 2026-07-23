# -*- coding: UTF-8 -*-

'''
Module
    check_interfaces.py
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
    Defines attribute(s) and function(s) for interface check support.
'''

from __future__ import annotations

import os
import ast
import sys

def get_base_name(node):
    """Extracts the base class name regardless of generics (Subscript) or attributes."""
    if isinstance(node, ast.Subscript):
        return get_base_name(node.value)
    if isinstance(node, ast.Name):
        return node.id
    elif isinstance(node, ast.Attribute):
        return node.attr

    return None

def is_dataclass(class_node):
    """Checks if the class is decorated with @dataclass."""
    for decorator in class_node.decorator_list:
        if isinstance(decorator, ast.Name) and decorator.id == 'dataclass':
            return True
        elif isinstance(decorator, ast.Call) and isinstance(decorator.func, ast.Name) and decorator.func.id == 'dataclass':
            return True

    return False

def inherits_from(class_node, exception_names):
    """Checks if the class inherits from any of the base classes from the allowed/ignored list."""
    for base in class_node.bases:
        name = get_base_name(base)

        if name in exception_names:
            return True

    return False

def main():
    package_dir = 'ats_utilities'
    errors = []
    defined_interfaces = {}

    ignored_bases = {
        'Exception', 'BaseException', 'ValueError', 'TypeError', 'KeyError', 
        'AttributeError', 'LookupError', 'RuntimeError', 'int', 'str', 'dict', 
        'list', 'set', 'tuple', 'bytes', 'object', 

        'TypedDict', 'Protocol', 'Generic', 'NamedTuple', 'ABC', 'ABCMeta',

        'Enum', 'IntEnum', 'StrEnum', 'Flag', 'IntFlag', 
        'ArgumentParser', 'Action', 'Formatter',

        'Thread', 'Process', 'Task', 'Future',
    }

    # 1. Collecting all defined interfaces (classes starting with 'I' and an uppercase letter)
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
                        if node.name.startswith('I') and len(node.name) > 1 and node.name[1].isupper():
                            defined_interfaces[node.name] = path

            except Exception as e:
                print(f"Error parsing {path}: {e}")

    # 2. Verification of concrete classes
    for root, _, files in os.walk(package_dir):
        if 'exceptions' in root:
            continue

        for file in files:
            if not file.endswith('.py') or file == '__init__.py':
                continue
            path = os.path.join(root, file)
            
            # Skipping files that are interfaces by convention
            if file.startswith('i') and len(file) > 1 and file[1].isupper():
                continue
                
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    tree = ast.parse(f.read(), filename=path)
                for node in ast.walk(tree):
                    if not isinstance(node, ast.ClassDef):
                        continue
                    
                    if node.name.startswith('I') and len(node.name) > 1 and node.name[1].isupper():
                        continue
                    
                    if is_dataclass(node):
                        continue
                        
                    if inherits_from(node, ignored_bases):
                        continue
                    
                    interfaces_inherited = []
                    for base in node.bases:
                        base_name = get_base_name(base)
                        if base_name and base_name.startswith('I') and len(base_name) > 1 and base_name[1].isupper():
                            interfaces_inherited.append(base_name)
                    
                    if not interfaces_inherited:
                        errors.append(f"❌ Class '{node.name}' in module '{path}' does not inherit from any interface.")
                        continue
                        
                    for base_name in interfaces_inherited:
                        if base_name not in defined_interfaces:
                            errors.append(f"❌ Class '{node.name}' in module '{path}' inherits from '{base_name}', but this interface is not defined in the codebase.")
                            
            except Exception as e:
                print(f"Error parsing {path}: {e}")

    if errors:
        for err in errors:
            print(err)

        print("---")
        print("Quality Gate Failed! Concrete class implementation is missing its interface or inherits from an undefined interface.")
        sys.exit(1)
    else:
        print("✅ Quality Gate Pass: Interface segregation requirements and interface definitions are respected.")
        sys.exit(0)

if __name__ == '__main__':
    main()
