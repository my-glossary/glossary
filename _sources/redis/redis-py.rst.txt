################
redis-py library
################

==============
Start redis-py
==============

`redis-py <https://redis-py.readthedocs.io/en/stable/index.html#>`_

Install redis-py
----------------

    python -m pip install redis[hiredis]==5.0.8

Connect to redis
----------------

    host = 'redis' or 'localhost'

.. code-block:: python

   >>> import redis
   >>> r = redis.Redis(host='redis', port=6379)
   >>> r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
   True
   >>> r.get("Bahamas")
   b'Nassau'
   >>> r.get("Bahamas").decode("utf-8")
   'Nassau'

Allowed Key Types
-----------------

    bytes, str, int, or float


Convert the Python date object to ``str``,
which you can do with ``.isoformat()`` or use str(today)

========
Commands
========

.. code-block:: python
   :caption: key[value] = number

   redis_server.hset(key, value, number)
