# mutable: 変更可能なオブジェクト list, dict, set
fruits = ['apple', 'peach', 'banana']
print(f'fruitsのIDは{id(fruits)}')
fruits.append('lemon')
print(fruits)
print(f'fruitsのIDは{id(fruits)}')

# immutable: 変更不可能なオブジェクト int, float, str, bool, tuple
fruits = 'apple'
print(f'fruitsのIDは{id(fruits)}')
fruits += ', lemon'
print(fruits)
print(f'fruitsのIDは{id(fruits)}')

# メモリ効率が悪い
text = ''
for i in range(1, 11):
    if i == 1:
        text += str(i)
    else:
        text += '-' + str(i)
print(text)

# 効率的なコード
text = []
for i in range(1, 11):
    text.append((str(i)))
text = '-'.join(text_list)
print(text)