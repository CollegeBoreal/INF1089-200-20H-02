accounts_numbers=[23410324,132432,865665,595400,4654680,87657432,86785342,5678888,734533,456045456]
accounts_passkeys=[2344,5433,7523,9806,4560,6454,5343,6565,3455,5677]
accounts_balances=[50000,70000,0,0,0,0,0,0,0,0]

current_user_index=-1

def withdraw(money):
    if money > accounts_balances[current_user_index]:
        print('not enough money in your balance')
    else:
        accounts_balances[current_user_index] = accounts_balances[current_user_index] - money
        print('withdrawal done succefully')
def deposit(money):
    accounts_balances[current_user_index] =accounts_balances[current_user_index] + money
    print('deposit done succefully')

def transfer_money(money):
    if money > accounts_balances[current_user_index]:
        print('not enough money in your balance')
    else:
        c = int(input('enter account number you want to transfer to:'))
        count = -1
        for a in accounts_numbers:
            count = count + 1
            if a == c:
                accounts_balances[current_user_index] = accounts_balances[current_user_index] - money
                accounts_balances[count] = accounts_balances[count] + money
                print('money transfered succefully')
                break



