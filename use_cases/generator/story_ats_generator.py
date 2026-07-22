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
from ats_utilities.generator.generator_registry import GeneratorRegistry
from ats_utilities.generator.gen_params_registry import GenParamsRegistry
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.registry import ContextRegistry

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'

# Paths to the generated archive and scheme
dir_path = os.path.dirname(os.path.abspath(__file__))
context_bundle: ContextBundle = ContextRegistry.create_default_context_bundle()

#
# Use Case 1: High-level generation using Generator orchestrator
# ==============================================================
#
print("Use Case 1: High-level generation using Generator orchestrator:")
generator_bundle: GeneratorBundle = GeneratorRegistry.create_default_generator_bundle(context_bundle)
generator = Generator(own=generator_bundle)
status: bool = False

# Archive and scheme paths for use case 1
archive1 = os.path.join(dir_path, 'templates.tgz')
scheme1 = os.path.join(dir_path, 'scheme.json')

# Output target directory for use case 1
target_dir1 = tempfile.mkdtemp()
template_key1 = 'base'
template_values1 = {'project_name': 'my_hexagonal_app'}

print(f"Extracting '{template_key1}' project to: {target_dir1}")
print(f"Project Name: {template_values1['project_name']}")

# Run generator for use case 1
status = generator.generate(
    GenParamsRegistry.create_gen_params_bundle(
        archive_path=archive1,
        target_dir=target_dir1,
        template_key=template_key1,
        scheme=scheme1,
        template_values=template_values1
    )
)

if status:
    print("Project successfully generated!")
    print("Generated files:")
    for root, dirs, files in os.walk(target_dir1):
        for file in files:
            rel_dir = os.path.relpath(root, target_dir1)
            if rel_dir == '.':
                print(f"  {file}")
            else:
                print(f"  {rel_dir}/{file}")
else:
    print("Project generation failed.")

print("\n" + 50 * "=" + "\n")

#
# Use Case 2: Generating a mini web service from a custom archive and JSON scheme
# ==============================================================================
#
print("Use Case 2: Generating a custom mini web service from a new archive and scheme:")

# Archive and scheme paths for use case 2
archive2 = os.path.join(dir_path, 'mini_service_templates.tgz')
scheme2 = os.path.join(dir_path, 'mini_service_templates.json')

target_dir2 = tempfile.mkdtemp()
template_values2 = {
    'project_name': 'my_billing_service',
    'service_name': 'my_billing_service',
    'service_name_camel': 'MyBillingService',
    'service_name_upper': 'MY_BILLING_SERVICE'
}

print(f"Extracting 'mini_service' project to: {target_dir2}")
print(f"Service Name: {template_values2['service_name']}")

# Run generator for use case 2
status = generator.generate(
    GenParamsRegistry.create_gen_params_bundle(
        archive_path=archive2,
        target_dir=target_dir2,
        template_key='mini_service',
        scheme=scheme2,
        template_values=template_values2
    )
)

if status:
    print("Project successfully generated!")
    print("Generated files:")
    for root, dirs, files in os.walk(target_dir2):
        for file in files:
            rel_dir = os.path.relpath(root, target_dir2)
            if rel_dir == '.':
                print(f"  {file}")
            else:
                print(f"  {rel_dir}/{file}")
else:
    print("Project generation failed.")
