====
Grep
====

.. code-block:: console

   git grep path/ word

Indexes
"""""""

display line numbers

.. code-block:: console

   -n

file types

.. code-block:: console

   -- '\*.html'

some words

.. code-block:: console

   -- 'some words'

no index

.. code-block:: console

   -i

specific directory

.. code-block:: console

   -- directory/

Exclude path/

.. code-block:: console

   git grep -n Points -- ':!docs/'

.. code-block:: console

   git grep -n Points -- ':(exclude)docs/'
