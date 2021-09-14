def myrange(stop):
    start = 0
    while start < stop:
        yield start
        start += 1

mr = myrange(10)
#
# for i in mr:
#     print(i)

# print(next(mr))
# print(next(mr))
# print(next(mr))
# print(next(mr))
# print(next(mr))
# print(next(mr))
# print(next(mr))
# print(next(mr))
# print(next(mr))
# print(next(mr))
# print(next(mr))

# challenge

def even(num):
    start = num
    while start > 0:
        if start % 2 == 0:
            yield start
        start -= 1

ev = even(10)
for i in ev:
    print(i)