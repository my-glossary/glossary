=======
Install
=======

.. code-block:: console
   :caption: Установка приложений

   sudo apt update && \
   sudo apt-get update && \
   sudo apt install python3-pip -y && \
   sudo apt install python3.10-venv -y && \
   sudo apt install curl && \
   sudo apt install telegram-desktop -y && \
   sudo apt install tree && \
   sudo apt install vim -y && \
   sudo apt-get install tilix -y && \
   sudo apt-get install filezilla -y && \
   sudo snap install pycharm-community --classic && \
   sudo apt install postgresql -y

.. code-block::
   :caption: Установка Docker

   # Docker
   # Add Docker's official GPG key:
   sudo apt-get update
   sudo apt-get install ca-certificates curl
   sudo install -m 0755 -d /etc/apt/keyrings
   sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
   sudo chmod a+r /etc/apt/keyrings/docker.asc
   # Add the repository to Apt sources:
   echo \
     "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
     $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
     sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   sudo apt-get update
   sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

.. code-block::
   :caption: Установка Docker Desktop (из скаченного файла)

   # Download or install from Disk/Soft directory docker-desktop-4.30.0-amd64.deb
   # At the end of the installation process, apt displays an error due to installing a downloaded package. You can ignore this error message.
   sudo apt-get update
   sudo apt-get install ./docker-desktop-4.30.0-amd64.deb

.. code-block:: console
   :caption: Установка Poetry

   # poetry
   curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.5.1 python3 -
   # Note /sv/ - user name !!!
   export PATH="/home/sv/.local/bin:$PATH"
   # restart comp!
   # чтобы создавал ``.venv``
   poetry config virtualenvs.in-project true
   # uninstall
   curl -sSL https://install.python-poetry.org | python3 - --uninstall


=========
Uninstall
=========

.. code-block:: console
   :caption: Удаление PyCharm

   sudo snap remove pycharm-community
