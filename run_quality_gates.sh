#!/bin/bash
#
# @brief   ats_utilities
# @version v1.0.1
# @date    Sat Aug 11 09:58:41 2017
# @company None, free software to use 2017
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 gates/gates/interfaces_checker.py ats_utilities
python3 gates/gates/isp_checker.py ats_utilities
python3 gates/gates/limits_checker.py ats_utilities
python3 gates/gates/srp_checker.py ats_utilities

echo "Done"
