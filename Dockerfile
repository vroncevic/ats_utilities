# Copyright 2017 - 2025 Vladimir Roncevic <elektron.ronca@gmail.com>
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

FROM ubuntu:20.04
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive \
    apt-get install -yq --no-install-recommends \
    nano \
    tree \
    htop \
    wget \
    curl \
    unzip \
    ca-certificates \
    openssl \
    python3 \
    python3-dev \
    libyaml-dev \
    python3-wheel \
    python3-pip \
    python3-setuptools \
    python3-build \
    python3-bs4 \
    python3-colorama \
    python3-yaml

RUN mkdir /ats_utilities/
COPY ats_utilities /ats_utilities/
COPY setup.cfg /
COPY pyproject.toml /
COPY MANIFEST.in /
COPY setup.py /
COPY README.md /
COPY LICENSE /
RUN python3 -m build --no-isolation --wheel
RUN python3 -m pip install /dist/ats_utilities-*-py3-none-any.whl
RUN rm -rf /ats_utilities*
RUN rm -rf dist/
RUN rm -rf tests/
RUN rm -f setup.cfg
RUN rm -f pyproject.toml
RUN rm -f MANIFEST.in
RUN rm -f setup.py
RUN rm -f README.md
RUN rm -f LICENSE
