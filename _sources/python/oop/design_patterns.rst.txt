===============
Design Patterns
===============

* `Hexlet / Паттерны без привязки к языку <https://github.com/Hexlet/patterns/tree/main/content>`_
* `Коллекция антипаттеров (wiki) <https://ru.wikipedia.org/wiki/%D0%90%D0%BD%D1%82%D0%B8%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD>`_

    Шаблоны проектирования или паттерны в разработке программного обеспечения
    решают проблемы проектирования в рамках некоторого часто возникающего контекста.

    Это повторяющаяся архитектурная конструкция, которая стала
    неотъемлемой частью современной разработки.

    Паттерн — это типовое решение для типовой задачи.

Паттерн "Перенос данных из конструктора в метод"
================================================

   Если создание объекта и вызов метода можно заменить на обычную
   функцию, то ни о какой абстракции речи не идет. Правильный подход в
   этом случае сводится к переносу данных из конструктора в сам метод.

.. code-block:: python
   :caption: Код для примера

   class MarkdownToHTML:
       def __init__(self, markdown_text):
           self.markdown_text = markdown_text

       def render(self):
           return markdown(self.markdown_text)

   md1 = MarkdownToHTML(markdown1)
   html1 = md1.render()

   md2 = MarkdownToHTML(markdown2)
   html2 = md2.render()

.. code-block:: python
   :caption: Перенос данных из конструктора в метод

   md = MarkdownToHTML()
   # Важно, чтобы render оставался чистой функцией и не сохранял markdown внутри объекта
   html1 = md.render(markdown1)
   html2 = md.render(markdown2)

Паттерн "Управления конфигурацией в приложениях"
================================================

   Основной идеей является инициализация объектов с опциями или настройками, которые затем можно использовать при вызове методов этих объектов. Это позволяет уменьшить дублирование кода и сделать приложение более гибким и настраиваемым.

.. code-block:: python
   :caption: Код для примера

   html1 = markdown_to_html(markdown1, sanitize=True)
   html2 = markdown_to_html(markdown2, sanitize=True)

.. code-block:: python
   :caption: Управления конфигурацией в приложениях

   options = {'sanitize': True}

   md = MarkdownToHTML(**options)
   html1 = md.render(markdown1)
   html2 = md.render(markdown2)

Паттерн "Изменяемая конфигурация"
=================================

   Если для конкретного запроса нужно временно установить опции,
   отличные от тех, что были переданы в конструктор.

.. code-block:: python

   request = Request(timeout=1)
   response = request.get("<http://example.com>")

   # Передаем дополнительный параметр при вызове метода
   response = request.get("<http://example.com>", timeout=10)
   response = request.get("<http://example.com>")

Паттерн "Объекты-сущности, Объекты-значения и внедренные объекты"
=================================================================

`Objects on Hexlet <https://ru.hexlet.io/courses/python-object-oriented-design/lessons/modeling/theory_unit>`_

Fluent Interface
================

`wiki <https://ru.wikipedia.org/wiki/Fluent_interface>`_
`Fluent Interface on Hexlet <https://ru.hexlet.io/courses/python-object-oriented-design/lessons/fluent-interface/theory_unit>`_

"Текучий интерфейс" хорош тем, что упрощается множественный вызов методов
одного объекта. Обычно это реализуется использованием цепочки методов,
передающих контекст вызова следующему звену (но текучий интерфейс влечет
за собой нечто большее, чем просто цепочку методов[1]). Обычно, этот
контекст:

* определён с помощью значения, возвращаемого методом;
* наследуется (в качестве нового контекста используется предыдущий);
* прекращается возвращением ничего не значащего значения (void).

self
----

Первый способ создания Fluent Interface основан на возврате self из
методов, которые участвуют в построении цепочек. self — ссылка на тот
объект, в контексте которого вызывается метод, поэтому его можно
возвращать как обычное значение:

.. code-block:: python
   :caption: способ создания Fluent Interface основан на возврате self из методов

   class Collection:
       def __init__(self, coll):
           self.coll = coll

       def map(self, fn):
           self.coll = list(map(fn, self.coll))
           return self

У этого способа есть один недостаток — объект изменяется. Это значит,
что нельзя взять и просто переиспользовать объект-коллекцию для разных
выборок, потому что они начнут накладываться друг на друга.

На практике часто используется другой подход, с которым мы уже
познакомились в прошлом курсе. Нужно добавить немного функциональности
в ООП — возвращать не self, а создавать новый объект того же типа с
обновленной коллекцией:

.. code-block:: python
   :caption: возвращать не self, а создавать новый объект того же типа с обновленной коллекцией

   class Collection:
       def __init__(self, coll):
           self.coll = coll

       def map(self, fn):
           return Collection(list(map(fn, self.coll)))

       def filter(self, fn):
           return Collection(list(filter(fn, self.coll)))

       # Возвращает саму коллекцию, а не self.
       # Этот метод всегда последний в цепочке вызовов Collection.
       def all(self):
           return self.coll

   cars = Collection([
       {'model': 'rapid', 'year': 2016},
       {'model': 'rio', 'year': 2013},
       {'model': 'mondeo', 'year': 2011},
       {'model': 'octavia', 'year': 2014}
   ])

   filtered_сars = cars.filter(lambda car: car['year'] > 2013)
   mapped_сars = filtered_сars.map(lambda car: car['model'])
   print(mapped_сars.all()) # ['rapid', 'octavia']
   print(cars.all())
   # [
   #   {'model': 'rapid', 'year': 2016},
   #   {'model': 'rio', 'year': 2013},
   #   {'model': 'mondeo', 'year': 2011},
   #   {'model': 'octavia', 'year': 2014}
   # ]

self.class
----------

Этот метод позволяет создавать новые объекты и сохранять исходные данные без изменений.

.. code-block:: python
   :caption: Не изменяемый вариант

   class Collection:
       # ...

       def map(self, fn):
           return self.__class__(list(map(fn, self.coll)))

       # ...

Этот прием обеспечивает большую гибкость при наследовании классов,
так как self.__class__ всегда ссылается на класс текущего экземпляра,
а не на конкретно указанный класс.

Сборщики (Builders)
===================

`Builders on Hexlet <https://ru.hexlet.io/courses/python-object-oriented-design/lessons/builder/theory_unit>`_

Builder
-------

   Предлагает разделить процесс построения сложного объекта
   на различные части, каждая из которых отвечает
   за определенный аспект построения объекта

Обычно реализуется с помощью fluent interface.
Каждый метод возвращает ссылку на сам объект ``return self``,
что позволяет вызывать методы последовательно в одной цепочке.

.. code-block:: python

   class DataValidator:
       def __init__(self, data):
           self.data = data
           self.errors = []

       def validate_email(self):
           if ... : self.errors.append('Invalid email')
           return self

       def validate_password(self):
           if ... : self.errors.append('Password is too short')
           return self

       def get_errors(self):
           return self.errors

   data = {"email": "test", "password": "short"}
   validator = DataValidator(data)
   errors = validator.validate_email().validate_password().get_errors()

   if errors:
       print(errors)

Pydantic
--------

   Библиотека Pydantic предоставляет набор инструментов
   для валидации данных с использованием python-типов:

Pydantic позволяет с помощью объявления типов поля в модели
определять правила валидации.

.. code-block:: python

   class User(BaseModel):
       name: str
       email: EmailStr
       age: PositiveInt

   try:
       User(name='Tom', email='tom@example.com', age=-1)
   except ValidationError as e:
       print(e)

Query Builder
-------------

   Позволяет собирать сложные запросы по частям

В Python одним из наиболее известных примеров использования этого
паттерна является Django ORM. Это фреймворк, который позволяет строить
запросы к базе данных с помощью fluent interface.

.. code-block:: python

   # Запрос выборки для модели User с условиями и сортировкой
   users = (
       User.objects.filter(name='Tom')
       .exclude(is_active=False)
       .order_by('-last_login')
   )

Money pattern
=============

Это объект-значение, который используется для представления денег в программе.

.. code-block:: python

   class Money:
    def __init__(self, amount, currency='usd'):
        self.amount = amount
        self.currency = currency

Null Object Pattern
===================

   Шаблон проектирования, который используется
   для обработки нулевых или отсутствующих значений.

.. code-block:: python
   :caption: определим класс ``User`` и ``Guest`` - Null Object класс

   class User:
       """Класс для аутентифицированного пользователя."""

       def __init__(self, name):
           self.name = name

       def get_name(self):
           return self.name

       def has_articles(self):
           return True

       def get_articles(self):
           # воображаемый код, делающий запрос к базе и получающий все статьи
           return db.get_articles(self)

   class Guest:
       """Класс для неаутентифицированного пользователя.

       Представляет собой «нулевой объект»,
       у которого тот же интерфейс, что и User,
       но возвращает значения по умолчанию.
       """

       def get_name(self):
           return "Guest"

       def has_articles(self):
           return False

       def get_articles(self):
           return []

.. code-block:: python
   :caption: определим функцию, которая возвращает
             либо аутентифицированного пользователя,
             либо Null Object

   def get_current_user(authenticated):
       if authenticated:
           return User("Alice")
       else:
           return Guest()

.. code-block:: python
   :caption: применим шаблон

   current_user = get_current_user(authenticated=True)
   print(current_user.get_name())  # => Alice
   print(current_user.get_articles())  # => ['article1', 'article2', 'article3']

   current_user = get_current_user(authenticated=False)
   print(current_user.get_name())  # => Guest
   print(current_user.get_articles())  # => []

Несмотря на удобство и простоту использования паттерна Null Object,
его стоит применять осторожно. Большое количество нулевых объектов
может затруднить отладку и понимание кода,
поскольку они скрывают отсутствие значения. Важно найти баланс между удобством использования и ясностью кода.