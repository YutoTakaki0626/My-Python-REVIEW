# is演算子:同じオブジェクトかどうかを判定する
a = 1
b = 1
c = 3
d = a
e = 2 - 1
print(id(1))
print(id(a))
print(id(b))
print(a is b)
print(a is not c)

hello = 'hello'
hello2 = 'h' + 'e' + 'l' + 'l' + 'o'
print(hello is hello2)
hello = 'konnichiwa'
print(hello is hello2)

# Noneかどうかの判定によく使う

nothing = None
print(id(nothing))