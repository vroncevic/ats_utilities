# -*- coding: UTF-8 -*-

'''
Module
    run_coverage.py
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
    Run and create code coverage statistics for ats_utilities.
'''

from unittest import TestLoader, TextTestRunner, TestSuite
from coverage import Coverage

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.2'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


if __name__ == "__main__":

    project_name: str = 'ats_utilities'
    cov: Coverage = Coverage(source=[project_name])
    cov.start()

    loader: TestLoader = TestLoader()
    suite: TestSuite = loader.discover(start_dir='tests', pattern='*_test.py', top_level_dir='.')
    runner: TextTestRunner = TextTestRunner(verbosity=2)
    runner.run(suite)

    cov.stop()
    cov.save()

    print("\n--- Coverage Report ---")
    cov.report()
    cov.json_report(outfile=f'{project_name}.json')
    cov.xml_report(outfile=f'{project_name}.xml')
    
    cov.html_report(directory='htmlcov')
    print("\nHTML report generated in 'htmlcov/' directory.")
