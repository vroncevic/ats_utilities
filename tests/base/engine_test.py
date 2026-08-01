# -*- coding: UTF-8 -*-

'''
Module
    engine_test.py
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
    Unit tests for Base engine class.
'''

from __future__ import annotations

import unittest
from unittest.mock import MagicMock, patch

from ats_utilities.base.engine import Base
from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.info.imanager import IInfoManager
from ats_utilities.option.imanager import IOptionManager
from ats_utilities.splash.imanager import ISplashManager
from ats_utilities.generation.imanager import IGeneratorManager
from ats_utilities.exceptions import ATSValueError, ATSTypeError


class ConcreteBase(Base):
    """A concrete implementation of the Base class for testing purposes."""

    def process(self, verbose: bool = False) -> bool:
        return True


@patch("ats_utilities.base.engine.BaseValidator")
class TestBaseEngine(unittest.TestCase):
    """Unit tests for the Base orchestrator engine class."""

    def setUp(self) -> None:
        """Set up standard context and component bundle mocks."""
        self.mock_context = MagicMock(spec=ContextBundle)
        self.mock_info_manager = MagicMock(spec=IInfoManager)
        self.mock_option_manager = MagicMock(spec=IOptionManager)
        self.mock_splash_manager = MagicMock(spec=ISplashManager)
        self.mock_generation_manager = MagicMock(spec=IGeneratorManager)

        # By default, configure components to report they are initialized
        self.mock_info_manager.is_initialized.return_value = True
        self.mock_option_manager.is_initialized.return_value = True
        self.mock_splash_manager.is_initialized.return_value = True
        self.mock_generation_manager.is_initialized.return_value = True

        # Build mock configuration BaseBundle
        self.mock_bundle = MagicMock(spec=BaseBundle)
        self.mock_bundle.context_bundle = self.mock_context
        self.mock_bundle.info_manager = self.mock_info_manager
        self.mock_bundle.option_manager = self.mock_option_manager
        self.mock_bundle.splash_manager = self.mock_splash_manager
        self.mock_bundle.generation_manager = self.mock_generation_manager

    def test_initialization_success_with_generator(self, mock_val: MagicMock) -> None:
        """Test successful initialization and readiness flags when the generator is enabled."""
        base_instance = ConcreteBase(self.mock_bundle)

        self.assertEqual(base_instance.get_context(), self.mock_context)
        self.assertTrue(base_instance.is_initialized())
        self.assertEqual(base_instance._generation_manager, self.mock_generation_manager)

    def test_initialization_success_without_generator(self, mock_val: MagicMock) -> None:
        """Test successful initialization and readiness flags when the generator is None."""
        self.mock_bundle.generation_manager = None
        base_instance = ConcreteBase(self.mock_bundle)

        self.assertEqual(base_instance.get_context(), self.mock_context)
        self.assertTrue(base_instance.is_initialized())
        self.assertIsNone(base_instance._generation_manager)

    def test_initialization_fails_when_component_uninitialized(self, mock_val: MagicMock) -> None:
        """Test that if any sub-component is uninitialized, the engine reports uninitialized."""
        self.mock_info_manager.is_initialized.return_value = False

        base_instance = ConcreteBase(self.mock_bundle)
        self.assertFalse(base_instance.is_initialized())

    def test_initialization_invalid_bundle(self, mock_val: MagicMock) -> None:
        """Test validation check faults when passing an invalid configuration bundle type."""
        # When validation fails, we want it to raise the error
        mock_val.validate.side_effect = ATSValueError("invalid bundle")
        with self.assertRaises(ATSValueError):
            ConcreteBase(None)  # type: ignore

        mock_val.validate.side_effect = ATSTypeError("invalid bundle type")
        with self.assertRaises(ATSTypeError):
            ConcreteBase(MagicMock())  # type: ignore

    def test_get_bundle(self, mock_val: MagicMock) -> None:
        """Test that get_bundle returns a valid BaseBundle mirroring the attributes."""
        base_instance = ConcreteBase(self.mock_bundle)
        bundle = base_instance.get_bundle()

        self.assertIsInstance(bundle, BaseBundle)
        self.assertEqual(bundle.context_bundle, self.mock_context)
        self.assertEqual(bundle.info_manager, self.mock_info_manager)
        self.assertEqual(bundle.option_manager, self.mock_option_manager)
        self.assertEqual(bundle.splash_manager, self.mock_splash_manager)
        self.assertEqual(bundle.generation_manager, self.mock_generation_manager)

    def test_update_bundle_success(self, mock_val: MagicMock) -> None:
        """Test updating base bundle successfully."""
        base_instance = ConcreteBase(self.mock_bundle)
        new_info_manager = MagicMock(spec=IInfoManager)
        new_info_manager.is_initialized.return_value = True

        new_bundle = BaseBundle(
            context_bundle=self.mock_context,
            info_manager=new_info_manager,
            option_manager=self.mock_option_manager,
            splash_manager=self.mock_splash_manager,
            generation_manager=self.mock_generation_manager
        )

        mock_val.validate.side_effect = None
        self.assertTrue(base_instance.update_bundle(new_bundle))
        self.assertEqual(base_instance._info_manager, new_info_manager)

    def test_update_bundle_failure(self, mock_val: MagicMock) -> None:
        """Test update_bundle failure when validation fails."""
        base_instance = ConcreteBase(self.mock_bundle)
        bad_bundle = MagicMock(spec=BaseBundle)
        bad_bundle.context_bundle = None

        mock_val.validate.side_effect = ATSValueError("invalid")
        self.assertFalse(base_instance.update_bundle(bad_bundle))

    def test_process_delegation(self, mock_val: MagicMock) -> None:
        """Test process method implementation."""
        base_instance = ConcreteBase(self.mock_bundle)
        self.assertTrue(base_instance.process(verbose=True))

    @patch("ats_utilities.base.engine.to_str")
    def test_string_representation(self, mock_to_str: MagicMock, mock_val: MagicMock) -> None:
        """Test reflection serialization mappings upon string requests."""
        base_instance = ConcreteBase(self.mock_bundle)
        mock_to_str.return_value = "Base{_is_initialized=True}"

        result = str(base_instance)

        mock_to_str.assert_called_once_with(base_instance)
        self.assertEqual(result, "Base{_is_initialized=True}")


if __name__ == '__main__':
    unittest.main()
