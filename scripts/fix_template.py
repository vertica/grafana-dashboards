#!/bin/env python

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
import sys
import getopt
import json


def main(argv):
    directory = ''
    opts, args = getopt.getopt(argv, "hd:", ["directory="])
    for opt, arg in opts:
        if opt == '-h':
            print('fix_template.py -d <directory>')
            sys.exit()
        elif opt in ("-d", "--directory"):
            directory = arg
    # Directly get filenames in the specified directory
    filenames = next(walk(directory), (None, None, []))[2]
    # Filter out only JSON files (assuming all dashboard files are JSON)
    json_files = [f for f in filenames if f.endswith('.json')]
    # Construct the full paths for these files
    parms = [os.path.join(directory, f) for f in json_files]
    for p in parms:
        remove_selected_text(p)
    print("============= Dashboards are valid now ==============")


def remove_selected_text(dashboard_file):
    with open(dashboard_file, "r") as f:
        j = json.load(f)
    templating_list = j['templating']['list']
    # Remove the last selected value for each dashboard variable
    for t in templating_list:
        if 'current' in t:
            t.pop('current')
    with open(dashboard_file, "w") as f:
        json.dump(j, f, indent=2, sort_keys=True, ensure_ascii=False)


if __name__ == "__main__":
    main(sys.argv[1:])
