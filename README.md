
## About

<br>

`sphinx_needs_data_explorer` enhances the interactivity of your Sphinx <br> generated documentation by enabling you to explore [Sphinx-Needs](https://www.sphinx-needs.com) data.

## Goals and Realization

<br>

![](doc/source/_static/images/sphinx_needs_data_explorer.svg)

<br>

## Screenshots

**Example 1:** exploring In-Neighbours, Out-Neighbours or both

![](doc/source/_static/images/sh2.jpg)

<br>

**Example 2:** switching between network visualization and documentation

![](doc/source/_static/images/sh3.jpg)

<br>

**Example 3:** interaction

![](doc/source/_static/sphinx-needs-data-explorer.gif)

<br>

## Installation

You can install the package with pip (TBD)

    pip install sphinx-needs-data-explorer

Alternatively (Linux)

    git clone https://github.com/mi-parkes/sphinx-needs-data-explorer.git
    cd sphinx-needs-data-explorer
    
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r doc/requirements.txt
    
    python3 -m build --wheel
    pip install dist/sphinx_needs_data_explorer*.whl

## Activation

In your conf.py configuration file, add `sphinx_needs_data_explorer` to your extensions list. And, please, make sure that `sphinx_needs` extension is configured to generate needs.json file in the root of your documentation E.g.:

    extensions = [
      ...
      'sphinx_needs_data_explorer'
      ...
    ]
    ...
    needs_build_json = True


You can create hyperlink to `sphinx_needs_data_explorer` by adding the following role in your .rst file(s)

    :sphinx_needs_data_explorer:`Sphinx Needs Data Explorer Test`

## Configuration

If defined, the following parameters are used for configuration:

* [needs_extra_options](https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-extra-options) - the parameter defines extra sphinx-needs options
* [needs_extra_links](https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-extra-links) - the parameter defines the type links to use when extracting sphinx-needs linkage
* [needs_types](https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-types) - the parameter defines sphinx-needs types and their attributes like node colors

You can define filtering expressions to populate the filter drop-down list:

    sphinx_needs_data_explorer_config = {
        "filters":[
            "status=='open'",
            "['15','16'] in id",
            "title ~ /r.*[0-9]+5'$/i"
        ]
    }
