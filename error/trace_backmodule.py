import traceback

def split_bill(price):
    num = input('何人で割り勘しますか？：')
    try:
        each = price / int(num)
    except ZeroDivisionError as e:
        print('0で割ることはできません。正しい値を入力してください')
    else:
        print(f'一人{each}円です')

def check(bill):
    total_bill = sum(bill.values())
    try:
        split_bill(total_bill)
    except ValueError:
        traceback.print_exc()
        print('エラーが出ました。やり直してください。')

if __name__ == '__main__':
    bill = {'burger': 500, 'pasta': 1400, 'egg': 200}
    check(bill)
    print('プログラムは問題なく実行されました')
