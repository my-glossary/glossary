===========
Полиморфизм
===========

   - способность объектов разных типов обрабатываться как объекты одного типа.

   - способность функции обрабатывать данные разных типов.

Обеспечивает универсальность и повторное использование кода,
что упрощает разработку и поддержку программного обеспечения.
**Также он позволяет объектам и функциям работать с данными разных типов.**

   Параметрический полиморфизм — это вид полиморфизма,
   который позволяет функциям работать независимо от
   используемых ими типов данных.

Полиморфизм позволяет объекту использовать методы производного класса,
который не был определен на момент создания базового класса.

Полиморфизм позволяет нам использовать единую точку входа,
которая может выполнять различные действия
в зависимости от входных данных или состояния системы

=============================
Диспетчеризация (Полиморфизм)
=============================

Диспетчеризация по ключу (данные)
=================================

`Hexlet / Диспетчеризация по ключу (данные) <https://ru.hexlet.io/courses/python-polymorphism/lessons/key-dispatch-data/theory_unit>`_

   Диспетчеризация — это процесс выбора функции, метода или данных
   для выполнения на основе типа или значений переменных.

.. code-block:: python
   :caption: Диспетчеризация на использовании словарей

   def get_config(env):
       configurations = {
           'development': {
               'debug': True,
               'database': 'sqlite:///:memory:',
           },
           'production': {
               'debug': False,
               'database': 'postgresql://user:pass@localhost/db',
           },
       }

       return configurations.get(env, configurations['development'])

Обновление данных словаря ``configurations`` требует перезапуск программы,
чтобы обновленные данные применились.

Диспетчеризация с использованием файлов конфигурации
----------------------------------------------------

   Позволяет легко изменять поведение программы
   без необходимости ее перекомпиляции.

Когда параметры программы нужно менять без вмешательства в код.
В этом случае параметры программы обычно хранят во внешних файлах,
таких как JSON или YAML.

.. code-block:: python
   :caption: ``config.json`` содержит различные параметры
             для программы в зависимости от окружения

   {
     "development": {
       "debug": True,
       "database": "sqlite:///:memory:",
     },
     "production": {
       "debug": False,
       "database": "postgresql://user:pass@localhost/db",
     },
   }

.. code-block:: python
   :caption: загружаем ``config.json``,
             а затем выбираем нужную конфигурацию по ключу

   import json

   # Открываем файл на чтение
   with open('config.json', 'r') as file:
       # Загружаем JSON из файла
       config = json.load(file)

   def get_config(env: str) -> dict[str, object]:
       """Get config data.

       Parameters
       ----------
       env : `str`
           Environment name.

       Return
       ------
       Configuration dictionary for specific environment
       (`dict[str, object]`).

       """
       return config.get(env, config['development'])

   print(get_config('development'))  # => {'debug': True, 'database': 'sqlite:///:memory:'}
   print(get_config('production'))  # => {'debug': False, 'database': 'postgresql://user:pass@localhost/db'}

Диспетчеризацию по ключу (функции)
==================================

`Hexlet / Диспетчеризацию по ключу (функции) <https://ru.hexlet.io/courses/python-polymorphism/lessons/key-dispatch-functions/theory_unit>`_

   Ключи соответствуют различным условиям или сценариям,
   а значения — это функции, которые будут выполняться
   для этих условий

.. code-block:: python

   def greet_in_english(name):
       return f"Hello, {name}!"

   def greet_in_french(name):
       return f"Bonjour, {name}!"

   def greet_in_spanish(name):
       return f"Hola, {name}!"

   def error_message(*args, **kwargs):
       return "Error: Invalid language"

   greetings = {
       "english": greet_in_english,
       "french": greet_in_french,
       "spanish": greet_in_spanish
   }

   def greet(language, name):
       func = greetings.get(language, error_message)
       return func(name)

   print(greet("english", "Alice"))    # => Hello, Alice!
   print(greet("french", "Bob"))       # => Bonjour, Bob!
   print(greet("spanish", "Charlie"))  # => Hola, Charlie!
   print(greet("german", "David"))     # => Error: Invalid language

Диспетчеризация по имени файла
==============================

`Hexlet / Диспетчеризация по имени файла <https://ru.hexlet.io/courses/python-polymorphism/lessons/key-dispatch-files/theory_unit>`_

   Позволяет выбирать действие на основе
   имени файла или его расширения

Структура файлов с конфигурациями для различных сред::

   configs/
     database.development.json
     database.production.json
     database.test.json

.. code-block:: python
   :caption: загружаем конфигурацию из файла

   import json

   ENV_NAME = os.getenv("ENV_NAME", "development")

   filename = f"database.{ENV_NAME}.json"
   with open(filename, "r") as fd:
       config = json.load(fd)

==============================
Утиная типизация (Полиморфизм)
==============================

«Если это выглядит как утка, плавает как утка и крякает как утка,
то это, вероятно, и есть утка».

   Важен не тип объекта, а его поведение или методы, которые он реализует.

.. code-block:: python

   class Article:
       def __init__(self):
           self.comments = []

       def add_comment(self, comment):
           self.comments.append(comment)

       def get_comments(self):
           return self.comments

   class Topic:
       def __init__(self):
           self.comments = []

       def add_comment(self, comment):
           self.comments.append(comment)

       def get_comments(self):
           return self.comments

   def has_comments(item: object) -> bool:
   """Check has item the comments.

   Parameter
   ---------
   item : `object`
      The ``Article`` or ``Topic`` class.

   Return
   ------
   ``True`` if item has the comments, ``False`` otherwise.

   Examples
   --------

   article = Article()
   topic = Topic()

   print(has_comments(article))  # => False

   article.add_comment("Great article!")
   print(has_comments(article))  # => True

   print(has_comments(topic))    # => False

   topic.add_comment("Interesting topic!")
   print(has_comments(topic))    # => True

   """
    return len(item.get_comments()) > 0

Параметрический полиморфизм
===========================

   Обрабатывает **значения** разных типов одинаковым образом.

Реализуется общий алгоритм для контейнера разных типов.

Полиморфизмом подтипов
======================

   Обрабатывает **объекты** разных типов одинаковым образом.

Использует одноименные методы разных объектов.
