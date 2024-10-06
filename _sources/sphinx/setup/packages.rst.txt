===============
Sphinx packages
===============

Copy button from block
^^^^^^^^^^^^^^^^^^^^^^

To add button for copy text from code-block the package
`Sphinx-copybutton <https://sphinx-copybutton.readthedocs.io/en/latest/#sphinx-copybutton>`_

.. code-block:: console

   poetry add sphinx-copybutton

.. code-block:: python
   :caption: ./docs/source/conf.py

   extensions = [
    ...
    # Add copy button from block
    # https://sphinx-copybutton.readthedocs.io/en/latest/#sphinx-copybutton
    'sphinx_copybutton'
    ...
    ]
