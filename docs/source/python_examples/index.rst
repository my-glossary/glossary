###############
Python examples
###############

.. code-block:: python
   :emphasize-lines: 6

   >>> capitals.update({
   ...     "Lebanon": "Beirut",
   ...     "Norway": "Oslo",
   ...     "France": "Paris",
   ... })
   >>> [capitals.get(k) for k in ("Lebanon", "Norway", "Bahamas")]
   ['Beirut', 'Oslo', 'Nassau']

