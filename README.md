
## About

<br>

The `sphinx_needs_data_explorer` is a web application written in HTML, CSS, and JavaScript, provided as a [Sphinx](https://www.sphinx-doc.org/en/master/index.html) extension. It enhances the interactivity of your Sphinx-generated documentation by enabling you to explore <a href="needs.json">Sphinx-Needs-Data</a> generated by the [Sphinx-Needs-Extension](https://www.sphinx-needs.com).

## Goals and Realization

<br>

![](doc/source/images/sphinx_needs_data_explorer.svg)

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
- hierarchical with repulsion

![](doc/source/images/network-perspective.jpg)

<br>

#### `Table-View`
In Table-View-Perspective you can see sphinx-needs data in table. You can select which columns should
be visible and which hidden.

![](doc/source/images/table-perspective.jpg)

<br>

#### `File-View`
In File-View-Perspective, you can see a list of files in which Sphinx-needs data were found.

![](doc/source/images/file-perspective.jpg)

<br>

### Powerfull Interactive Data Filtering
You can predefine filtering expressions during documentation generation or interactively while browsing documentation, and apply the data filtering across all three view perspectives.

![](doc/source/images/data-filtering.jpg)

You can use attribute lookup table while writing your filters.

![](doc/source/images/scr6.jpg)

<br>

### Exploring In-Neighbours, Out-Neighbours or both

![](doc/source/images/sh2.jpg)

<br>

### Visualizing Constraint Violations in Network Transitions 

![](doc/source/images/scr7.jpg)

<br>

### Controlling Neighborhood Depth in Network Visualization

![](doc/source/images/depthview.gif)

<br>

### Switching between Perspective Views and Documentation

![](doc/source/images/sh3.jpg)

<br>

### Interaction

![](doc/source/images/sphinx-needs-data-explorer.gif)

<br>

## Installation

You can install [sphinx-needs-data-explorer](https://pypi.org/project/sphinx-needs-data-explorer/) with pip

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

or you can include it only if the extension is available in your virtual environment:

    ...
    try:
        import sphinx-needs-data-explorer
        extensions.add('sphinx-needs-data-explorer')
    except ImportError:
        pass
    ...
    needs_build_json = True

<br>

If your project uses [sphinx_book_theme](https://github.com/executablebooks/sphinx-book-theme),
`sphinx_needs_data_explorer` supports full integration in your documentation by adding `E` header button accesible from any documentation page.

![](doc/source/images/E-header-button-doc.jpg)

Otherwise, you can create hyperlink to `sphinx_needs_data_explorer` by adding the following role in your .rst file(s)

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

![](doc/source/images/help1.jpg)


Visualizing Constraint Violations in Network Transitions:

    sphinx_needs_data_explorer_config = {
        "valid-linkage-color":"Black",
        "invalid-linkage-color":"OrangeRed",
        "valid-linkage":{
            'need': {
                'need':'refinement'
            },
            'feat': {
                'fear':'refinement',
                'need':'links'
            },
            ...
        }
    }

