# Copyright 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
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
RUN DEBIAN_FRONTEND=noninteractive \
    apt-get install -yq --no-install-recommends \
    vim \
    nano \
    tree \
    htop \
    wget \
    unzip \
    ca-certificates \
    openssl \
    python \
    python-dev \
    python3 \
    python3-dev \
    libyaml-dev

RUN wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
RUN python2 get-pip.py
RUN python2 -m pip install --upgrade setuptools
RUN python2 -m pip install --upgrade pip
RUN python2 -m pip install --upgrade build
RUN rm -f get-pip.py
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN python3 -m pip install --upgrade setuptools
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade build
RUN rm -f get-pip.py
RUN mkdir /ats_utilities/
COPY ats_utilities /ats_utilities/
COPY setup.cfg /
COPY pyproject.toml /
COPY MANIFEST.in /
COPY setup.py /
COPY README.md /
COPY LICENSE /
COPY requirements.txt /
RUN pip2 install -r requirements.txt
RUN pip3 install -r requirements.txt
RUN rm -f requirements.txt
RUN python2 -m build --no-isolation --wheel
RUN pip2 install /dist/ats_utilities-*-py2-none-any.whl
RUN python3 -m build --no-isolation --wheel
RUN pip3 install /dist/ats_utilities-*-py3-none-any.whl
RUN rm -rf /ats_utilities*
RUN rm -rf dist/ tests/
RUN rm -f setup.cfg
RUN rm -f pyproject.toml
RUN rm -f MANIFEST.in
RUN rm -f setup.py
RUN rm -f README.md
RUN rm -f LICENSE
