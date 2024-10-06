==========
Exceptions
==========

    * raising
    * traceback

`Tutorial / 8. Errors and Exceptions <https://docs.python.org/3/tutorial/errors.html#errors-and-exceptions>`_
`Built-in Exceptions hierarchy <https://docs.python.org/3/library/exceptions.html#exception-hierarchy>`_


Иерархия исключений
===================

Чтобы можно было "ловить" исключения как по одному (ловить IndexError), так и перехватывать целые группы (OSError).

    * BaseException - корень дерева исключений
    * Exception - ствол дерева исключений
    * дальше происходит ветвление на виды исключений
    * а затем — на конкретные исключения

.. code-block:: python
   :caption: возбуждение исключения

   raise ValueError('Age too low!')

.. code-block:: python
   :caption: перехват исключений

   try:
       ...
   except Exception:
       ...
   except (KeyError, IndexError):
       ...

finally
-------

В этом коде файл будет закрыт (f.close()) в любом случае,
вне зависимости от того, произошла ошибка или нет.
Если ошибка все же произошла, то сразу
после блока finally выполнение кода будет прервано
и исключение "всплывет" выше, но хотя бы
по поводу незакрытого файла можно будет не волноваться!

.. code-block:: python

   f = open('data.txt')
   try:
       text = f.read()
       words = len(text.split())
   finally:
       f.close()

Получение экземпляра исключения и возбуждение уже пойманного
------------------------------------------------------------

.. code-block:: python
   :caption: в ветке except указать имя переменной, которая получит ссылку на экземпляр исключения

   try:
       ...
   except (SQLSelectError, SQLInsertError) as e:
       print(f"Query execution error: '{e.query}'")
   except DBConnectionError as e:
       print(f"Can't connect to DB: '{e.status}'")
   ...

Антипаттерны при перехвате исключений
-------------------------------------

* Неправильный порядок обработчиков
* except Exception
* огромные try-блоки

   Единственный случай, в котором допустимо перехватывать Exception,
   это случай, когда в конце обработчика исключение возбуждается заново.
   Таким способом вы можете, например, протоколировать
   (логировать, записывать в log-файл) все ошибки,
   но никак их не обрабатывать, чтобы у вызывающей стороны
   была возможность отреагировать на ошибку.

.. literalinclude:: ../../../examples_python/except01.py
