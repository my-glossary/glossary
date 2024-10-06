=====
Class
=====

Классы позволяют реализовать абстракцию.

============
Наследование
============

`Tutorial / 9. Classes / 9.5 Inheritance <https://docs.python.org/3/tutorial/classes.html#inheritance>`_

   * object — самый базовый класс в Python
   * superclass
   * subclass
   * override

* позволяет выделить общее для нескольких классов поведение
  и вынести его в отдельный класс.

.. code-block:: python
   :caption: Доступ к классам предкам через super()

   class A:
       x = 'a'

   class B(A):
       x = 'b'

   class C(B):
       x = 'c'

   class D(C):
       x = 'c'
       def super_x_of_a(self): return super(B, self).x
       def super_x_of_b(self): return super(C, self).x
       def super_x_of_c(self): return super().x   # the same as: return super(D, self).x

Возврат объектов
================

.. code-block:: python
   :caption: Внутри объектов можно также создавать новые объекты и вовзращать их.

   class Clone:
    def __init__(self, name):
        self.name = name
    def make_new_clone(self, name):
        return Clone(name)

   sheep_1 = Clone('Dolly')
   sheep_2 = sheep_1.make_new_clone('Sally')

   sheep_1.name # 'Dolly'
   sheep_2.name # 'Sally'


__init__
========

Отвечает за инициализацию экземпляров класса после их создания.
Позволяет получить уже полностью настроенный экземпляр.

Protocols
=========

* `PEP 544 <https://peps.python.org/pep-0544/>`_
* `Python Protocols: Leveraging Structural Subtyping <https://realpython.com/python-protocol/#the-meaning-of-protocol-in-python>`_

Python сам вызывает метод __init__ в нужный момент.
Это же касается большинства dunder-методов:
таковые вы только объявляете, но вручную не вызываете.
Такое поведение часто называют **протоколом** (или поведением):
класс реализует некий протокол, предоставляя нужные dunder-методы.
А Python, в свою очередь, работает с объектом посредством протокола.

.. code-block:: python
   :caption: Протокол получения длины имени объекта

    class Person:
    def __init__(self, name):
        self.name = name
    def __len__(self):
        return len(self.name)

    tom = Person('Thomas')
    len(tom)  # 6

Протоколы в Python являются представлением идеи Duck typing в коде.
