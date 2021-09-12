# dictionary:キーと値の組み合わせを複数保持するデータ型
fruits_colors = {'apple':'red', 'lemon': 'yellow', 'grapes': 'purple'}

print(fruits_colors['apple'])
fruits_colors['peach'] = 'pink'
print(fruits_colors)

dict_sample = {1: 'one', 'two': 2, 'three': [1, 2, 3], 'four':{'inner': 'dict'}}
print(dict_sample)
print(dict_sample['four']['inner'])

# .keys() .values()
for fruit in fruits_colors.keys():
    print(fruit)

# .items()
for fruit, color in fruits_colors.items():
    print(f'{fruit} is {color}')