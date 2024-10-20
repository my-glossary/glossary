********
Property
********

**Setter** — метод, принимает новое значение для атрибута и как-то его обрабатывает.

.. tip::

    Сеттеры часто используют для того, чтобы проверить корректность
    нового значения или произвести какие-то его преобразования перед
    фактическим сохранением в другие атрибуты.

**Getter** — метод, возвращающий динамически вычисляемое значение.

**Deleter** — метод предоставляет дополнительный уровень контроля над тем,
как атрибуты класса удаляются.
Контролировать процесс удаления атрибутов, например, очищать связанные ресурсы
или выполнять некоторую логику очистки.

.. tip::

   Использование делитера особенно полезно в случаях,
   когда необходимо управлять удалением важных или связанных данных,
   или выполнять освобождение ресурсов (как, например, закрытие файлов
   или сетевых соединений) в момент уничтожения объекта или его свойств.

.. code-block:: python

   class Person:
       def __init__(self, name, surname):
           self.name = name
           self.surname = surname

       @property
       def full_name(self):
           return self.name + ' ' + self.surname

       @full_name.setter
       def full_name(self, new):
           self.name, self.surname = new.split(' ')

       @full_name.deleter
       def full_name(self):
           print("Удаляем имя и фамилию!")
           self.name = None
           self.surname = None

===================
Decorator @property
===================

`Python documentation / library / Built-in Functions / class property <https://docs.python.org/3/library/functions.html#property>`_

.. code-block:: python

    property(fget=None, fset=None, fdel=None, doc=None)

В такой форме property удобно использовать, когда вы уже имеете
готовые функции, которые хотите просто "упаковать" в свойство:

.. code-block:: python

    def get_full_name(self):
        ...

    def set_full_name(self, new):
        ...

    class Person:
        ...
        full_name = property(
            fget=get_full_name,
            fset=set_full_name,
            doc='A full name of person'
        )
