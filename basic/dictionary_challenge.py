# challenge

age = int(input('何歳ですか？:'))
casino_age = 18

game_dict = {'1': 'ルーレット', '2': 'ブラックジャック', '3': 'ポーカー'}

if age >= casino_age:
    print('どうぞお入りください')

    while True:
        print('プレイするゲームを選択してください：')
        for num, game_name in game_dict.items():
            print(f'{num}:{game_name}')
        game = input(':')

        if game in game_dict:
            print('あなたは{}を選びました'.format(game_dict[game]))
            break
        else:
            print('1~3を選んでください')
else:
    print('{}歳未満の方はカジノへは入れません'.format(casino_age))
