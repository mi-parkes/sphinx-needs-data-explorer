
## About

<br>

`sphinx_needs_data_explorer` enhances the interactivity of your Sphinx <br> generated documentation by enabling you to explore [Sphinx-Needs](https://www.sphinx-needs.com) data.

## Goals and Realization

<br>

![](doc/source/_static/images/sphinx_needs_data_explorer.svg)

<br>

## Features

### Three Sphinx-Needs Data View Perspectives

#### `Network-View`
In Network-View-Perspective you can see how sphinx-needs data are interconnected in data networks.

You can choose which **data context** to see
- incoming connections from in-neighbours
- outgoing connections from out-neighbours
- incoming and outgoing connections

You can choose **network layout**
- hierarchical bottom-up
- hierarchical right-to-left
- hierarchical with hierarchicalRepulsion

![](doc/source/_static/images/network-perspective.jpg)

<br>

#### `Table-View`
In Table-View-Perspective you can see sphinx-needs data in table. You can select which columns should
be visible and which hidden.

![](doc/source/_static/images/table-perspective.jpg)

<br>

#### `File-View`
In File-View-Perspective, you can see a list of files in which Sphinx-needs data were found.

![](doc/source/_static/images/file-perspective.jpg)

<br>

### Powerfull Interactive Data Filtering
You can predefine filtering expressions during documentation generation or interactively while browsing documentation, and apply the data filtering across all three view perspectives.

![](doc/source/_static/images/data-filtering.jpg)

<br>

### Exploring In-Neighbours, Out-Neighbours or both

![](doc/source/_static/images/sh2.jpg)

<br>

### Switching between Perspective Views and Documentation

![](doc/source/_static/images/sh3.jpg)

<br>

### Interaction

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

<br>

If your project uses [sphinx_book_theme](https://github.com/executablebooks/sphinx-book-theme),
`sphinx_needs_data_explorer` supports full integration in your documentation by adding `E` header button accesible from any documentation page.

![](doc/source/_static/images/E-header-button-doc.jpg)

Otheriwse, you can create hyperlink to `sphinx_needs_data_explorer` by adding the following role in your .rst file(s)

    :sphinx_needs_data_explorer:`Sphinx Needs Data Explorer Test`

## Configuration

If defined, the following parameters are used for configuration:

* [needs_extra_options](https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-extra-options) - the parameter defines extra sphinx-needs options
* [needs_extra_links](https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-extra-links) - the parameter defines the type links to use when extracting sphinx-needs linkage
* [needs_types](https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-types) - the parameter defines sphinx-needs types and their attributes like node colors

You can predefine filtering expressions to populate the filter drop-down list:

    sphinx_needs_data_explorer_config = {
        "filters":[
            "status=='open'",
            "['15','16'] in id",
            "title ~ /r.*[0-9]+5'$/i",
            "type != 'req' && incoming==[]",
            "type=='spec' && outgoing!=[] && title ~ /5'$/"
        ]
    }

`sphinx_needs_data_explorer` Help lists all attributes found in your project that can be used for data filtering.

![](doc/source/_static/images/help1.jpg)