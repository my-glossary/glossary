====
Code
====

.. code-block:: python

   class Meta:
       """Set model features."""

.. code-block:: python

   def __str__(self) -> str:
        """Provide the informal string representation of an object."""

.. code-block:: python

   def get_object(self, **kwargs):
       """Return the object the view is displaying."""

.. code-block:: python

   def get_queryset(self):
       """Return the `QuerySet` to look up the object."""

admin.py
""""""""

.. code-block:: python

   """Modul of models representation in the admin interface."""

apps.py
"""""""

.. code-block:: python
   :caption: apps.py

   """Configuration module of the Task application."""

.. code-block:: python
   :caption: class UsersConfig(AppConfig):

   """Configuration of the User application."""

urls

.. code-block:: python
   :caption: urls.py

   """User app urls module."""

models
""""""

.. code-block:: python
   :caption: __init__.py

   """Package of models of the Users application."""
