Sphinx Needs Data Explorer
##########################

The ``sphinx_needs_data_explorer`` is a web application built with HTML, CSS, and JavaScript, offered
as a `Sphinx <https://www.sphinx-doc.org/en/master/index.html>`_ extension. Created as a personal
open-source project, it enhances the interactivity of Sphinx-generated documentation by enabling 
users to explore the `needs.json <https://mi-parkes.github.io/sphinx-needs-data-explorer/needs.json>`_ 
data produced by the `Sphinx-Needs <https://www.sphinx-needs.com>`_ extension. Users can filter data 
attributes and view the data in three distinct modes: `network-view`_,
`table-view`_ , and `file-view`_.
Additionally, it supports generating reports in various formats, making it a powerful and flexible 
tool for analyzing and presenting documentation data.

Goals and Realization
#####################

.. image:: https://raw.githubusercontent.com/mi-parkes/sphinx-needs-data-explorer/41b530aa785343e4d378f0a5664ce520b158ed16/doc/source/images/sphinx_needs_data_explorer.svg

Features
########

Three Sphinx-Needs Data View Perspectives
=========================================

Network-View
--------------
In Network-View-Perspective you can see how sphinx-needs data are interconnected in data networks.

You can choose which **data context** to see
- incoming connections from in-neighbours
- outgoing connections from out-neighbours
- incoming and outgoing connections

You can choose **network layout**
- hierarchical bottom-up
- hierarchical right-to-left
- hierarchical with repulsion

.. image:: https://raw.githubusercontent.com/mi-parkes/sphinx-needs-data-explorer/41b530aa785343e4d378f0a5664ce520b158ed16/doc/source/images/network-perspective.jpg

Table-View
------------
In Table-View-Perspective you can see sphinx-needs data in table. You can select which columns should
be visible and which hidden.

.. image:: https://raw.githubusercontent.com/mi-parkes/sphinx-needs-data-explorer/41b530aa785343e4d378f0a5664ce520b158ed16/doc/source/images/table-perspective.jpg

File-View
-----------
In File-View-Perspective, you can see a list of files in which Sphinx-needs data were found.

.. image:: https://raw.githubusercontent.com/mi-parkes/sphinx-needs-data-explorer/41b530aa785343e4d378f0a5664ce520b158ed16/doc/source/images/file-perspective.jpg

Powerfull Interactive Data Filtering
====================================
You can predefine filtering expressions during documentation generation or interactively while browsing documentation, and apply the data filtering across all three view perspectives.

.. image:: https://raw.githubusercontent.com/mi-parkes/sphinx-needs-data-explorer/41b530aa785343e4d378f0a5664ce520b158ed16/doc/source/images/data-filtering.jpg

You can use attribute lookup table while writing your filters.

.. image:: https://raw.githubusercontent.com/mi-parkes/sphinx-needs-data-explorer/41b530aa785343e4d378f0a5664ce520b158ed16/doc/source/images/scr6.jpg

Exploring In-Neighbours, Out-Neighbours or both
===============================================
.. image:: https://raw.githubusercontent.com/mi-parkes/sphinx-needs-data-explorer/41b530aa785343e4d378f0a5664ce520b158ed16/doc/source/images/sh2.jpg

Visualizing Constraint Violations in Network Transitions 
=========================================================

.. image:: https://raw.githubusercontent.com/mi-parkes/sphinx-needs-data-explorer/41b530aa785343e4d378f0a5664ce520b158ed16/doc/source/images/scr7.jpg


Controlling Neighborhood Depth in Network Visualization
=========================================================

.. image:: https://raw.githubusercontent.com/mi-parkes/sphinx-needs-data-explorer/41b530aa785343e4d378f0a5664ce520b158ed16/doc/source/images/depthview.gif


Switching between Perspective Views and Documentation
=========================================================

.. image:: https://raw.githubusercontent.com/mi-parkes/sphinx-needs-data-explorer/41b530aa785343e4d378f0a5664ce520b158ed16/doc/source/images/sh3.jpg

Interaction
============

.. image:: https://raw.githubusercontent.com/mi-parkes/sphinx-needs-data-explorer/41b530aa785343e4d378f0a5664ce520b158ed16/doc/source/images/sphinx-needs-data-explorer.gif

Installation
============

You can install `sphinx-needs-data-explorer <https://pypi.org/project/sphinx-needs-data-explorer/>`_ with pip

.. code-block::

  pip install sphinx-needs-data-explorer

Alternatively (Linux)

.. code-block:: bash

  git clone https://github.com/mi-parkes/sphinx-needs-data-explorer.git
  cd sphinx-needs-data-explorer

  poetry install
  poetry build
  poetry run task doc

  # you can then install the package in your virtual environment
  pip install dist/sphinx_needs_data_explorer*.whl

Activation
============

In your conf.py configuration file, add `sphinx_needs_data_explorer` to your extensions list. And, please, make sure that `sphinx_needs` extension is configured to generate needs.json file in the root of your documentation E.g.:

.. code-block:: python

  extensions = [
    ...
    'sphinx_needs_data_explorer'
    ...
  ]
  ...
  needs_build_json = True

or you can include it only if the extension is available in your virtual environment:

.. code-block:: python

  ...
  try:
      import sphinx_needs_data_explorer
      extensions.add('sphinx_needs_data_explorer')
  except ImportError:
      pass
  ...
  needs_build_json = True

If your project uses `sphinx_book_theme <https://github.com/executablebooks/sphinx-book-theme>`_,
`sphinx_needs_data_explorer` supports full integration in your documentation by adding `E` header button accesible from any documentation page.

.. image:: https://raw.githubusercontent.com/mi-parkes/sphinx-needs-data-explorer/41b530aa785343e4d378f0a5664ce520b158ed16/doc/source/images/E-header-button-doc.jpg

Otherwise, you can create hyperlink to `sphinx_needs_data_explorer` by adding the following role in your .rst file(s)

.. code-block:: rst

    :sphinx_needs_data_explorer:`Sphinx Needs Data Explorer Test`

Configuration
=============
If defined, the following parameters are used for configuration:

* `needs_extra_options <https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-extra-options>`_ - the parameter defines extra sphinx-needs options
* `needs_extra_links <https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-extra-links>`_ - the parameter defines the type links to use when extracting sphinx-needs linkage
* `needs_types <https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-types>`_ - the parameter defines sphinx-needs types and their attributes like node colors

You can predefine filtering expressions to populate the filter drop-down list:

.. code-block:: python

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

.. image:: https://raw.githubusercontent.com/mi-parkes/sphinx-needs-data-explorer/41b530aa785343e4d378f0a5664ce520b158ed16/doc/source/images/help1.jpg

Visualizing Constraint Violations in Network Transitions:

.. code-block:: python

  sphinx_needs_data_explorer_config = {
      "valid-linkage-color":"Black",
      "invalid-linkage-color":"OrangeRed",
      "valid-linkage":{
          'need': {
              'need':'refinement'
          },
          'feat': {
              'feat':'refinement',
              'need':'links'
          },
          ...
      }
  }

