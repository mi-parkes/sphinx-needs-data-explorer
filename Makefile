.ONESHELL:
SHELL=/bin/bash

help:
	echo "$(MAKE) install    	# Rebuild and reinstall sphinx_needs_data_explorer"
	echo "$(MAKE) html       	# Build sphinx_needs_data_explorer documentation"
	echo "$(MAKE) webserver  	# Run webserver hosting sphinx_needs_data_explorer documentation in docker container"
	echo "$(MAKE) show       	# View the documentation for sphinx_needs_data_explorer, which is hosted on a server running nginx, in a web browser"
	echo "$(MAKE) show-session	# View stored sesion"

$(VERBOSE).SILENT:
	echo

doc/.venv:
	python3 -m venv doc/.venv
	source doc/.venv/bin/activate
	pip install -r doc/requirements.txt

install: doc/.venv
	source doc/.venv/bin/activate
	rm -rf build dist doc/build
	python -m build  --sdist --wheel
	pip uninstall sphinx-needs-data-explorer -y
	pip install dist/sphinx_needs_data_explorer*.whl

html:
	source doc/.venv/bin/activate
	$(MAKE) -C doc clean html

WEBSERVERPORT=8080

webserver:
	docker ps | awk '$$NF=="sphinx_needs_data_explorer"{print "docker stop "$$1}' | bash
	docker run -it --rm -d -p $(WEBSERVERPORT):80 --name sphinx_needs_data_explorer -v $$PWD/doc/build/html:/usr/share/nginx/html nginx

show:
	open http://localhost:$(WEBSERVERPORT)

show-session:
	open "http://localhost:$(WEBSERVERPORT)/_static/sphinx_needs_data_explorer.html?type=req&filter=status%3D%3D%27implemented%27&id=R_00005+-+Title+of+%27R_00005%27&layout=&view=2"
