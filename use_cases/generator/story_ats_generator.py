# -*- coding: utf-8 -*-

'''
Module
    story_ats_generator.py
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
    Use cases for ATS generator.
'''

import os
import tempfile
from ats_utilities.generator.engine import Generator
from ats_utilities.generator.generator_bundle import GeneratorBundle
from ats_utilities.generator.scheme_loader import SchemeLoader
from ats_utilities.generator.tar_processor import TarProcessor
from ats_utilities.generator.tar_process_bundle import TarProcessBundle

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.3.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

# Paths to the generated archive and scheme
archive_path = '/data/dev/python/2_basic/2_design_patterns/hexagonal/hexagonal_templates.tgz'
scheme_path = '/data/dev/python/2_basic/2_design_patterns/hexagonal/hexagonal_templates.json'

#
# Use Case 1: High-level generation using Generator orchestrator
# ==============================================================
#
print("Use Case 1: High-level generation using Generator orchestrator:")
generator = Generator()

# Output target directory
target_dir = tempfile.mkdtemp()
template_key = 'gen_standalone'
template_values = {'project_name': 'my_hexagonal_app'}

print(f"Extracting '{template_key}' project to: {target_dir}")
print(f"Project Name: {template_values['project_name']}")

# Run generator
success = generator.generate(
    GeneratorBundle(
        archive_path=archive_path,
        target_dir=target_dir,
        template_key=template_key,
        scheme=scheme_path,
        template_values=template_values
    )
)

if success:
    print("Project successfully generated!")
    print("Generated files:")
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            rel_dir = os.path.relpath(root, target_dir)
            if rel_dir == '.':
                print(f"  {file}")
            else:
                print(f"  {rel_dir}/{file}")
else:
    print("Project generation failed.")

print("\n" + 50 * "=" + "\n")

#
# Use Case 2: Modular usage using SchemeLoader and TarProcessor directly
# ======================================================================
#
print("Use Case 2: Modular usage using SchemeLoader and TarProcessor directly:")
loader = SchemeLoader()
processor = TarProcessor()

# Load and resolve the scheme
resolved_scheme = loader.load(scheme_path)

# Extract config for tool_standalone project
template_key2 = 'tool_standalone'
project_scheme = resolved_scheme[template_key2]
source_dir = project_scheme['source_dir']
path_replacements = project_scheme['path_replacements']
exclude_patterns = project_scheme['exclude']

# Define target dir and computed values
target_dir2 = tempfile.mkdtemp()
vals = {
    'project_name': 'my_standalone_tool',
    'project_name_dashed': 'my-standalone-tool',
    'project_name_camel': 'MyStandaloneTool',
    'project_name_upper': 'MY_STANDALONE_TOOL'
}

print(f"Extracting '{template_key2}' project directly to: {target_dir2}")

# Run processor
processor.process(
    TarProcessBundle(
        archive_path=archive_path,
        target_dir=target_dir2,
        source_dir=source_dir,
        path_replacements=path_replacements,
        exclude_patterns=exclude_patterns,
        vals=vals
    )
)
print("Modular project successfully generated!")

print("\n" + 50 * "=" + "\n")

#
# Use Case 3: Generating a mini web service from a custom archive and JSON scheme
# ==============================================================================
#
print("Use Case 3: Generating a custom mini web service from a new archive and scheme:")

# Define paths for the new mini service archive and scheme
mini_archive = os.path.join(os.path.dirname(__file__), 'mini_service_templates.tgz')
mini_scheme = os.path.join(os.path.dirname(__file__), 'mini_service_templates.json')

generator3 = Generator()
target_dir3 = tempfile.mkdtemp()
template_values3 = {
    'project_name': 'my_billing_service',
    'service_name': 'my_billing_service',
    'service_name_camel': 'MyBillingService',
    'service_name_upper': 'MY_BILLING_SERVICE'
}

print(f"Extracting 'mini_service' project to: {target_dir3}")
print(f"Service Name: {template_values3['service_name']}")

# Run generator
success3 = generator3.generate(
    GeneratorBundle(
        archive_path=mini_archive,
        target_dir=target_dir3,
        template_key='mini_service',
        scheme=mini_scheme,
        template_values=template_values3
    )
)

if success3:
    print("Mini service successfully generated!")
    print("Generated files:")
    for root, dirs, files in os.walk(target_dir3):
        for file in files:
            rel_dir = os.path.relpath(root, target_dir3)
            if rel_dir == '.':
                file_path = os.path.join(target_dir3, file)
                print(f"  {file}")
            else:
                file_path = os.path.join(target_dir3, rel_dir, file)
                print(f"  {rel_dir}/{file}")
            
            # Print a snippet of file content to verify placeholder rendering
            if file.endswith('.py') or file.endswith('.md'):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    first_line = content.split('\n')[0] if content else ""
                    # If it's the __init__.py which is empty, get the second line or skip
                    if not first_line and len(content.split('\n')) > 1:
                        first_line = content.split('\n')[1]
                    print(f"    Content preview: {first_line}")
else:
    print("Mini service generation failed.")

