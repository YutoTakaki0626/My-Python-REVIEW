# in演算子
fruits = ['apple', 'peach', 'grapes', 'banana']
print('lemon' not in fruits)
print('h' in 'hello')

# Challenge

user = input('好きなフルーツ：')
if user in fruits:
    fruits.remove(user)
    print(fruits)
else:
    fruits.append(user)
    print(fruits)