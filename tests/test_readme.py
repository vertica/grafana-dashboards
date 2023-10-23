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

import git
from bs4 import BeautifulSoup
from markdown import markdown


def get_readme():
    repo = git.Repo('.', search_parent_directories=True)
    repo.working_tree_dir
    with open(f"{repo.working_tree_dir}/README.md", 'r') as f:
        ip = f.read()
    html = markdown(ip)
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def get_dashboards_in_readme():
    readme = get_readme()
    dashboards = {}
    for e in readme:
        if e.name == 'h2':
            dash = {}
            dashboards[e.text] = dash
        if e.name == 'ul':
            for le in e.find_all('li'):
                kv = le.text.split(":")
                if len(kv) < 2:
                    continue
                dash[kv[0]] = kv[1].strip()
    return dashboards


def get_dashboard_in_readme(dashboard_json):
    dashboards_in_readme = get_dashboards_in_readme()
    deployment_type = dashboard_json['deployment_type']
    print(deployment_type)
    dashboard_name = dashboard_json['file_name']
    print(dashboard_name)
    db_title = dashboard_name
    assert db_title in dashboards_in_readme, \
        f"Dashboard {db_title} is missing in README"
    return dashboards_in_readme[db_title]


def test_dashboard_exists(dashboard_json):
    readme = get_readme()
    dashboards = readme.find_all('h2')
    dashboard_json['file_name'] in dashboards


def test_description(dashboard_json):
    d = get_dashboard_in_readme(dashboard_json)
    assert "Description" in d, "Missing description of dashboard"
    assert "description" in dashboard_json
    assert d["Description"] == dashboard_json['description']


def test_title(dashboard_json):
    d = get_dashboard_in_readme(dashboard_json)
    assert "Title" in d, "Missing title of dashboard in readme"
    assert "title" in dashboard_json, "Missing title of dashboard in json"
    assert d["Title"] == dashboard_json['title']
