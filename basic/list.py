# リスト(list): 複数のオブジェクトを順序づけて保存するデータ型

fruits = ['apple', 'peach', 'melon', 'grapes']

hetro_list = ['stting', 1, 3.4, True, fruits]

# print(hetro_list)
# print(fruits[0])
# print(fruits[-3])
# print(hetro_list[-1][-1])
# print('hello world'[3])

# .append: 新しいオブジェクトを追加する
fruits.append('banana')
# .insert: 指定したindexに指定したオブジェクトを追加する
fruits.insert(3, 'lemon')
# .remove: マッチした最初のオブジェクトを除く
fruits.remove('peach')
# .sort: 昇順に並び替える
fruits.sort()
fruits.sort(reverse=True)
# len(): リストの要素数を取得する
len(fruits)
