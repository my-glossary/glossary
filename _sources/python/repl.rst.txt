====
REPL
====

* `Python - Command line and environment <https://docs.python.org/3/using/cmdline.html#command-line-and-environment>`_
* `The Python Standard REPL: Try Out Code and Ideas Quickly <https://realpython.com/python-repl/>`_
* `Python Command-Line Arguments <https://realpython.com/python-command-line-arguments/>`_

Passing Command-Line Options to the python Command
--------------------------------------------------

``-i`` ``globals()``

.. code-block:: python
   :caption: sample.py

   def read_data():
       # Read data from a file or database...
       return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

   sample = read_data()

   def mean(data):
       return sum(data) / len(data)

   average = mean(sample)

.. code-block:: console

   $ python -i sample.py
   >>> average
   5.5
   >>> mean([2, 3, 3, 2])
   2.5

``-c``

.. code-block:: console

   python -c "print('Hello, World')"
   Hello, World

``-b``

.. code-block:: console

   python -b
   >>>

Customizing the Standard REPL
-----------------------------

`Customizing the Standard REPL <https://realpython.com/python-repl/#customizing-the-standard-repl>`_

`PYTHONSTARTUP <https://docs.python.org/3/using/cmdline.html#envvar-PYTHONSTARTUP>`_
