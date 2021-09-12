# for

fruits = ['apple', 'peach', 'grapes', 'banana']
#
# for fruit in fruits:
#     print(f'I love {fruit}!!')
#
# for char in 'hello world!!':
#     print(f'char:{char}')

# iteration と iterable

# challenge1

fav = input('好きなフルーツはなんですか:')

for fruit in fruits:
    if fav == fruit:
        print('{}は好き'.format(fruit))
    else:
        print('{}は好きじゃない'.format(fruit))

# challenge2

like = []
dislike = []

for fruit in fruits:
    favorite = input('{}は好きですか？yes or no:'.format(fruit))
    if favorite == 'yes':
        like.append(fruit)
    else:
        dislike.append(fruit)

print(like)
print(dislike)
