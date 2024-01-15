Sphinx Needs Data Explorer
==========================

:sphinx_needs_data_explorer:`Test Sphinx-Needs Data Explorer`

About
-----
**sphinx_needs_data_explorer** adds more interactivity when exploring
`Sphinx-Needs <https://github.com/useblocks/sphinx-needs>`_ data defined 
in your Sphinx generated documentation.

Installation
------------

.. code-block::

  pip install sphinx-needs-data-explorer

Activation
----------

In your conf.py configuration file, add **sphinx_needs_data_explorer** to your extensions list. 
And, please, make sure that 'sphinx_needs' extension generates needs.json file in the root of 
your documentation E.g.:

.. code-block::

   extensions = [
      ...
      'sphinx_needs_data_explorer'
      ...
   ]
   ...
   needs_build_json = True


Add the following role in your index.rst file or in any other convenient place(s) in your documentation project.

.. code-block::

  :sphinx_needs_data_explorer:`Sphinx-Needs Data Explorer`

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Demo Sphinx_Needs Project <demo.rst>

