This repository contains dashboards that you can import into [Grafana](https://grafana.com/) to visualize time series metrics about Vertica. Each dashboard is available for download in JSON format from [Releases](https://github.com/vertica/grafana-dashboards/releases) or directly from [Grafana Dashboards](https://grafana.com/grafana/dashboards/).

# Dashboards

Unless explicitly noted, all dashboards are compatible with new Vertica server versions. The minimum supported Vertica version is listed with the release version in the following dashboard sections.

Some dashboards might use metrics that are available in specific Vertica versions. Review the [Prometheus metrics](https://docs.vertica.com/latest/en/admin/managing-db/https-service/prometheus-metrics/) to verify which metrics are available in each Vertica version.

## Cluster overview

`cluster-overview.json`

[![revision](https://img.shields.io/badge/revision-1-orange.svg)](https://example.com) [![release](https://img.shields.io/badge/release-1.0.0-green.svg)](https://github.com/vertica/grafana-dashboards/releases) [![Dashboard ID](https://img.shields.io/badge/Dashboard_ID-TBD-yellow.svg)](https://grafana.com/grafana/dashboards/?search=TBD) [![Vertica compatibility](https://img.shields.io/badge/Vertica-v23.3.0-blue.svg)](https://docs.vertica.com/latest/en/)

General cluster overview. This dashboard is designed to be the initial landing page in Grafana. This dashboard includes the following:

- Total number of nodes and their state, data size, and disk usage
- Query request and processing statistics
- User and license information
- Overall cluster health

## Queries

`queries.json`

[![revision](https://img.shields.io/badge/revision-1-orange.svg)](https://example.com) [![release](https://img.shields.io/badge/release-1.0.0-green.svg)](https://github.com/vertica/grafana-dashboards/releases) [![Dashboard ID](https://img.shields.io/badge/Dashboard_ID-TBD-yellow.svg)](https://img.shields.io/badge/Dashboard_ID-TBD-yellow.svg) [![Vertica compatibility](https://img.shields.io/badge/Vertica-v23.3.0-blue.svg)](https://docs.vertica.com/latest/en/)

Detailed information about [queries](https://docs.vertica.com/latest/en/data-analysis/queries/) that are currently running in a cluster. This dashboard includes the following:

- Total query request success and failure rate
- Completed and failed queries, per node and per resource pool
- User query type and execution time per type

## Resource management

`resource-management.json`

[![revision](https://img.shields.io/badge/revision-1-orange.svg)](https://example.com) [![release](https://img.shields.io/badge/release-1.0.0-green.svg)](https://github.com/vertica/grafana-dashboards/releases) [![Dashboard ID](https://img.shields.io/badge/Dashboard_ID-TBD-yellow.svg)](https://img.shields.io/badge/Dashboard_ID-TBD-yellow.svg) [![Vertica compatibility](https://img.shields.io/badge/Vertica-v23.3.0-blue.svg)](https://docs.vertica.com/latest/en/)

Details about [user-defined](https://docs.vertica.com/latest/en/sql-reference/statements/create-statements/create-resource-pool/) and [built-in](<(https://docs.vertica.com/latest/en/sql-reference/statements/create-statements/create-resource-pool/built-pools/)>) resource pool usage. This dashboard includes the following:

- Pool configuration values
- Per node pool memory usage, query activity, and queued requests statistics
- Queued request thresholds and memory usage
- Average running queries and their average execution time

## Depot

`depot.json`

[![revision](https://img.shields.io/badge/revision-1-orange.svg)](https://example.com) [![release](https://img.shields.io/badge/release-1.0.0-green.svg)](https://github.com/vertica/grafana-dashboards/releases) [![Dashboard ID](https://img.shields.io/badge/Dashboard_ID-TBD-yellow.svg)](https://img.shields.io/badge/Dashboard_ID-TBD-yellow.svg) [![Vertica compatibility](https://img.shields.io/badge/Vertica-v23.3.0-blue.svg)](https://docs.vertica.com/latest/en/)

Details about [depot](https://docs.vertica.com/latest/en/eon/depot-management/) usage. This dashboard includes the following:

- Current usage
- Lookup hits
- Fetches and evictions
- Uploads from depot to communal storage

# Contribute

Vertica welcomes contributions to this repository. For details, see [CONTRIBUTING.md](CONTRIBUTING.md)
