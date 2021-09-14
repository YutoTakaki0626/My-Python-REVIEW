fruits = ['apple', 'lemon', 'peach']

print(next(fruits))

fruits_iterator = iter(fruits)
print(next(fruits_iterator))
print(iter(fruits_iterator))