


import accounts

account_num=int(input('welcome, to atm, enter your account number:'))
account_index=-1
counter=-1
for a in accounts.accounts_numbers:
    counter=counter+1
    if a==account_num:
        accounts.current_user_index=a
        break

if accounts.current_user_index==-1:
    print('account number does not exists')
else:
    passkey=int(input('enter your passkey'))
    if passkey==accounts.accounts_passkeys[counter]:
     while True:
        choice=int(input('1.withdraw money.\n2.transfer money to another account.\n3.deposit money.\n4.display balance.\n5.exit'))
        if choice==1:
            accounts.withdraw(int(input('enter money amount:')))
        elif choice==2:
            money = int(input('enter money amount:'))
            if money > accounts.accounts_balances[counter]:
                print('not enough money in your balance')
            else:
                c=int(input('enter account number you want to transfer to:'))
                count=-1
                for a in accounts.accounts_numbers:
                    count=count+1
                    if a==c:
                        accounts.accounts_balances[counter] = accounts.accounts_balances[counter] - money
                        accounts.accounts_balances[count]=accounts.accounts_balances[count]+money
                        print('money transfered succefully')
                        break
        elif choice==3:
            money=int(input('inter money amount:'))
            accounts.accounts_balances[counter] = accounts.accounts_balances[counter] + money
            print('deposit done succefully')
        elif choice==4:
            print('your balance equal',accounts.accounts_balances[counter])
        else:
            break

