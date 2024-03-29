VENV := $(PWD)/.venv
PYTHON := python
PIP := $(PYTHON) -m pip

VERSION := $(file < VERSION)

.PHONY: help lint package clean

help:	# The following lines will print the available commands when entering just 'make'
ifeq ($(UNAME), Linux)
	@grep -P '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
else
	@awk -F ':.*###' '$$0 ~ FS {printf "%15s%s\n", $$1 ":", $$2}' \
		$(MAKEFILE_LIST) | grep -v '@awk' | sort
endif

venv3: ### Creates a virtual environment for this project
	test -d $(VENV) || python3.8 -m venv $(VENV)
	$(PIP) install --upgrade pip wheel setuptools twine
	$(PIP) install -r requirements-dev.txt

clean: clean-build clean-pyc ### Cleans artifacts

clean-build: ### Removes builds
	find . -type d -iname "build" ! -path "./.venv/*" -exec rm -rf {} +
	find . -type d -iname "dist" ! -path "./.venv/*" -exec rm -rf {} +
	find . -type d -iname "*.egg-info" ! -path "./.venv/*" -exec rm -rf {} +

clean-env: ### Removes environment directory
	rm -rf $(VENV)

clean-pyc: ### Removes python compiled bytecode files
	find . -iname "*.pyc" ! -path "./.venv/*" -delete
	find . -type d -iname "__pycache__" ! -path "./.venv/*" -exec rm -rf {} +


define BUILD
	echo $(version) > VERSION && \
	cd src/$1/ && rm -rf dist/ && $(PYTHON) setup.py bdist_wheel
endef

define INSTALL
	$(PIP) install src/$1/dist/ydata_$(subst -,_,$1)-$(VERSION)-py2.py3-none-any.whl
endef

define UPLOAD
	cd src/$1/ && $(PYTHON) -m twine upload -r ydata dist/*
endef

build-core:
	$(call BUILD,core)

build-datascience:
	$(call BUILD,datascience)

build-all: build-core build-datascience ### Build all packages

upload-core:
	$(call UPLOAD,core)

upload-datascience:
	$(call UPLOAD,datascience)

upload-all: upload-core upload-datascience ### Upload all packages to pypi

lint-core: ### Run prospector
	$(PYTHON) -m prospector src/core

lint-datascience: ### Run prospector
	$(PYTHON) -m prospector src/datascience

lint: lint-core lint-datascience ### Run prospector on all packages

define LINK_LOCAL
	$(PIP) install -e src/$1
endef

link-core:
	echo "0.0.0" > src/core/VERSION
	$(call LINK_LOCAL,core)

link-datascience:
	echo "0.0.0" > src/datascience/VERSION
	$(call LINK_LOCAL,datascience)

link-all: link-core link-datascience ### Link all packages

test: link-all ### Runs the tests
	$(PYTHON) -m pytest src/core
