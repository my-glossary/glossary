==========
find, grep
==========

.. code-block:: console
   :caption: Искать содержание текста в директории файлов

   grep -rl "string" /path

`<https://www.gnu.org/software/grep/>`_

::

   -i -- makes it case insensitlve;
   -r --  means do this recursively, right down the directory tree;
   -n -- prints the line number for matches;
   --include -- lets you add file names, extensions.

.. code-block:: console
   :caption: find dir by name

   find -type d -name '*english*'
