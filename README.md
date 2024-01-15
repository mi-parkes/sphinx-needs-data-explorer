## About

`sphinx_needs_data_explorer` adds new interactivity 
to your Sphinx generated documentation 
when exploring [Sphinx-Needs](https://github.com/useblocks/sphinx-needs) data.

## Installation

You can install the package with pip


    pip install sphinx-needs-data-explorer

## Activation

In your conf.py configuration file, add `sphinx_needs_data_explorer` to your extensions list. And, please, make sure that `sphinx_needs` extension is configured to generate needs.json file in the root of your documentation E.g.:

    extensions = [
      ...
      'sphinx_needs_data_explorer'
      ...
    ]
    ...
    needs_build_json = True


Then, add the `sphinx_needs_data_explorer` role in your index.rst file or in any other convenient place(s) in your documentation project.

    :sphinx_needs_data_explorer:`Sphinx-Needs Data Explorer`


In your conf.py configuration file, add this extension to your extensions list.