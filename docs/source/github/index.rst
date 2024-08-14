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

   git config --list --show-origin

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
