# if文

age = 23
age_alcohol = 20
if age >= age_alcohol:
    print('You can drink beer!')
else:
    print('You are too young to drink beer')

age_drive = 18
if age >= age_alcohol:
    print('You can drink beer')
elif age < age_drive:
    print('You cannot even drive')
else:
    print('You are not alloewd to drink beer but you can drive if you have a driver`s license')

if not 0 < age < 120:
    print('The value is valid')

# challenge1

balance = 100
withdrawal = 200

if balance > withdrawal:
    balance -= withdrawal
else:
    pass

# challenge2

withdrawal_limit = 1000000

if withdrawal > withdrawal_limit:
    print('The withdrawal limit is {}'.format(withdrawal_limit))
elif balance > withdrawal:
    balance -= withdrawal
    print('Your new balance is {}'.format(balance))
else:
    print('You don`t have money')