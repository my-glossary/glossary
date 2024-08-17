======
System
======


Disk memory info
----------------

`<https://itsfoss.com/free-up-space-ubuntu-linux/>`_

.. code-block:: console
   :caption: Вывести сведения, ``-h`` - in human-readable format

   df -h

Clean up APT cache in Ubuntu
""""""""""""""""""""""""""""

.. code-block:: console
   :caption: Информация о размере АРТ кэше

   sudo du -sh /var/cache/apt

.. code-block:: console
   :caption: Очистить АРТ кэш

   sudo apt-get autoclean

Clear systemd journal logs
""""""""""""""""""""""""""

.. code-block:: console
   :caption: info

   journalctl --disk-usage

.. code-block:: console
   :caption: clean

   sudo journalctl --vacuum-time=3d

Memory info
-----------

.. code-block:: console

   free -g -h -t

stdout:

::

                   total        used        free      shared  buff/cache   available
    Mem:           985Mi       292Mi        73Mi        16Mi       619Mi       506Mi
    Swap:             0B          0B          0B
    Total:         985Mi       292Mi        73Mi
