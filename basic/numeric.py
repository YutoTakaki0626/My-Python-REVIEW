# 数値型:integer, float, complex

print(type(1))

print(type(0.1))
print(0.1+0.1+0.1)

# Numeric Operator 数値演算子
print(1 + 0.4)
print(1 - 0.4)
print(2 * 3)
print(1 / 2)
print(5 * 6 - 3 / 6)

result = 1 + 1.0
print(result)

# floor division
print(14 // 3)
# modulo
print(14 % 3)
#exponentiation
print(2 ** 3)

hint_point = 100
attack_point = 40.3
remain = hit_point - attack_point
print(f'remain hit point is {remain}')

# augmented assignment +=, -=, *=, /=
a = 1
a = a + 1
a += 1 # a = a + 1と同じ
print(a)