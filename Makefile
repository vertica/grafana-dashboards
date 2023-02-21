# VERSION defines the next GitHub version
VERSION ?= 1.0.0

REPO_DIR:=$(dir $(word $(words $(MAKEFILE_LIST)),$(MAKEFILE_LIST)))

default: help

# Setting SHELL to bash allows bash commands to be executed by recipes.
# Options are set to exit when a recipe line exits non-zero or a piped command fails.
SHELL = /usr/bin/env bash -o pipefail
.SHELLFLAGS = -ec

##@ General

# The help target prints out all targets with their descriptions organized
# beneath their categories. The categories are represented by '##@' and the
# target descriptions by '##'. The awk commands is responsible for reading the
# entire set of makefiles included in this invocation, looking for lines of the
# file as xyz: ## something, and then pretty-format the target and help. Then,
# if there's a line with ##@ something, that gets pretty-printed as a category.
# More info on the usage of ANSI control characters for terminal formatting:
# https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_parameters
# More info on the awk command:
# http://linuxcommand.org/lc3_adv_awk.php

.PHONY: help
help: ## Display this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  \033[36m%-25s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(firstword $(MAKEFILE_LIST))

##@ Commands

.PHONY: test
test: pep8 ## Verify the dashboards
	pytest --verbose --directory=$(REPO_DIR)/dashboards

.PHONY: fix-template 
fix-template: ## Remove fields related to a dashboard run
	./scripts/fix_template.py --directory=$(REPO_DIR)/dashboards

.PHONY: pep8
pep8: ## Ensures python code conforms to PEP8
	pycodestyle tests/*py scripts/*py

.PHONY: fix-pep8
fix-pep8: ## Automatically fixes any PEP8 violations
	autopep8 --in-place tests/*py scripts/*py
