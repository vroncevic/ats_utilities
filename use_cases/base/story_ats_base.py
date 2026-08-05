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

from ats_utilities.base.engine import Base
from ats_utilities.base.setup.factory import BaseBundleFactory
from ats_utilities.base.setup.options import BaseBundleOptions
from ats_utilities.context.factory import ContextBundleFactory
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.reporter.ireporter import IReporter

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2026, https://vroncevic.github.io/ats_utilities'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__ = '3.4.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'

class MyTool(Base):
    '''Concrete implementation of Base for use case illustration.'''

    _INFO_FILE: str = '../../tests/assets/config/read_only/ats_cli_cfg_api.cfg'
    _logger: ILogger
    _reporter: IReporter

    def __init__(self):
        '''Initialize MyTool instance.'''
        current_dir: str = dirname(realpath(__file__))
        super().__init__(
            BaseBundleFactory.create_bundle(
                options=BaseBundleOptions(
                    info_file=f'{current_dir}/{self._INFO_FILE}',
                    use_generator=False,
                    context_bundle=ContextBundleFactory.create_bundle()
                )
            )
        )
        self._logger = self.get_context().logger
        self._reporter = self.get_context().reporter
        self._splash_manager.show()

        self._logger.write_log('Log: MyTool initialized successfully', INFO)
        self._reporter.success(['Report: MyTool initialized successfully'])

    def process(self, verbose: bool = True) -> bool:
        self._logger.write_log(f'Log: Processing starting, verbose: {verbose}', INFO)
        self._reporter.verbose(verbose, [f'Report: Processing starting, verbose: {verbose}'])
        print(f'Overwrite result {verbose} ...')
        return verbose

    def perform_action(self) -> None:
        '''A new method showing logging and reporting with different levels and colors.'''
        self._logger.write_log('Log: Performing a specific tool action', INFO)
        self._logger.write_log('Log: This is a warning log from MyTool action', WARNING)
        self._reporter.warning(['Report: This is a colored warning from MyTool'])
        self._reporter.error(['Report: This is a colored error from MyTool'])


if __name__ == "__main__":
    tool: MyTool = MyTool()

    result: bool = False
    print(f'Result: {result}')

    if tool.is_initialized():
        result = tool.process(True)
        tool.perform_action()

    print(f'Result: {result}')
