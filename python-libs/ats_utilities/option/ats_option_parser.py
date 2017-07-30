# encoding: utf-8

from optparse import OptionParser

from ats_utilities.error.lookup_error import AppError

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ATSOptionParser(object):
    """
    Define class ATSOptionParser with attribute(s) and method(s).
    Create option parser and process arguments from start.
    It defines:
        attribute:
            VERBOSE - Verbose prefix text
            __opt_parser - Options parser
        method:
            __init__ - Initial constructor
            add_operation - Adding option to App/Tool/Script
            parese_args - Process arguments from start
    """

    VERBOSE = '[ATS_OPTION_PARSER]'

    def __init__(self, version, epilog, description, verbose=False):
        """
        Setting version, epilog and description of App/Tool/Script.
        :param version: App/Tool/Script version and build date
        :type: str
        :param epilog: App/Tool/Script long description
        :type: str
        :param description: App/Tool/Script author and license
        :type: str
        :param verbose: Enable/disable verbose option
        :type verbose: bool
        """
        if verbose:
            msg = ATSOptionParser.VERBOSE
            print(msg)
        try:
            if version and epilog and description:
                self.__opt_parser = OptionParser(
                    version=version, epilog=epilog, description=description
                )
            else:
                msg = 'missing option parser argument(s)!'
                raise AppError(msg)
        except AppError as e:
            print("Error: ", e)

    def add_operation(self, *args, **kwargs):
        """
        Adding option to App/Tool/Script.
        :param args: List of arguments
        :type: Python object(s)
        :param kwargs: Options and texts
        :type: Python object(s)
        """
        self.__opt_parser.add_option(*args, **kwargs)

    def parse_args(self, argv):
        """
        Process arguments from start.
        :param argv: Arguments
        :type: Python object(s)
        :return: Options and arguments
        :rtype: Python object(s)
        """
        (opts, args) = self.__opt_parser.parse_args(argv)
        return opts, args
