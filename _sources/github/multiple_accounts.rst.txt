==========================
Managing multiple accounts
==========================

`Managing multiple accounts <https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-your-personal-account/managing-multiple-accounts>`_

.. code-block:: console
   :caption: Генерация SSH keys для для двух аккаунтов

   ssh-keygen -t rsa -C "454004@mail.ru" -f "454004"
   ssh-keygen -t rsa -C "mikurov_sergey@mail.ru" -f "mikurov_sergey"

.. code-block:: python
   :caption: Start ssh-agent

   eval "$(ssh-agent -s)"

.. code-block:: console
   :caption: Добавление SSH keys в SSH Agent

   # if:
   # ssh-add -K ~/.ssh/454004
   # ssh-add -K ~/.ssh/mikurov_sergey
   # then: Enter PIN for authenticator:

   ssh-add ~/.ssh/454004
   ssh-add ~/.ssh/mikurov_sergey

.. code-block:: console
   :caption: Копирование публичного ключа

   cat ~/.ssh/454004.pub
   cat ~/.ssh/mikurov_sergey.pub

Paste the public key on Github

.. code-block:: console
   :caption: Create a Config File and Make Host Entries

   nano config

.. code-block:: console
   :caption: Create a Config File and Make Host Entries

   #454004 account
   Host github.com-454004
        HostName github.com
        User git
        IdentityFile ~/.ssh/454004

   #mikurov_sergwy account
   Host github.com-mikurov_sergey
        HostName github.com
        User git
        IdentityFile ~/.ssh/mikurov_sergey

For cloning the repo use the below command
""""""""""""""""""""""""""""""""""""""""""

.. code-block:: console
   :caption: Clone repo

   git clone git@github.com-454004:svmikurov/repo-name.git
   git clone git@github.com-mikurov_sergey:my-glossary/repo-name.git

To push or pull to the correct account
""""""""""""""""""""""""""""""""""""""

We need to add the remote origin to the project

.. code-block:: console
   :caption: Для нового repo на аккаунте 454004

   git commit -m "first commit"
   git branch -M main
   git remote add origin git@github.com-454004:svmikurov/{new-project-name}.git
   git push -u origin main

.. code-block:: console
   :caption: Для repo на аккаунте 454004

   git config user.email "454004@mail.ru"
   git config user.name "Sergei Mikurov"
   git remote set-url origin git@github.com-454004:svmikurov/{project-name}.git
   git push

.. code-block:: console
   :caption: Для repo на аккаунте mikurov_sergey

   git config user.email "mikurov_sergey@mail.ru"
   git config user.name "Sergei Mikurov"

   git remote add origin git@github.com-mikurov_sergey:mikurov_sergey

.. code-block:: console
   :caption: Push glossary to mikurov_sergey

   git config user.email "mikurov_sergey@mail.ru"
   git config user.name "Sergei Mikurov"
   git remote set-url origin git@github.com-mikurov_sergey:my-glossary/glossary.git
   git push -u origin main
