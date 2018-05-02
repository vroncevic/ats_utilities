# -*- coding: UTF-8 -*-
# __init__.py
# Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# ats_utilities is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ats_utilities is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.
#

import sys
from inspect import stack

try:
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ###################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class BaseSlots(object):
    """
        Define class BaseSlots with attribute(s) and method(s).
        App/Tool/Script settings utilities, property for class slots.
        It defines:
            attribute:
                __CLASS_SLOTS__ - Tuple for collecting class slots
            method:
                __init__ - Initial constructor
                __extract_class_name - Getting class name (absolute path)
                __setattr__ - Setting attribute to instance of object
                __getattr__ - Getting attribute from instance of object
    """

    __CLASS_SLOTS__ = ()

    def __init__(self):
        """
            Initial constructor.
        """
        pass

    @classmethod
    def __extract_class_name(cls, class_absolute_path):
        """
            Getting class name from class absolute path.
            :param class_absolute_path: Python class path
            :type class_absolute_path: <Python class>
            :return: Python class name
            :rtype: <str>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func = stack()[0][3]
        expected_txt = 'Argument: expected class_absolute_path <str> object'
        expected_msg = "{0} {1} {2}".format('def', func, expected_txt)
        if class_absolute_path is None or not class_absolute_path:
            raise ATSBadCallError(expected_msg)
        if not isinstance(class_absolute_path, str):
            raise ATSTypeError(expected_msg)
        class_path_no_quote = class_absolute_path.replace('\'', '')
        class_path = class_path_no_quote.replace('<', '').replace('>', '')
        class_name = class_path.split('.')[-1]
        return class_name

    def __setattr__(self, attr_name, attr_value):
        """
            Setting attribute to instance of object.
            :param attr_name: Attribute name (class)
            :type attr_name: <Python object>
            :param attr_value: Attribute value
            :type attr_value: <Python object>
            :exceptions: AttributeError
        """
        cls, read_only = self.__class__, 'VERBOSE'
        class_name = cls.__extract_class_name(str(cls))
        format_exc_txt = "Add field \"{0}\" to {1}.__CLASS_SLOTS__"
        parent_classes = cls.__bases__
        # Single-inheritance: protected class
        if parent_classes == (BaseSlots, ):
            for field in cls.__CLASS_SLOTS__:
                if attr_name == read_only:
                    message = "{0}{1}".format('Read only field: ', read_only)
                    raise AttributeError(message)
                else:
                    if field != read_only:
                        class_field_path = "_{0}{1}".format(class_name, field)
                        if class_field_path == attr_name:
                            object.__setattr__(self, attr_name, attr_value)
                        else:
                            message = "{0}".format(
                                format_exc_txt.format(attr_name, class_name)
                            )
                            raise AttributeError(message)
        else:
            # Multi-inheritance: protected class
            print(len(parent_classes))
            for parent_class in parent_classes:
                print(parent_class)

    def __getattr__(self, attr):
        """
            Getting attribute from instance of object.
            :param attr: Attribute field (class)
            :type attr: <Python object>
            :exceptions: AttributeError
        """
        cls = self.__class__
        class_name = cls.__extract_class_name(str(cls))
        not_empty = bool(cls.__CLASS_SLOTS__)
        if not not_empty:
            return None
        else:
            if attr not in cls.__CLASS_SLOTS__:
                message = "{0}".format(
                    'Add field "{0}" to {1}.__CLASS_SLOTS__'.format(
                        attr, class_name
                    )
                )
                raise AttributeError(message)
            return self.attr
