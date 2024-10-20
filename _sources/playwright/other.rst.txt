=====
Other
=====

To get text form page element
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Waiting for the test to become visible

`wait_for <https://playwright.dev/python/docs/api/class-locator#locator-wait-for>`_

.. code-block:: python

   locator.wait_for(state='visible')

`inner_text <https://playwright.dev/python/docs/api/class-elementhandle#element-handle-inner-text>`_

.. code-block:: python

   element_handle.inner_text()

`text_content <https://playwright.dev/python/docs/api/class-locator#locator-text-content>`_

.. code-block:: python

   locator.text_content()
   locator.text_content(**kwargs)
