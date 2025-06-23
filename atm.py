import bank_balance 
pin = 1234
if 'card'==input('Insert your card'):
    print ('Welcome')
    if pin==int(input('Enter your pin')):
        print('''1) check balance\n2) cash withdraw''')
        option=int(input('select your option'))
    if option==1:
        print('your current balance is',bank_balance.amountcard
              )
    elif option==2:
        user_amount=int(input('enter your amount'))
        bank_balance = bank_balance.amount-user_amount
        file = open('bank_balance.py','w')
        file.write(f'amount={bank_balance} ')
        file.close()
    else:
        print('Wrong Pin')
else:
    print('Invalid card')   