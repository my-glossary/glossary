********
Branches
********

==========
Add branch
==========

Create branch::

    git branch <new-branch>

Create and switch to branch::

    git checkout -b <new-branch>

Push new branch::

    git push --set-upstream origin <new-branch>

=============
Delete branch
=============

удалить ветку, если ветка слита полностью::

    git branch -d <branch-name>

удалить ветку, в любом случае::

    git branch -D <branch-name>

удалить ветку в репозитории::

    git push origin --delete <branch-name>
