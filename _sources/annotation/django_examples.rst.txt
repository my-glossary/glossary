==========================
Django annotation examples
==========================

.. seealso::

   * `mypy-django <https://github.com/machinalis/mypy-django>`_

.. code-block:: python

   def get(self, request: HttpRequest, *args: object, **kwargs: object) -> HttpResponse:

   def get_context_data(self, **kwargs: object) -> Dict[str, object]: ...

   def get_redirect_url(self, *args: object, **kwargs: object) -> Optional[str]: ...
