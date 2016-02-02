octogrid
========

    GitHub following network visualizer for Humans

.. image:: https://img.shields.io/pypi/v/octogrid.svg?style=flat-square
    :target: https://pypi.python.org/pypi/octogrid/
    :alt: Latest Version
    
.. image:: https://img.shields.io/badge/Python-2.6%2C%202.7-brightgreen.svg?style=flat-square
    :target: https://pypi.python.org/pypi/octogrid/
    :alt: Supported Python versions
    
.. image:: https://img.shields.io/pypi/l/octogrid.svg?style=flat-square
    :target: https://pypi.python.org/pypi/octogrid/
    :alt: License

.. image:: https://img.shields.io/pypi/dm/octogrid.svg?style=flat-square
    :target: https://pypi.python.org/pypi/octogrid/
    :alt: Downloads

Installation
~~~~~~~~~~~~
    pip install octogrid

Usage
~~~~~
- **octogrid generate [--reset] [--user=<username>]**

    Generate the GML file for user representing its GitHub following graph

- **octogrid publish [--reset] [--user=<username>]**

    Publish the user's GitHub community graph using Plotly
    
**--reset** (*optional*) flag is used to clear the cache storage for a given user

octogrid in action
~~~~~~~~~~~~~~~~~~
.. figure:: https://raw.githubusercontent.com/pravj/octogrid/master/docs/github-network.png
   :alt: Communities in GitHub Following Network for @pravj

License
~~~~~~~~~~~~
    MIT © `Pravendra Singh <http://pravj.github.io>`_.