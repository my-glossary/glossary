********
Makefile
********

=================
Environment value
=================

Get from .env
_____________

Source: `Including Other Makefiles <https://www.gnu.org/software/make/manual/html_node/Include.html>`_

.env::

    ENVIRONMENT=PRODUCTION

Makefile::

    include .env

    echo:
        echo ${ENVIRONMENT}

console::

    make echo

stdout::

    echo PRODUCTION
    PRODUCTION


======================
Syntax of Conditionals
======================

Source: `Syntax of Conditionals <https://www.gnu.org/software/make/manual/html_node/Conditional-Syntax.html>`_

Makefile::

    include .env

    ifeq (${ENVIRONMENT}, DEVELOPMENT)
        DISPLAY := DEV
    else ifeq (${ENVIRONMENT}, PRODUCTION)
        DISPLAY := PROD
    endif

    display:
        echo ${DISPLAY}

stdout ::

    echo PROD
    PROD
