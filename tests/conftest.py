# (c) Copyright [2023] Micro Focus or one of its affiliates.
# Licensed under the Apache License, Version 2.0 (the "License");
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from os import walk
import pytest
import json


def pytest_addoption(parser):
    parser.addoption(
        "--directory",
        action="store",
        default=None,
        required=True,
        help="Directory to find dashboards",
    )


def pytest_generate_tests(metafunc):
    if "dashboard_file" in metafunc.fixturenames:
        d = metafunc.config.getoption("directory")
        filenames = next(walk(d), (None, None, []))[2]
        parms = [f"{d}/{f}" for f in filenames]
        metafunc.parametrize("dashboard_file", parms)


@pytest.fixture
def dashboard_json(dashboard_file):
    with open(dashboard_file, "r") as f:
        j = json.load(f)
    # Add our own extra meta-data so that its available for test
    j['full_path'] = dashboard_file
    j['file_name'] = os.path.basename(dashboard_file)
    return j
