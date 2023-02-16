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


def test_json_expected_fields(dashboard_json):
    j = dashboard_json
    # Look for well-known fields that the JSON must have
    expected_fields = ["uid", "title", "tags", "panels", "schemaVersion",
                       "version", "description", "links"]
    for ef in expected_fields:
        assert ef in j


def test_vertica_tag(dashboard_json):
    j = dashboard_json
    print(j["tags"])
    assert "vertica" in j["tags"]


def test_stable_uid(dashboard_json):
    dashboard_name = dashboard_json['file_name']
    deployment_type = dashboard_json['deployment_type']
    # The uids is going to the dashboard name striped of its suffix, plus the
    # deployment type
    assert dashboard_name.endswith(".json")
    uid = "vertica-{}-{}".format(deployment_type,
                                 dashboard_name[:-len(".json")])
    assert dashboard_json["uid"] == uid


def test_dashboard_link(dashboard_json):
    j = dashboard_json
    assert "links" in j
    links = j['links']
    assert len(links) == 1
    assert links[0]["asDropdown"] is True
    assert links[0]["includeVars"] is True
    assert links[0]["keepTime"] is True
    assert links[0]["targetBlank"] is False
    assert len(links[0]["tags"]) == 1
    assert links[0]["tags"][0] == "vertica"
    assert links[0]["title"] == "Dashboards"
    assert links[0]["type"] == "dashboards"


def test_refresh(dashboard_json):
    j = dashboard_json
    assert "refresh" in j
    # All dashboards must have 5s refresh by default
    assert j["refresh"] == "5s"
