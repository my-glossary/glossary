========
Property
========

RealPython
----------
* `Getters and Setters: Manage Attributes in Python <https://realpython.com/python-getter-setter/>`_

Guidelines:
-----------

    * Use public attributes whenever appropriate, even if you expect the attribute to require functional behavior in the future.
    * Avoid defining setter and getter methods for your attributes. You can always turn them into properties if needed.
    * Use properties when you need to attach behavior to attributes and keep using them as regular attributes in your code.
    * Avoid side effects in properties because no one would expect operations like assignments to cause any side effects.

See also:
---------
* `Python Class Constructors: Control Your Object Instantiation <https://realpython.com/python-class-constructor/>`_

Links:
------
* `Using Python datetime to Work With Dates and Times <https://realpython.com/python-datetime/>`_

Typing:
-------
* `Python Type Checking (Guide) <https://realpython.com/python-type-checking/>`_
* `mypy: Declaring decorators <https://mypy.readthedocs.io/en/stable/generics.html#declaring-decorators>`_
