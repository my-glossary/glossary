##############
Redis Examples
##############

`Store Nested data structures and Python objects in Redis Cache
<https://medium.com/@vickypalaniappan12/store-nested-data-structures-and-python-objects-in-redis-cache-814f03436d89>`_

`django / django / core / cache / backends / redis.py
<https://github.com/django/django/blob/b6ad8b687adf011245270df17a38c1a42792e3d7/django/core/cache/backends/redis.py#L12>`_

`vickypalani/redis_cache.py
<https://gist.github.com/vickypalani/225907e94065d040f4d186b829405694>`_

.. code-block:: python
   :caption: vickypalani/redis_cache.py:

    """Redis cache operations example."""
    import asyncio
    import pickle
    from uuid import uuid4

    import redis.asyncio as redis


    class RedisClient:
        """A client for interacting with Redis cache."""

        def __init__(self, host, port):
            """
            Initialize the Redis client.
            Args:
                host (str): The hostname of the Redis server.
                port (int): The port number of the Redis server.
            """
            self.host = host
            self.port = port
            self.redis = redis.Redis(host=self.host, port=self.port)

        async def close(self):
            """Close the Redis connection."""
            await self.redis.aclose()

        async def set(self, key, value):
            """
            Set a key-value pair in Redis.
            Args:
                key (str): The key to set.
                value (Any): The value to set. If it's an integer, it's stored as-is.
                              Otherwise, it's pickled before storage.
            """
            if isinstance(value, int):
                await self.redis.set(key, value)
            else:
                await self.redis.set(key, pickle.dumps(value))

        async def get(self, key):
            """
            Get a value from Redis by key.
            Args:
                key (str): The key to retrieve.
            Returns:
                Any: The unpickled value if found, None otherwise.
            """
            value = await self.redis.get(key)
            if value:
                return pickle.loads(value)
            return None

        async def clear_all(self):
            """Clear all keys and values from the Redis database."""
            await self.redis.flushall()


    async def demonstrate_redis_operations():
        """Demonstrate various Redis cache operations including storing and retrieving different data types."""
        client = redis.Redis(host="localhost", port=6379)
        await client.flushall()

        # Store and retrieve string value
        await client.set("string_key", "string-value")
        retrieved_string = await client.get("string_key")
        print(f"Retrieved string: {retrieved_string}")  # Retrieved string: b'string-value'

        # Store and retrieve list value
        await client.lpush("list_key", "list_item")
        retrieved_list = await client.lrange("list_key", 0, -1)
        print(f"Retrieved list: {retrieved_list}")  # Retrieved list: [b'list_item']

        # Store and retrieve dictionary value
        await client.hset("dict_key", mapping={"subkey": "value"})
        retrieved_dict = await client.hgetall("dict_key")
        print(f"Retrieved dict: {retrieved_dict}")  # Retrieved dict: {b'subkey': b'value'}

        # Attempt to store nested data structure (list of dict)
        try:
            await client.lpush("nested_list_key", {"subkey": "value"})
            retrieved_nested_list = await client.lrange("nested_list_key", 0, -1)
            print(
                f"Retrieved nested list: {retrieved_nested_list}"
            )  # Invalid input of type: 'dict'. Convert to a bytes, string, int or float first.
        except Exception as e:
            print(
                f"Error storing nested structure: {e}"
            )  # Error storing nested structure: [Some error message]

        # Attempt to store Python object (UUID)
        try:
            await client.set("uuid_key", uuid4())
            retrieved_uuid = await client.get("uuid_key")
            print(
                f"Retrieved UUID: {retrieved_uuid}"
            )  # This will not be printed due to the exception
        except Exception as e:
            print(f"Error storing UUID: {e}")  # Error storing UUID: [Some error message]

        # Store and retrieve Python objects using pickle serialization
        await client.set("serialized_dict_key", pickle.dumps({"subkey": "value"}))
        retrieved_serialized_dict = pickle.loads(await client.get("serialized_dict_key"))
        print(
            f"Retrieved serialized dict: {retrieved_serialized_dict}"
        )  # Retrieved serialized dict: {'subkey': 'value'}
        print(
            f"Type of retrieved serialized dict: {type(retrieved_serialized_dict)}"
        )  # Type of retrieved serialized dict: <class 'dict'>

        await client.set("serialized_uuid_key", pickle.dumps(uuid4()))
        retrieved_serialized_uuid = pickle.loads(await client.get("serialized_uuid_key"))
        print(
            f"Retrieved serialized UUID: {retrieved_serialized_uuid}"
        )  # Retrieved serialized UUID: [UUID object]
        print(
            f"Type of retrieved serialized UUID: {type(retrieved_serialized_uuid)}"
        )  # Type of retrieved serialized UUID: <class 'uuid.UUID'>

        await client.aclose()

        print("\n\nRedisClient\n\n")

        # Lets try the same with the RedisClient we implemented
        redis_client = RedisClient("localhost", 6379)
        await redis_client.clear_all()

        # String example
        await redis_client.set("string_key", "string-value")
        retrieved_string = await redis_client.get("string_key")
        print(f"Retrieved string: {retrieved_string}")  # Retrieved string: string-value

        # List example
        await redis_client.set("list_key", ["item1", "item2", "item3"])
        retrieved_list = await redis_client.get("list_key")
        print(
            f"Retrieved list: {retrieved_list}"
        )  # Retrieved list: ['item1', 'item2', 'item3']

        # Dict example
        await redis_client.set("dict_key", {"key1": "value1", "key2": "value2"})
        retrieved_dict = await redis_client.get("dict_key")
        print(
            f"Retrieved dict: {retrieved_dict}"
        )  # Retrieved dict: {'key1': 'value1', 'key2': 'value2'}

        # Nested data structure
        await redis_client.set(
            "nested_list_key", [{"subkey": "value1"}, {"subkey": "value2"}]
        )
        retrieved_nested_list = await redis_client.get("nested_list_key")
        print(
            f"Retrieved nested list: {retrieved_nested_list}"
        )  # Retrieved nested list: [{'subkey': 'value1'}, {'subkey': 'value2'}]

        # UUID4 example
        await redis_client.set("uuid_key", uuid4())
        retrieved_uuid = await redis_client.get("uuid_key")
        print(f"Retrieved UUID: {retrieved_uuid}")  # Retrieved UUID: <UUID object>

        await redis_client.clear_all()
        await redis_client.close()


        if __name__ == "__main__":
            asyncio.run(demonstrate_redis_operations())