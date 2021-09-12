# input():ユーザーの入力した値（文字列）を取得する

# age = input('何歳ですか？')
# print('あなたは{}歳です'.format(age))

# challenge1

age = int(input('何歳ですか？'))
casino_age = 18
#
# if age >= casino_age:
#     print('どうぞお入りください')
# else:
#     print('{}歳未満の方はカジノへは入れません'.format(casino_age))

# challenge2
game_text = '''プレイするゲームを選択してください
1: ルーレット
2: ブラックジャック
3: ポーカー
'''

if not age >= casino_age:
    print('{}歳未満の方はカジノへは入れません'.format(casino_age))
else:
    num = int(input(game_text))
    if num == 1:
        print('ルーレット')
    elif num == 2:
        print('ブラックジャック')
    elif num == 3:
        print('ポーカー')
