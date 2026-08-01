# -*- coding: UTF-8 -*-

'''
Module
    check_interfaces.py
Info
    Defines attribute(s) and function(s) for Protocol interface check support.
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

def extract_methods_and_properties(class_node):
    """Izvlači nazive svih metoda i property-ja definisanih unutar klase."""
    members = set()
    for item in class_node.body:
        if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
            members.add(item.name)
    return members

def main():
    package_dir = 'ats_utilities'
    errors = []
    
    defined_protocols = {}

    ignored_bases = {
        'Exception', 'BaseException', 'ValueError', 'TypeError', 'KeyError', 
        'AttributeError', 'LookupError', 'RuntimeError', 'int', 'str', 'dict', 
        'list', 'set', 'tuple', 'bytes', 'object', 

        'TypedDict', 'Protocol', 'Generic', 'NamedTuple', 'ABC', 'ABCMeta',

        'Enum', 'IntEnum', 'StrEnum', 'Flag', 'IntFlag', 
        'ArgumentParser', 'Action', 'Formatter',

        'Thread', 'Process', 'Task', 'Future',
    }

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
                            defined_protocols[node.name] = extract_methods_and_properties(node)

            except Exception as e:
                print(f"Error parsing {path}: {e}")

    # 2. Verifikacija konkretnih klasa prema protokolima
    for root, _, files in os.walk(package_dir):
        if 'exceptions' in root:
            continue

        for file in files:
            if not file.endswith('.py') or file == '__init__.py':
                continue
            path = os.path.join(root, file)
            
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
                    
                    if is_dataclass(node) or inherits_from(node, ignored_bases):
                        continue
                    
                    class_methods = extract_methods_and_properties(node)
                    
                    # Npr. LogBuffer posmatra protokol ILogBuffer
                    expected_protocol_name = f"I{node.name}"
                    
                    if expected_protocol_name in defined_protocols:
                        required_methods = defined_protocols[expected_protocol_name]
                        missing_methods = required_methods - class_methods
                        
                        if missing_methods:
                            errors.append(
                                f"❌ Class '{node.name}' in '{path}' does not satisfy Protocol '{expected_protocol_name}'. "
                                f"Missing methods/properties: {missing_methods}"
                            )
                    else:
                        # Možeš opciono izdati grešku ili upozorenje ako konkretna klasa nema svoj I* protokol
                        # errors.append(f"⚠️ Warning: No protocol definition '{expected_protocol_name}' found for class '{node.name}'")
                        pass

            except Exception as e:
                print(f"Error parsing {path}: {e}")

    if errors:
        for err in errors:
            print(err)

        print("---")
        print("Quality Gate Failed! Concrete class does not satisfy Protocol requirements.")
        sys.exit(1)
    else:
        print("✅ Quality Gate Pass: All structural protocols are correctly implemented by concrete classes.")
        sys.exit(0)

if __name__ == '__main__':
    main()
