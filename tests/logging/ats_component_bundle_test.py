# -*- coding: UTF-8 -*-

'''
Module
    ats_component_bundle_test.py
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
    Creates test cases for checking LoggingComponentBundle.
'''

from __future__ import annotations

from unittest import TestCase, main
from unittest.mock import MagicMock

from ats_utilities.logging.component_bundle import LoggingComponentBundle
from ats_utilities.logging.logger.ilogger import ILogger
from ats_utilities.logging.logger.logger_bundle import LoggerBundle
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.exceptions import ATSValueError, ATSTypeError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '1.0.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class LoggingComponentBundleTestCase(TestCase):
    '''Test cases for LoggingComponentBundle.'''

    def test_logging_component_bundle(self) -> None:
        '''Test LoggingComponentBundle methods.'''
        mock_logger = MagicMock(spec=ILogger)
        mock_logger_bundle = LoggerBundle()
        mock_context = ContextBundle()
        bundle1 = LoggingComponentBundle()
        bundle2 = LoggingComponentBundle(
            logger=mock_logger,
            logger_bundle=mock_logger_bundle,
            context_bundle=mock_context
        )

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.logger, mock_logger)

        bundle1.validate()
        d = bundle1.to_dict()
        self.assertEqual(d['logger'], mock_logger)

    def test_logging_component_bundle_validation_errors(self) -> None:
        '''Test LoggingComponentBundle validation exceptions.'''
        mock_logger = MagicMock(spec=ILogger)
        mock_logger_bundle = LoggerBundle()
        mock_context = ContextBundle()

        fields = {
            'logger': mock_logger,
            'logger_bundle': mock_logger_bundle,
            'context_bundle': mock_context
        }

        for field in fields:
            bundle = LoggingComponentBundle(
                logger=mock_logger,
                logger_bundle=mock_logger_bundle,
                context_bundle=mock_context
            )
            setattr(bundle, field, None)
            with self.assertRaises(ATSValueError):
                bundle.validate()

        # Type validation errors
        bundle = LoggingComponentBundle(
            logger=mock_logger,
            logger_bundle=mock_logger_bundle,
            context_bundle=mock_context
        )
        bundle.logger = "not_a_logger"
        with self.assertRaises(ATSTypeError):
            bundle.validate()

        bundle = LoggingComponentBundle(
            logger=mock_logger,
            logger_bundle=mock_logger_bundle,
            context_bundle=mock_context
        )
        bundle.logger_bundle = "not_a_logger_bundle"
        with self.assertRaises(ATSTypeError):
            bundle.validate()

        bundle = LoggingComponentBundle(
            logger=mock_logger,
            logger_bundle=mock_logger_bundle,
            context_bundle=mock_context
        )
        bundle.context_bundle = "not_a_context_bundle"
        with self.assertRaises(ATSTypeError):
            bundle.validate()

        with self.assertRaises(ATSTypeError):
            bundle.merge("not_a_logging_component_bundle")

    def test_logging_component_bundle_merge_with_none(self) -> None:
        '''Test LoggingComponentBundle merge with None values.'''
        bundle1 = LoggingComponentBundle()
        bundle2 = LoggingComponentBundle()
        bundle2.logger_bundle = None
        bundle1.merge(bundle2)
        self.assertIsNotNone(bundle1.logger_bundle)



if __name__ == '__main__':
    main()
