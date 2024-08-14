from collections import Collection

names = Collection(['taylor', 'abigail', None])

result = names.map(lambda name: str(name).upper() if name else '') \
        # Отфильтровываем пустые
    .reject(lambda name: name == '')

# Выводим коллекцию на экран
print(result.all())  # => ['TAYLOR', 'ABIGAIL']
