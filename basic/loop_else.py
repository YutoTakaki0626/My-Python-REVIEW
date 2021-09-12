fruits = ['apple', 'peach', 'grapes', 'banana']

# for else

# for fruit in fruits:
#     choice = input(f'あなたが探しているフルーツは{fruit}ですか？ y/n :')
#     if choice == 'y':
#         print('見つかって良かったですね')
#         break
#     else:
#         print('そうですか・・・')
#     print(fruit)
# else:
#     print('お探しのフルーツは見つかりませんでした')

# while else

balance = 1000
game_price = 200

while balance >= game_price:
    choice = input(f'1回{game_price}円のゲームに参加しますか？(残高:{balance}円)(y/n?):')
    if choice == 'y':
        balance -= game_price
    elif choice == 'n':
        print('また遊びましょう')
        break
    else:
        print('yかnかで答えてください')
else:
    print(f'あなたの残高は{balance}円です。')