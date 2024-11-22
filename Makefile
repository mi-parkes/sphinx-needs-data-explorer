.ONESHELL:
SHELL=/bin/bash
.SHELLFLAGS = -e -c

UNAME := $(shell uname 2>/dev/null || echo Windows)

ifeq ($(UNAME),Linux)
endif

ifeq ($(UNAME),Darwin)
endif

help:
	echo "$(MAKE) install         # Rebuild and reinstall sphinx_needs_data_explorer"
	echo "$(MAKE) installx        # Reinstall sphinx_needs_data_explorer in active virtual environment"
	echo "$(MAKE) html            # Build sphinx_needs_data_explorer documentation"
	echo "$(MAKE) webserver       # Run webserver hosting sphinx_needs_data_explorer documentation in docker container"
	echo "$(MAKE) show            # View the documentation for sphinx_needs_data_explorer, which is hosted on a server running nginx, in a web browser"
	echo "$(MAKE) show-session    # View stored sesion"

helpx:
	echo "$(MAKE) prep-release    # Prepare release data"
	echo "$(MAKE) upload-package  # Uplaod package to PYPI"

$(VERBOSE).SILENT:
	echo

install:
	rm -rf build dist doc/build
	poetry install

prep-release:
	rm -rf build dist doc/build
	poetry install
#	poetry build
	poetry build -f sdist
	tar -tf dist/*.tar.gz

installx:
	pip uninstall sphinx-needs-data-explorer -y
	pip install dist/sphinx_needs_data_explorer*.whl

html:
	source doc/.venv/bin/activate
	$(MAKE) -C doc clean html

WEBSERVERPORT=8080

webserver:
	docker ps | awk '$$NF=="sphinx_needs_data_explorer"{print "docker stop "$$1}' | bash
	sleep 1
	docker run -it --rm -d -p $(WEBSERVERPORT):80 --name sphinx_needs_data_explorer -v $$PWD/doc/build/html:/usr/share/nginx/html nginx

show:
	open http://localhost:$(WEBSERVERPORT)

ifeq ($(UNAME),Darwin)
gshow:
	open -a '/Applications/Google Chrome.app' http://localhost:$(WEBSERVERPORT)

gshowx:
	open -a '/Applications/Google Chrome.app' http://localhost:$(WEBSERVERPORT)/_static/sphinx_needs_data_explorer.html
endif

show-session:
	open "http://localhost:$(WEBSERVERPORT)/_static/sphinx_needs_data_explorer.html?type=any&filter=&id=F00016+-+Title+of+%27F00016%27&layout=DU&view=2&viewModeMaxDepth=2&mode=0"
-include ../tests.mak

new-install:
	$(eval VENV=.venv)
	python3 -m venv $(VENV)
	source $(VENV)/bin/activate
	python -m pip install --upgrade pip
	pip install poetry

	echo source $(VENV)/bin/activate

test-package-cur:
	$(MAKE) test-package BRANCH=`git branch | awk '$$1=="*"{print $$2}'`

test-package:
	$(eval WDIR=/tmp/test)
	$(eval BRANCH=main)
	mkdir -p $(WDIR)
	rm -rf $(WDIR)/*
	cd $(WDIR)
	git clone -b $(BRANCH) --single-branch \
			https://github.com/mi-parkes/sphinx-needs-data-explorer.git
	cd sphinx-needs-data-explorer
#	poetry install --only test,docs
	poetry install
	poetry build
	poetry run task doc

test-package2:
	$(eval WDIR=/tmp/test)
	$(eval BRANCH=main)
	mkdir -p $(WDIR)
	rm -rf $(WDIR)/*
	cd $(WDIR)
	git clone -b $(BRANCH) --single-branch \
			https://github.com/mi-parkes/sphinx-needs-data-explorer.git
	cd sphinx-needs-data-explorer
	gsed -iE 's,^name\s*=\s*"sphinx_needs_data_explorer",name="test",'  pyproject.toml
	rm -rf sphinx_needs_data_explorer
	poetry add -G doc sphinx-needs-data-explorer
	poetry install --no-root
	poetry run task doc
	code .

test-package-show:
	$(eval WDIR=/tmp/test)
	cd $(WDIR)/sphinx-needs-data-explorer
	$(MAKE) webserver show

show-package:
	tar -tvf dist/sphinx_needs_data_explorer-*.tar.gz

clean-dc:
	docker images | awk '$$1=="<none>"{print "docker rmi "$$3}' | bash

mindmap:	
	java -jar $(PLANTUML_PATH) -v \
		-tpng doc/source/_static/puml/sphinx_needs_data_explorer.puml \
		-o $(CURDIR)/doc/source/images
	java -jar $(PLANTUML_PATH) -v \
		-tsvg doc/source/_static/puml/sphinx_needs_data_explorer.puml \
		-o $(CURDIR)/doc/source/images
