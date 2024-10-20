======
origin
======

.. code-block:: console
   :caption: При добавлении проекта в репозиторий,
             если несколько аккаунтов на машине,
             добавить "-454004" в "git@github.com-454004:svmikurov/"

   git remote add origin git@github.com-454004:svmikurov/drf-toga.git
   git push -u origin main

.. code-block:: console
   :caption: При добавлении аккаунта на машину,
             перезаписать origin

   git config user.email "454004@mail.ru"
   git config user.name "Sergei Mikurov"
   git remote set-url origin git@github.com-454004:svmikurov/project-name.git
   git push --force

.. code-block:: console
   :caption: Remove origin

   git remote rm origin
