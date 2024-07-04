#!/bin/bash
#
# @brief   ats_utilities
# @version v1.0.1
# @date    Sat Aug 11 09:58:41 2017
# @company None, free software to use 2017
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf htmlcov ats_utilities_coverage.xml ats_utilities_coverage.json .coverage
python3 -m coverage run -m --source=../ats_utilities unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html -d htmlcov
python3 -m coverage xml -o ats_utilities_coverage.xml 
python3 -m coverage json -o ats_utilities_coverage.json
python3 -m coverage report --format=markdown -m
python3 ats_coverage.py -n ats_utilities
