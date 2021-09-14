class MyIterator:
    def __init__(self, start=0):
        self.current = start

    def __next__(self):
        num = self.current
        self.current += 1
        return num

    def __iter__(self):
        return self

my = MyIterator()

print(next(my))
print(next(my))
print(next(my))
print(next(my))
print(next(my))

# Challenge

class EvenIterator:
    def __init__(self, start=10):
        self.current = start

    def __next__(self):
        num = self.current
        if self.current < 2:
            raise StopIteration
        elif self.current % 2 == 0:
            num = self.current
            self.current -= 2
            return num
        else:
            self.current -= 1
            return self.__next__()

    def __iter__(self):
        return self

print('-' * 30)
my = EvenIterator()
print(next(my))
print(next(my))
print(next(my))
print(next(my))
print(next(my))