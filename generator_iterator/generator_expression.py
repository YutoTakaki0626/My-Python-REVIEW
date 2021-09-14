import sys

square_list = [num * num for num in range(10)]
print(square_list)

square_gen = (num * num for num in range(10))
print(next(square_gen))
print(next(square_gen))
print(next(square_gen))
print(next(square_gen))

print(sys.getsizeof(square_list))
print(sys.getsizeof(square_gen))

even_square = (num * num for num in range(10) if num % 2 == 0)