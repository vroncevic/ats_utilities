# -*- coding: utf-8 -*-

try:
    from colorama import Fore
except ImportError as e:
    msg = "\n{0}\n".format(e)
    print(msg)
    exit(-1)  # Force close python module #####################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

"""
    ATS - Global stdout text part
    DBG - Setting blue console text
    ERR - Setting red console text
    RST - Reset color to default value
"""
ATS = 'App/Tool/Script'
DBG = Fore.BLUE
ERR = Fore.RED
RST = Fore.RESET
