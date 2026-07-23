# -*- coding: UTF-8 -*-

'''
Module
    reflection_test.py
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
    Unit tests for reflection utilities.
'''

from __future__ import annotations

from typing import Any
import unittest

from ats_utilities.exceptions import ATSValueError, ATSAttributeError
from ats_utilities.utils.reflection import cls_name, get_pvt, has_attrs, to_str, instance_to_dict

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/ats_utilities'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/ats_utilities/blob/dev/LICENSE'
__version__: str = '3.4.4'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class DummyClass:
    '''
        Defines class DummyClass to test has_attrs decorator.

        It defines:

            :attributes:
                | _attr1 - Test attribute 1 (default None).
                | _attr2 - Test attribute 2 (default None).
            :methods:
                | __init__ - Initializes DummyClass constructor.
                | decorated_method - Method decorated with has_attrs.
    '''

    def __init__(self, attr1: Any = None, attr2: Any = None) -> None:
        '''
            Initializes DummyClass constructor.

            :param attr1: First attribute value | None.
            :type attr1: Any
            :param attr2: Second attribute value | None.
            :type attr2: Any
            :exceptions: None.
        '''
        self._attr1 = attr1
        self._attr2 = attr2

    @has_attrs('_attr1', '_attr2')
    def decorated_method(self) -> str:
        '''
            Method decorated with has_attrs.

            :return: Static string indicating successful execution.
            :rtype: str
            :exceptions: None.
        '''
        return "success"


class ReflectionTest(unittest.TestCase):
    '''
        Defines class ReflectionTest with attribute(s) and method(s).
        Tests factory reflection utility functions.

        It defines:

            :attributes: None.
            :methods:
                | test_get_pvt - Tests get_pvt function.
                | test_has_attrs_success - Tests has_attrs when attributes are non-empty.
                | test_has_attrs_empty_but_allowed - Tests has_attrs when attributes are 0 or False.
                | test_has_attrs_missing_or_empty - Tests has_attrs when attributes are missing or empty.
                | test_cls_name - Tests cls_name function.
                | test_to_str_empty - Tests to_str with an instance having no attributes.
                | test_to_str_with_attributes - Tests to_str with an instance having attributes.
    '''

    def test_get_pvt(self) -> None:
        '''
            Tests get_pvt function.

            :exceptions: None.
        '''
        instance = DummyClass("val1", "val2")
        self.assertEqual(get_pvt(instance, "_attr1"), "val1")
        self.assertEqual(get_pvt(instance, "attr1"), "val1")

    def test_has_attrs_success(self) -> None:
        '''
            Tests has_attrs when attributes are non-empty.

            :exceptions: None.
        '''
        instance = DummyClass("val1", "val2")
        self.assertEqual(instance.decorated_method(), "success")

    def test_has_attrs_empty_but_allowed(self) -> None:
        '''
            Tests has_attrs when attributes are 0 or False.

            :exceptions: None.
        '''
        instance1 = DummyClass(0, False)
        self.assertEqual(instance1.decorated_method(), "success")

    def test_has_attrs_missing_or_empty(self) -> None:
        '''
            Tests has_attrs when attributes are missing or empty.

            :exceptions: None.
        '''
        instance = DummyClass(None, "val2")
        with self.assertRaises(ATSValueError) as ctx:
            instance.decorated_method()
        self.assertIn("missing or empty attribute _attr1", str(ctx.exception))

        instance2 = DummyClass("", "val2")
        with self.assertRaises(ATSValueError) as ctx:
            instance2.decorated_method()
        self.assertIn("missing or empty attribute _attr1", str(ctx.exception))

        instance3 = DummyClass([], "val2")
        with self.assertRaises(ATSValueError) as ctx:
            instance3.decorated_method()
        self.assertIn("missing or empty attribute _attr1", str(ctx.exception))

    def test_cls_name(self) -> None:
        '''
            Tests cls_name function.

            :exceptions: None.
        '''
        instance = DummyClass()
        self.assertEqual(cls_name(instance), "DummyClass")

    def test_to_str_empty(self) -> None:
        '''
            Tests to_str with an instance having no attributes.

            :exceptions: None.
        '''
        class EmptyClass:
            pass

        instance = EmptyClass()
        expected = f"EmptyClass at 0x{id(instance):x}"
        self.assertEqual(to_str(instance), expected)

    def test_to_str_with_attributes(self) -> None:
        '''
            Tests to_str with an instance having attributes.

            :exceptions: None.
        '''
        instance = DummyClass("val1", 42)
        v1_id = f"0x{id('val1'):x}"
        v2_id = f"0x{id(42):x}"
        inst_id = f"0x{id(instance):x}"

        result = to_str(instance)

        self.assertIn("attr1=val1", result)
        self.assertIn("attr2=42", result)
        
        self.assertIn(f"val1 at {v1_id}", result)
        self.assertIn(f"42 at {v2_id}", result)
        self.assertTrue(result.endswith(f") at {inst_id}"))

        class CustomVal:
            def __str__(self) -> str:
                return f"custom at 0x{id(self):x}"

        custom_val_inst = CustomVal()
        custom_inst = DummyClass(custom_val_inst, "other")
        res_custom = to_str(custom_inst)
        self.assertIn(f"custom at 0x{id(custom_val_inst):x}", res_custom)
        self.assertNotIn(f"custom at 0x{id(custom_val_inst):x} at", res_custom)

        # Test with a non-primitive type that doesn't contain its id in str representation
        list_inst = DummyClass([1, 2], "other")
        list_id = f"0x{id(list_inst._attr1):x}"
        res_list = to_str(list_inst)
        self.assertIn(f"[1, 2] at {list_id}", res_list)

    def test_instance_to_dict(self) -> None:
        '''
            Tests instance_to_dict function.
        '''
        from dataclasses import dataclass

        @dataclass
        class DummyDataclass:
            a: int
            b: str

        inst = DummyDataclass(a=1, b="test")
        result = instance_to_dict(inst)
        self.assertEqual(result, {"a": 1, "b": "test"})

    def test_instance_to_dict_none(self) -> None:
        '''
            Tests instance_to_dict raises ATSValueError when instance is None.
        '''
        with self.assertRaises(ATSValueError):
            instance_to_dict(None)

    def test_instance_to_dict_invalid_type(self) -> None:
        '''
            Tests instance_to_dict raises ATSAttributeError when instance is not a dataclass.
        '''
        class NonDataclass:
            pass

        with self.assertRaises(ATSAttributeError):
            instance_to_dict(NonDataclass())


if __name__ == "__main__":
    unittest.main()
