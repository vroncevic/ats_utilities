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
from ats_utilities.generator.scheme.scheme_loader import SchemeLoader
from ats_utilities.generator.tar.tar_processor import TarProcessor
from ats_utilities.generator.tar.tar_process_bundle import TarProcessBundle

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'

# Paths to the generated archive and scheme
archive_path = 'templates.tgz'
scheme_path = 'scheme.json'

#
# Use Case 1: High-level generation using Generator orchestrator
# ==============================================================
#
print("Use Case 1: High-level generation using Generator orchestrator:")
generator = Generator()

# Output target directory
target_dir = tempfile.mkdtemp()
template_key = 'base'
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
# Use Case 3: Generating a mini web service from a custom archive and JSON scheme
# ==============================================================================
#
print("Use Case 3: Generating a custom mini web service from a new archive and scheme:")

# Define paths for the new mini service archive and scheme
mini_archive = 'mini_service_templates.tgz'
mini_scheme = 'mini_service_templates.json'

generator2 = Generator()
target_dir2 = tempfile.mkdtemp()
template_values2 = {
    'project_name': 'my_billing_service',
    'service_name': 'my_billing_service',
    'service_name_camel': 'MyBillingService',
    'service_name_upper': 'MY_BILLING_SERVICE'
}

print(f"Extracting 'mini_service' project to: {target_dir2}")
print(f"Service Name: {template_values2['service_name']}")

# Run generator
success2 = generator2.generate(
    GeneratorBundle(
        archive_path=mini_archive,
        target_dir=target_dir2,
        template_key='mini_service',
        scheme=mini_scheme,
        template_values=template_values2
    )
)

if success2:
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

