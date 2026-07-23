# -*- coding: utf-8 -*-

'''
Module
    story_ats_version.py
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
    Use cases for ATS version.
'''

from logging import INFO, WARNING
from os.path import dirname, realpath
from typing import override

from ats_utilities.base.engine import Base
from ats_utilities.base.setup.factory import BaseFactory
from ats_utilities.context.factory import ContextFactory

__author__ = r'Vladimir Roncevic'
__copyright__ = r'(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = [r'Vladimir Roncevic', r'Python Software Foundation']
__license__ = r'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = r'3.4.3'
__maintainer__ = r'Vladimir Roncevic'
__email__ = r'elektron.ronca@gmail.com'
__status__ = r'Development'

class MyTool(Base):
    '''Concrete implementation of Base for use case illustration.'''

    _INFO_FILE: str = '../../tests/assets/config/read_only/ats_cli_cfg_api.cfg'

    def __init__(self):
        current_dir: str = dirname(realpath(__file__))
        super().__init__(
            BaseFactory.create_default_base_bundle(
                info_file=f'{current_dir}/{self._INFO_FILE}',
                context_bundle=ContextFactory.create_default_bundle()
            )
        )

        # Log that initialization is complete using both logger and reporter
        context = self.get_shared_context()
        my_logger = context.logger
        my_reporter = context.reporter

        my_logger.write_log('MyTool initialized successfully', INFO)
        my_reporter.success(['MyTool initialized successfully (Reporter Success)'])

    @override
    def process(self, verbose: bool = True) -> bool:
        context = self.get_shared_context()
        context.logger.write_log(f'Processing starting, verbose: {verbose}', INFO)
        context.reporter.verbose(verbose, [f'Processing starting, verbose: {verbose} (Reporter Verbose)'])
        print(f'Overwrite result {verbose} ...')
        return verbose

    def perform_action(self) -> None:
        '''A new method showing logging and reporting with different levels and colors.'''
        context = self.get_shared_context()
        context.logger.write_log('Performing a specific tool action', INFO)
        context.logger.write_log('This is a warning log from MyTool action', WARNING)

        # Color logs via reporter
        context.reporter.warning(['This is a colored warning from MyTool (Reporter Warning)'])
        context.reporter.error(['This is a colored error from MyTool (Reporter Error)'])

tool: MyTool = MyTool()

result: bool = False
print(f'Result: {result}')

if tool.is_initialized():
    result = tool.process(True)
    tool.perform_action()

print(f'Result: {result}')
print(str(tool))
