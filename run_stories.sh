#!/bin/bash
#
# @brief   ats_utilities
# @version v1.0.1
# @date    Sat Aug 11 09:58:41 2017
# @company None, free software to use 2017
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

for story in $(find use_cases/ -name "story_*.py"); do
    PYTHONPATH=. python3 "$story" > /dev/null 2>&1 && \
        echo "PASS: $story" || \
        echo "FAIL: $story"
done

rm -f run.log app.log

echo "Done"
