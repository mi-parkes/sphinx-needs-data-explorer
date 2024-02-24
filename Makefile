.ONESHELL:
SHELL=/bin/bash

help:

doc/.venv:
	python3 -m venv doc/.venv
	source doc/.venv/bin/activate
	pip install -r doc/requirements.txt

install: doc/.venv
	source doc/.venv/bin/activate
	rm -rf build dist doc/build
	python -m build  --sdist --wheel
	pip uninstall sphinx-needs-data-explorer -y
	pip install dist/sphinx_needs_data_explorer-0.8.0-py3-none-any.whl
	$(MAKE) -C doc clean html

installx:
	source doc/.venv/bin/activate
	$(MAKE) -C doc clean html

webserver:
	docker ps | awk '$$NF=="web"{print "docker stop "$$1}' | bash
	docker run -it --rm -d -p 8080:80 --name web -v $$PWD/doc/build/html:/usr/share/nginx/html nginx

show:
	open http://localhost:8080
