******************
SQL query examples
******************

.. code-block:: sql
   :caption: Обнули бонусы пользователя

   INSERT INTO task_points (write_off, balance, created_at, user_id) VALUES (32700, 0, current_timestamp, 7);

.. code-block:: sql
   :caption: Извлеки бонусы по id пользователя

   select * from task_points where task_id=1 order by id desc;

.. code-block:: sql
   :caption: Счетчик количества посетителей страницы

   INSERT INTO visits (url, count, date) VALUES ('hexlet.io/courses', 1, '2022-01-01') ON DUPLICATE KEY UPDATE count = count + 1
