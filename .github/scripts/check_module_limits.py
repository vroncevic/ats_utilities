# -*- coding: UTF-8 -*-

'''
Module
    check_module_limits.py
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
    Defines attribute(s) and function(s) for module limits check support.
'''

from __future__ import annotations

import os
import sys

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'1.0.0'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'


MAX_LINE_LENGTH = 150
MAX_MODULE_LINES = 500

def main():
    package_dir = 'ats_utilities'
    errors = []

    for root, _, files in os.walk(package_dir):
        for file in files:
            if not file.endswith('.py'):
                continue
            
            path = os.path.join(root, file)

            try:
                with open(path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                total_lines = len(lines)

                if total_lines > MAX_MODULE_LINES:
                    errors.append(
                        f"❌ Module Length Violation: '{path}' has {total_lines} lines "
                        f"(Max allowed is {MAX_MODULE_LINES})."
                    )

                for line_num, line in enumerate(lines, 1):
                    clean_line = line.rstrip('\r\n')

                    if len(clean_line) > MAX_LINE_LENGTH:
                        errors.append(
                            f"❌ Line Length Violation in '{path}' at line {line_num}: "
                            f"Length is {len(clean_line)} chars (Max allowed is {MAX_LINE_LENGTH})."
                        )
                        
            except Exception as e:
                errors.append(f"❌ Error reading file '{path}': {e}")

    if errors:
        for err in errors:
            print(err)

        print("---")
        print("Quality Gate Failed! Module size/line limits exceeded.")
        sys.exit(1)
    else:
        print("✅ Quality Gate Pass: Module limits (lines & line lengths) are respected.")
        sys.exit(0)

if __name__ == '__main__':
    main()