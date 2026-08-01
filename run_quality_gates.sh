#!/bin/bash
#
# @brief   ats_utilities
# @version v1.0.1
# @date    Sat Aug 11 09:58:41 2017
# @company None, free software to use 2017
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 .github/scripts/check_interfaces.py
python3 .github/scripts/check_isp.py
python3 .github/scripts/check_module_limits.py
python3 .github/scripts/check_srp.py

echo "Done"
