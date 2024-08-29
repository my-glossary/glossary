********
Tutorial
********

`BeeWare Tutorial <https://docs.beeware.org/en/latest/#welcome-to-the-beeware-tutorial>`_

`Toga 0.4.6.dev306+gf564dba0e <https://toga.readthedocs.io/en/latest/reference/api/index.html>`_

`The Pack Style Engine <https://toga.readthedocs.io/en/latest/reference/style/pack.html#the-pack-style-engine>`_

`Success Stories <https://toga.readthedocs.io/en/stable/background/project/success.html>`_

`Eddington — инструмент для подбора данных, основанный на Toga и Briefcase.
<https://github.com/EddLabs/eddington-gui/blob/develop/src/eddington_gui/app.py>`_

.. code-block:: console
   :caption: Use developer mode

   briefcase dev

Creating your application scaffold
==================================

`<https://docs.beeware.org/en/latest/tutorial/tutorial-3.html#creating-your-application-scaffold>`_

briefcase create

Building your application
=========================

`<https://docs.beeware.org/en/latest/tutorial/tutorial-3.html#building-your-application>`_

На этом этапе выполняется любая двоичная компиляция, необходимая
для того, чтобы ваше приложение могло выполняться на целевой платформе.

.. code-block:: console

   briefcase build

Running your app
================

`<https://docs.beeware.org/en/latest/tutorial/tutorial-3.html#running-your-app>`_

.. code-block:: console

   briefcase run

Building your installer
=======================

.. code-block:: console
   :caption: Build installer and show path to it

   briefcase package

   ...
   [wselfedu] Packaged dist/wselfedu_0.0.1-1~ubuntu-jammy_amd64.deb

Updating application code
=========================

`<https://docs.beeware.org/en/latest/tutorial/tutorial-4.html#updating-application-code>`_

.. code-block:: console
   :caption: to update the code for your existing bundled application

   briefcase update

.. code-block:: console
   :caption: to re-compile the app

   briefcase build

.. code-block:: console
   :caption: to run the updated app

   briefcase run

.. code-block:: console
   :caption: to repackage the application for distribution

   briefcase package

Update and run in one step
==========================

`<https://docs.beeware.org/en/latest/tutorial/tutorial-4.html#update-and-run-in-one-step>`_

.. code-block:: console
   :caption: update, build and run the app with one command

   briefcase run -u

.. code-block:: console
   :caption: make a change to your application code and want to repackage immediately

   briefcase package -u

Tutorial 5 - Taking it mobile: Android
======================================

`<https://docs.beeware.org/en/latest/tutorial/tutorial-5/android.html#tutorial-5-taking-it-mobile-android>`_

Create an Android app and compile it
------------------------------------

.. code-block:: console
   :caption: downloads an Android app template and adds your Python code to it.

   briefcase create android

.. code-block:: console
   :caption: to compile this into an Android APK app file

   $ briefcase build android

   ...
   BUILD SUCCESSFUL in 1m 58s
   41 actionable tasks: 41 executed
   Building... done

   [wselfedu] Built build/wselfedu/android/gradle/app/build/outputs/apk/debug/app-debug.apk

Run the app on a physical device
--------------------------------

.. code-block:: console
   :caption:

   briefcase run android

Add requirements
================

`<https://docs.beeware.org/en/latest/tutorial/tutorial-7.html#running-the-updated-app>`_

.. code-block:: console
   :caption: Update the code in the packaged app

   briefcase update

.. code-block:: console
   :caption: Rebuild the app

   briefcase build

.. code-block:: console
   :caption: And finally, run the app

   briefcase run

Updating dependencies
=====================

`<https://docs.beeware.org/en/latest/tutorial/tutorial-7.html#updating-dependencies>`_

   requires = [
       "httpx",
   ]

.. code-block:: console
   :caption: to update requirements in the packaged app

   briefcase update -r
   briefcase build
   briefcase run

or

.. code-block:: console
   :caption: to update requirements in the packaged app

   briefcase run -u -r

Ubuntu uninstall app
====================

.. code-block:: console
   :caption: to uninstall wselfedu

   sudo apt-get remove wselfedu
