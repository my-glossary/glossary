##########
Redis Base
##########

`Hexlet / Основы Redis <https://ru.hexlet.io/courses/redis-basics>`_

`RealPython / How to Use Redis With Python <https://realpython.com/python-redis/>`_

=====================
Особенности хранилища
=====================

* **in-memory** - данные хранятся в оперативной памяти
* **KV хранилище (key-value)** - данные записываются и получаются по ключам

==============
Redis commands
==============

=============================================== ==================================================
Cli                                             Overview
=============================================== ==================================================
**Запись . Получение данных**
set ``key`` ``value``                           Записать значение по ключу
get ``key`` ``value``                           Получить значение по ключу
mset ``key1`` ``value1`` ``key2`` ``value2``    Записать несколько значений по ключам
mget ``key1`` ``value1`` ``key2`` ``value2``    Получить несколько значений по ключам
exists ``key``                                  Проверить на существование без получения данных

**Таймер хранения данных**
set ``key`` ``value`` ex ``seconds``            Записать значение по ключу
set ``key`` ``value`` px ``milliseconds``       Записать значение по ключу
ttl ``key``                                     Проверить, через сколько секунд ключ удалится
pttl ``key``                                    Проверить, через сколько милисек ключ удалится
expire ``key`` ``value`` ex ``seconds``         Для установки времени жизни для уже существующего ключа
del ``key``                                     Удалить ключ
unlink ``key1`` ``key2``                        Удалить несколько ключей (через пробел)

**Инкремент / Декремент**
incr ``key``                                    Увеличение значения на 1
incrby ``key`` ``value``                        Увеличение значения на ``value``
decr ``key``                                    Уменьшение значения на 1
decrby ``key`` ``value``                        Уменьшение значения на ``value``

**Списки**
lpush ``key`` ``value1`` [``value2``...]        Для добавления элемента в начало списка (слева)
lrange ``key`` ``start_index`` ``stop_index``   Получение элементов
lpop ``key``                                    Удаление первого элементов списка
rpop ``key``                                    Удаление последнего элементов списка
lrem ``key`` ``0`` ``value``                    Ищет в списке значение и удаляет его

FLUSHDB                                         Очистить базу данных
QUIT                                            Выйти
=============================================== ==================================================

=============
Install Redis
=============

.. code-block::
   :caption: Project structure:

    ├── docker
    |   ├── redis
    |       └── Dockerfile
    |
    ├── docker-compose.yml

.. code-block:: docker
   :caption: Dockerfile:

   FROM redis:7.4.0-bookworm

.. code-block:: docker
   :caption: docker-compose.yml:

   redis:
     container_name: redis
     image: redis
     build:
       context: .
       dockerfile: ./docker/redis/Dockerfile
     hostname: redis
     ports:
       - "6379:6379"

.. code-block:: python
   :caption: python -m pip install redis

   >>> import redis
   >>> r = redis.Redis(host='redis', port=6379)
   >>> r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
   True
   >>> r.get("Bahamas")
   b'Nassau'



=========
Run Redis
=========

.. code-block:: console
   :caption: После установки Redis сервер нужно запускать вручную:

   redis-server

.. code-block:: console
   :caption: Обычно Redis сервер запускается как демон (daemon):

   redis-server --daemonize yes

.. code-block:: console
   :caption: Подключиться к Redis с помощью утилиты redis-cli:

   redis-cli

   127.0.0.1:6379>

.. code-block:: console
   :caption: Начать новую базу данных под номер 5 (0, по умолчанию):

   redis-cli -n 5

.. code-block:: console
   :caption: test connect to the server

   127.0.0.1:6379> PING
   PONG

=============================
Redis как key-value хранилище
=============================

Запись новой сессии
===================

.. code-block:: console
   :caption: Команда записи в Redis:

   # set ключ значение

   127.0.0.1:6379> set session:1 120
   OK

..

    в ключах рекомендуется использовать двоеточие как разделитель слов
    (хотя и встречаются другие подходы к наименованию).
    В примере с сессией ключ имеет вид session:{session_id}.

..

    команда set записывает значение как строку.
    Одиночное слово пишется без кавычек, но предложение придется
    писать в одинарных или двойных кавычках set key1 'hello world'.

Получение существующей сессии
=============================

.. code-block:: console
   :caption: Получение существующей сессии:

   127.0.0.1:6379> get session:1
   "120"

.. code-block:: console
   :caption: Запрос по несуществующему ключу:

   127.0.0.1:6379> get session:N
   (nil)

.. code-block:: console
   :caption: Проверить на существование без получения данных

   127.0.0.1:6379> exists session:1
   (integer) 1
   127.0.0.1:6379> exists session:N
   (integer) 0

   # Если ключ существует, Redis возвращает целое число 1.
   # В противном случае вернется 0.

Удаление сессии
===============

.. code-block::
   :caption: Удаление сессии

   127.0.0.1:6379> del session:1
   (integer) 1
   127.0.0.1:6379> del session:N
   (integer) 0

Ответ Redis идентичен команде exists:

    1, если ключ существовал, и он был успешно удален
    0, если ключа не было, поэтому ничего не было удалено

Счетчик
=======

Со счетчиком можно работать так же, как и с обычным ключом:
получать значение, устанавливать время жизни, удалять:

RedisJSON
=========

`RedisJSON <https://github.com/RedisJSON/RedisJSON#redisjson>`_

======================
Списки в Redis (Lists)
======================

   Списки в Redis — это список строк, упорядоченный в порядке вставки.

Запись элементов
================

   lpush key value1 [value2...]

.. code-block:: python
   :caption: Для добавления элемента в начало списка (слева):

   127.0.0.1:6379> lpush user:14:recent_posts 10
   (integer) 1
   127.0.0.1:6379> lpush user:14:recent_posts 20 30
   (integer) 3

Если списка не существовало до этого, то Redis создаст новый.

Команда lpush возвращает количество элементов в списке после вставки.

Получение элементов
===================

   lrange ``key`` ``start_index`` ``stop_index``

   Если ``stop_index = -1``, то вернется весь список.

.. code-block:: python
   :caption: Получение элементов:

   127.0.0.1:6379> lrange user:14:recent_posts 0 -1
   1) "30"
   2) "20"
   3) "10"

Удаление элементов
==================

   ``lpop`` удаляет элемент из начала списка и возвращает его


   ``rpop`` удаляет элемент из конца списка и возвращает его

.. code-block:: console

   127.`0.0.1:6379> lpop user:14:recent_posts
   "30"
   127.0.0.1:6379> rpop user:14:recent_posts
   "10"`

   Если количество элементов в списке маленькое,
   то можно использовать команду ``lrem key 0 value``,
   которая ищет в списке значение и удаляет его.
   Команда ``lrange`` возвращает указанные элементы списка.

.. code-block:: console

   127.0.0.1:6379> lrem user:14:recent_posts 0 120
   (integer) 0
   127.0.0.1:6379> lrem user:14:recent_posts 0 20
   (integer) 1
   127.0.0.1:6379> lrange user:14:recent_posts 0 -1
   (empty array)

   Если элемент не был найден в списке, то возвращается ``0``.
   В случае успешного удаления вернется ``1``.
   Так как удалился последний элемент в списке,
   команда ``lrange`` вернула пустой массив.

Время жизни
===========

.. code-block:: console
   :caption: время жизни в 1 час
             на список с последними постами пользователя 14:

   127.0.0.1:6379> expire user:14:recent_posts 3600
   (integer) 1
   127.0.0.1:6379> ttl user:14:recent_posts
   (integer) 3598

============
Redis Hashes
============

Запись
======

   hset ``key`` ``field value`` [``field value`` ...]

   Возвращает количество добавленных полей.

   Если ключа не существовало, то он будет создан.

.. code-block:: console

   127.0.0.1:6379> HSET realpython url "https://realpython.com/"
   (integer) 1
   127.0.0.1:6379> HSET realpython github realpython
   (integer) 1
   127.0.0.1:6379> HSET realpython fullname "Real Python"
   (integer) 1

.. code-block:: python

   data = {
       "realpython": {
           "url": "https://realpython.com/",
           "github": "realpython",
           "fullname": "Real Python",
       }
   }


==============================================
Проверка на уникальность с Sets — Основы Redis
==============================================

Обычные ключи
=============

.. code-block:: console
   :caption: хранить каждое посещение
             отдельным ключом с форматом page:{page_path}:user:{user_id}:

   127.0.0.1:6379> set page:/courses:user:22 1
   OK
   127.0.0.1:6379> set page:/courses:user:33 1
   OK
   127.0.0.1:6379> exists page:/courses:user:22
   (integer) 1
   127.0.0.1:6379> keys page:/courses:user:*
   1) "page:/courses:user:33"
   2) "page:/courses:user:22"

Проверка с Redis Lists
======================

.. code-block:: console

   127.0.0.1:6379> lpush page:/courses 22 33 44
   (integer) 3
   127.0.0.1:6379> llen page:/courses
   (integer) 3

Проверка с Redis Hashes
=======================

.. code-block:: console

   127.0.0.1:6379> hset page:/courses 11 1 22 1 33 1
   (integer) 3
   127.0.0.1:6379> hlen page:/courses
   (integer) 3

Проверка с Redis Sets
=====================

   Sets — это список уникальных элементов, поддерживающий
   быстрые функции вставки, проверки на уникальность и пересечений.

Запись Redis Sets
-----------------

   sadd key member [member ...]

.. code-block:: console

   127.0.0.1:6379> sadd page:/courses 11 22 33 44
   (integer) 4

Чтение и проверка на уникальность Redis Sets
--------------------------------------------

   scard key

.. code-block:: console
   :caption: Получить количество уникальных пользователей:

   127.0.0.1:6379> scard page:/courses
   (integer) 4

..

   sismember key member

.. code-block:: console

   127.0.0.1:6379> sismember page:/courses 33
   (integer) 1
   127.0.0.1:6379> sismember page:/courses 12222
   (integer) 0

Удаление Redis Sets
-------------------

   srem key member [member ...]

.. code-block:: console
   :caption: Удалить пользователя из набора:

   127.0.0.1:6379> srem page:/courses 44
   (integer) 1
   127.0.0.1:6379> smembers page:/courses
   1) "11"
   2) "22"
   3) "33"

Пересечения Redis Sets
----------------------

   sinter key [key ...]

.. code-block:: console
   :caption: получить уникальных пользователей, которые посетили все 3 страницы

   127.0.0.1:6379> sadd page:/courses 1 2 3 4 5 6 7 8 9 10
   (integer) 10
   127.0.0.1:6379> sadd page:/courses/java 1 2 3 4 5 6 7
   (integer) 7
   127.0.0.1:6379> sadd page:/courses/php 5 6 7 8 9
   (integer) 5
   127.0.0.1:6379> sinter page:/courses page:/courses/java page:/courses/php
   1) "5"
   2) "6"
   3) "7"
