# -*- coding: utf-8 -*-

import sys

try:
    from ats_utilities.text.stdout_text import ATS, ATS_PROCESS, CON, RST
except ImportError as e:
    msg = "\n{0}\n".format(e)
    sys.exit(msg)  # Force close python ATS ###################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class info(object):
    """
    Define class info with attribute(s) and method(s).
    Define info decorator for print console mechanism.
    It defines:
        attribute:
            __func - Function object
        method:
            __init__ - Initial constructor
            __call__ - Dunder (magic) method
    """

    def __init__(self, function_object):
        """
        Setting function object.
        :param function_object: Function object
        :type function_object: <function>
        """
        has_call = hasattr(function_object, '__call__')
        if has_call:
            self.__func = function_object
        else:
            self.__func = None
            msg = "{0} [{1}]".format(
                'Expected <function> type of object, received type',
                type(function_object)
            )
            raise TypeError(msg)

    def __call__(self, *args, **kwargs):
        """
        Calling function.
        :param args: List of arguments (objects)
        :type args: <list>
        :param kwargs: Arguments in shape of dictionary
        :type kwargs: <dict>
        :return: Function object | None
        :rtype: <function> | <NoneType>
        """
        msg_prefix, msg_prefix_delimiter, msg_delimiter = ATS, '', ' '
        msg_merged = msg_delimiter.join(args)
        msg_debug = "{0}".format(msg_merged)
        for key_msg, val_msg in kwargs.items():
            if key_msg == ATS_PROCESS:
                msg_prefix = "[{0}{1}{2}]".format(CON, val_msg, RST)
        msg = "{0} {1}".format(msg_prefix, msg_debug)
        print(msg)
        has_call = hasattr(self.__func, '__call__')
        return self.__func(*args, **kwargs) if has_call else None
