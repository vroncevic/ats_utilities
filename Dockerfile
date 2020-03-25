# Copyright 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

FROM debian:10
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends python python-pip tree
RUN mkdir /ats_utilities/
COPY ats_utilities /ats_utilities/
COPY setup.py /
RUN find /ats_utilities/ -name "*.editorconfig" -type f -exec rm -Rf {} \;
RUN python setup.py install
RUN rm -rf /ats_utilities/
RUN rm -f setup.py
RUN chmod -R 755 /usr/local/lib/python2.7/dist-packages/
RUN tree /usr/local/lib/python2.7/dist-packages/ats_utilities/
