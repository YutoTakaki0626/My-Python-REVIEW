# whileループ
# count = 0
# while count < 10:
#     print(count)
#     count += 1

# breakとcontinue
# while True:
#     age = int(input('あなたは何歳ですか'))
#     if not 0 <= age <=120:
#         print('入力された値は正しくありません')
#         continue
#     else:
#         print(f'あなたは{age}歳です')
#         break

# challenge

age = int(input('何歳ですか？:'))
casino_age = 18

game_text = '''プレイするゲームを選択してください
1: ルーレット
2: ブラックジャック
3: ポーカー
'''

if not age >= casino_age:
    print('{}歳未満の方はカジノへは入れません'.format(casino_age))
else:
    num = 0
    
    while not 1 <= num <= 3:
        num = int(input(game_text))

    if num == 1:
        print('ルーレット')
    elif num == 2:
        print('ブラックジャック')
    elif num == 3:
        print('ポーカー')