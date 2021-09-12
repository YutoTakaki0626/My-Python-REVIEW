import time

class Account:

    account_number = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = Account.account_number
        self.show_balance()
        self.transaction = []
        Account.account_number += 1

    def withdraw(self):
        while True:
            money = int(input('いくらおろされますか？：'))
            if money > self.balance:
                print(f'口座番号:{self.account_number} 口座名: {self.name} 様　{money}円を引き出すためには残高が足りません')
            else:
                self.balance -= money
                self.show_balance()
                self.update_transaction(-money)
                break

    def deposit(self):
        money = int(input('いくら振り込まれますか？：'))
        self.balance += self.balance
        self.update_transaction(money)
        self.show_balance()

    def show_balance(self):
        print(f'口座番号:{self.account_number} 口座名: {self.name} 様　残高は{self.balance}円です')

    def update_transaction(self, money):
        new = {'withdraw/deposit': money, 'balance': self.balance, '日時': Account.get_time()}
        self.transaction.append(new)
        print(self.transaction)

    @staticmethod
    def get_time():
        current_time = time.localtime()
        return '{0.tm_year}年{0.tm_mon}月{0.tm_mday}日{0.tm_hour}時{0.tm_min}分'.format(current_time)

    def show_transaction_history(self):
        for trans in self.transaction:
            trans_str_list = []
            for k, v in trans.items():
                trans_str_list += f'{k}: {v}'
            print(', '.join(trans_str_list))


hiroshi = Account('hiroshi', 9803230)
takeda = Account('takeda', 1263)
yoshiki = Account('yoshiki', 732980)

print(hiroshi.account_number)
print(yoshiki.account_number)

# takeda.withdraw()
# hiroshi.deposit()
# takeda.deposit()



