Sphinx Needs Data Explorer
==========================

About
-----
**sphinx_needs_data_explorer** adds more interactivity when exploring
`Sphinx-Needs <https://github.com/useblocks/sphinx-needs>`_ data defined 
in your Sphinx generated documentation.

.. image:: _static/sphinx-needs-data-explorer.gif

|

See :sphinx_needs_data_explorer:`Sphinx-Needs-Data-Explorer` in action.

Installation
------------

.. code-block::

  pip install sphinx-needs-data-explorer

Activation
----------

In your conf.py configuration file, add **sphinx_needs_data_explorer** to your extensions list. 
And, please, make sure that 'sphinx_needs' extension generates needs.json file in the root of 
your documentation E.g.:

.. code-block:: python

   extensions = [
      ...
      'sphinx_needs_data_explorer'
      ...
   ]
   ...
   needs_build_json = True

Configuration
-------------

The following configuration parameters are supported:

* link_types - defines lists of all link types in your traceability network to be explored
* type_color_map - assigns specific color to each Sphinx-Needs type

.. code-block:: python

   sphinx_needs_data_explorer_config={
      'link_types':['links','verifies'],
      'type_color_map': {
         'req'   :'#DEFFDC',
         'spec'  :'#FFFF99',
         'test'  :'#87CEFA'
      }
   }

Add the following role in your index.rst file.

.. code-block:: rst

  :sphinx_needs_data_explorer:`Sphinx-Needs Data Explorer`

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Demo Sphinx_Needs Project <demo.rst>

