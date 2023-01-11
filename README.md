This repository provides various dashboards that can be imported into Grafana to visualize the Prometheus metrics that Vertica supports. Dashboards can be downloaded from the Release section. Each time we Release a dashboard here it is uploaded to grafana.com. You can either download the JSON here or import it directly from grafana.com using the dashboard ID.

# Dashboards

Unless otherwise stated, all released dashboards will be compatible with new versions of the server. Pay attention to new dashboards as they may use metrics that are only available in a specific Vertica version. This chart will show compatibility of all of the released dashboards.

## vertica-cluster-overview.json
* Title: Vertica Overview
* Description: Provides a general overview of a cluster. This is meant as the initial landing page in Grafana.
* grafana.com Dashboard ID: 12603

| Revision | Release | Vertica Server (min) | Vertica Server (max) |
| --- | --- | --- | --- |
| 1 | 1.0.0 | 12.0.4 |

## vertica-queries.json
* Title: Vertica Queries
* Description: Provides detailed information about queries that are running in the cluster.
* grafana.com Dashboard ID: 12604

| Revision | Release | Vertica Server (min) | Vertica Server (max) |
| --- | --- | --- | --- |
| 1 | 1.0.0 | 12.0.4 |

## vertica-resource-management.json
* Title: Vertica Resource Management
* Description: Provides insight into the usage of the various resource pools
* grafana.com Dashboard ID: 12605

| Revision | Release | Vertica Server (min) | Vertica Server (max) |
| --- | --- | --- | --- |
| 1 | 1.0.0 | 12.0.4 |

<details><summary>Dashboard table template</summary>
## dashboard name
* Title: *Provide a title for the dashboard*
* Description: *provide a description of the dashboard*
* grafana.com Dashboard ID: *the ID of the dashboard in grafana.com*

| Revision | Release | Vertica Server (min) | Vertica Server (max) |
| --- | --- | --- | --- |
| *Revision of dashboard in grafana.com* | *GitHub release that provided this dashboard* | *Minimum Vertica server version needed* | *If dashboard doesn't work on latest Vertica, this is the final version where it works.* |
</details>

# Contributing

We welcome contributions to this repository. Detailed information in [CONTRIBUTING.md](CONTRIBUTING.md)
