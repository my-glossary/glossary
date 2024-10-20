============
Sphinx links
============

`Cross-referencing syntax <https://www.sphinx-doc.org/en/master/usage/referencing.html#cross-referencing-syntax>`_

Link to sections by their title
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add `extension <https://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html#module-sphinx.ext.autosectionlabel>`_.

.. code-block:: python
   :caption: conf.py

   extensions = [
       ...
       # Allow reference sections using its title
       # https://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html#module-sphinx.ext.autosectionlabel
       'sphinx.ext.autosectionlabel',
       ...
   ]

Target::

   ====================
   Sphinx configuration
   ====================

Link::

   :ref:`Sphinx configuration`

Link, if config.py: autosectionlabel_prefix_document = True::

   :ref:`subroot/path/doc:Sphinx configuration`

Context::

   To configure Sphinx, see the :ref:`Sphinx configuration` and
   :ref:`Sphinx packages` sections.

Link to sections by ref label
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Cross-referencing arbitrary locations <https://www.sphinx-doc.org/en/master/usage/referencing.html#cross-referencing-arbitrary-locations>`_

Target::

   .. _run_stop_app:

   Run and stop application
   ------------------------

Link::

   :ref:`<run_stop_app>`

Context::

   For start and stop application use :ref:`commands <run_stop_app>`.

Link to sections :doc: Vs :ref: Vs :obj:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add to ``doc.rst`` or ``module.py``.

test_mentorship.rst::

   Test :doc:`Mentorship page </testing/tests_plw/pages/mentorship>`

test_mentorship.py::

   """
   Test :ref:`testing/tests_plw/pages/mentorship:Mentorship page`
   """

test_mentorship.py::

   """
   Test :doc:`Mentorship page </testing/tests_plw/pages/mentorship>`
   """

see :obj: on `stackoverflow <https://stackoverflow.com/questions/45282320/sphinx-link-to-a-method-of-a-class-in-another-module-in-python-docstring>`_

link to class of test_mentorship.py::

   """
   Test :obj:`Mentorship page <tests_plw.pages.mentorship.MentorshipProfilePage>`
   """

link to test_mentorship.py::

   """
   Test :obj:`Mentorship page <tests_plw.pages.mentorship>`
   """
