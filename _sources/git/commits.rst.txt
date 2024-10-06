=======
Commits
=======

Схлопнуть коммиты
-----------------

.. code-block:: console
   :caption: Сделать резервную копию (новичкам)

   git branch backup

.. code-block:: console
   :caption: Выбрать три последних коммита

   git rebase -i HEAD~3

Откроется диалоговое окно::

    pick bcdca61 Commit 1
    pick 4643a5f Commit 2
    pick e0ca8b9 Commit 3 (last)

Чтобы объединить их все в один
нужно заменить pick на squash
для двух самых свежих коммитов (две нижние строки)::

    pick bcdca61 Commit 1
    squash 4643a5f Commit 2
    squash e0ca8b9 Commit 3 (last)

После сохранить и закрыть диалоговое окно.

В следующем "диалоге" вам предложат указать заголовок для получившегося коммита.