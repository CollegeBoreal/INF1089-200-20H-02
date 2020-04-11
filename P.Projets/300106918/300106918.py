accounts_numbers=[23410324,132432,9865665,596900,4654680,76432,86785342,5678888,734533,456045456]
accounts_passkeys=[2344,5433,7523,9806,4560,6454,5343,6565,3455,5677]
accounts_balances=[0,0,0,0,0,0,0,0,0,0]

account_num=int(input('welcome, to atm, enter your account number:'))
found_account=False
counter=-1
for a in accounts_numbers:
    counter=counter+1
    if a==account_num:
        found_account=True
        break

if found_account == False:
    print('account number does not exists')
else:
    passkey=int(input('enter your passkey'))
    if passkey==accounts_passkeys[counter]:
        choice=int(input('1.withdraw money.\n2.transfer money to another account.\n3.deposit money.\n4.display balance.\n'))
        if choice==1:
            money=int(input('enter money amount:'))
            if money>accounts_balances[counter]:
                print('not enough money in your balance')
            else:
                accounts_balances[counter]=accounts_balances[counter]-money
        elif choice==2:
            money = int(input('enter money amount:'))
            if money > accounts_balances[counter]:
                print('not enough money in your balance')
            else:
                c=int(input('enter account number you want to transfer to:'))
                count=-1
                for a in accounts_numbers:
                    count=count+1
                    if a==c:
                        accounts_balances[counter] = accounts_balances[counter] - money
                        accounts_balances[count]=accounts_balances[count]+money
                        break
        elif choice==3:
            money=int(input('inter money amount:'))
            accounts_balances[counter] = accounts_balances[counter] + money
        elif choice==4:
            print('your balance equal',accounts_balances[counter])