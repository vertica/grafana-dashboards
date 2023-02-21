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
    deployment_types = next(walk(directory), (None, None, []))[1]
    parms = []
    for dpt in deployment_types:
        filenames = next(walk(f"{directory}/{dpt}"), (None, None, []))[2]
        dpt_parms = [f"{directory}/{dpt}/{f}" for f in filenames]
        parms.extend(dpt_parms)
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
