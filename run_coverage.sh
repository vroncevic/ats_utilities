#!/bin/bash
#
# @brief   ats_utilities
# @version v1.0.1
# @date    Sat Aug 11 09:58:41 2017
# @company None, free software to use 2017
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 ats_coverage.py -n ats_utilities
pylint ats_utilities > ats_utilities.report
echo "Done"
