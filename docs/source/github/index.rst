######
GitHub
######

.. toctree::
   :maxdepth: 2

   multiple_accounts


====
Base
====

.. code-block:: console
   :caption: перейти в каталог ``.ssh/``

   cd ~/.ssh/

Создаем SSH ключ для репозитория "svmikurov"
--------------------------------------------

.. code-block::
   :caption: создать новый SSH ключ для ``454004@mail.ru``

   $ ssh-keygen -t ed25519 -C "454004@mail.ru"
   Generating public/private ed25519 key pair.
   Enter file in which to save the key (/home/sv/.ssh/id_ed25519): svmikurov
   Enter passphrase (empty for no passphrase):
   Enter same passphrase again:

.. code-block:: console
   :caption: вывести в терминале SSH ключ для ``454004@mail.ru``

   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/svmikurov
   cat ~/.ssh/svmikurov.pub

Добавляем ключ в репозиторий ``https://github.com/settings/keys``.

Создаем SSH ключ для репозитория "my-glossary"
----------------------------------------------

.. code-block::
   :caption: создать новый SSH ключ для ``mikurov_sergey@mail.ru``

   $ ssh-keygen -t ed25519 -C "mikurov_sergey@mail.ru"
   Enter file in which to save the key (/home/sv/.ssh/id_ed25519): glossary
   Enter passphrase (empty for no passphrase):
   Enter same passphrase again:

.. code-block:: console
   :caption: вывести в терминале SSH ключ для ``mikurov_sergey@mail.ru``

   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/glossary
   cat ~/.ssh/glossary.pub

Добавляем ключ в репозиторий ``https://github.com/settings/keys``.

Настраиваем git
---------------

.. code-block:: console
   :caption: Создаем файл ``config``

   nano config

В файле ``config`` прописываем::

   Host 454004
     HostName github.com
     User user1
     IdentityFile /home/sv/.ssh/454004

   Host glossary
     HostName github.com
     User user2
     IdentityFile /home/sv/.ssh/glossary

========================
Перезаписать репозиторий
========================

.. code-block:: console
   :caption: скопировать проект в новый репозиторий

   git remote set-url origin git@github.com:svmikurov/glossary.git
   git push -u origin main --force

=====
Pages
=====

   repository / Settings /Pages

Бесплатно только в публичном репозитории
