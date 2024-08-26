======================
Python typing examples
======================

Передача необязательной функции, без аргументов, обратного вызова
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`"Fundamental building blocks", PEP 483 <https://peps.python.org/pep-0483/#fundamental-building-blocks>`_

`stackoverflow <https://stackoverflow.com/questions/64298298/type-hinting-callable-with-no-parameters>`_

.. code-block:: python

   def function(callback_function: Callable[[], None]) -> None:
