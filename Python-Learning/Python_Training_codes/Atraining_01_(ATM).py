password = "1234"
is_login = False
print("Welcome to this ATM!")
Numdecider1 = 3
User_choosen = 0
while Numdecider1 >= 1:
    User_input = input("Please enter your password:")
    if User_input == password:
        print("The password is correct!")
        is_login = True
        Numdecider = -1
        break
    else:
        if Numdecider1 > 1:
            Numdecider1 -= 1
            print(f"The password is wrong!You have {Numdecider1} chances left")
        else:
            print("Sorry, you've made 3 wrong entries!")
            break
usetimes = True
Balance = 1000.00
import decimal
decimal.Decimal(Balance)
while usetimes == True:
    if is_login:
        print("U can choose your service here:")
        print('''    1.查询余额
    2.存款
    3.取款
    4.退出''')
        User_choosen = 0
        User_choosen = int(input("Enter the number to choose your service :) :"))
        usetimes = False
    while User_choosen == 1:
        if User_choosen == 1:
            User_password = input("Please enter your password again to certify:")
            if User_password == password:
                print(f"The current balance is {Balance}\n")
                usetimes = True
                User_choosen = 0
                break
            else:
                print("Sorry, the password is wrong.\nTry again please.\n")
                usetimes = True
                User_choosen = 0
                break
    while User_choosen == 2:
        if User_choosen == 2:
            User_password = input("Please enter your password again to certify:")
            if User_password == password:
                Saved_balance = input("Enter the required deposit amount:")
                Saved_balance = float(Saved_balance)
                decimal.Decimal(Saved_balance)
                if Saved_balance > 0:
                    Balance = Balance + Saved_balance
                    decimal.Decimal(Balance)
                    print("The deposit completed!\n")
                    usetimes = True
                    User_choosen = 0
                    break
                else:
                    print("Sorry, the amount is not available\n")
                    usetimes = True
                    User_choosen = 0
                    break
            else:
                print("Sorry, the password is wrong.\nTry again please.\n")
                usetimes = True
                User_choosen = 0
                break
    while User_choosen == 3:
        if User_choosen == 3:
            User_password = input("Please enter your password again to certify:")
            if User_password == password:
                Withdrawal_balance = input("Enter the required withdrawal amount:")
                Withdrawal_balance = float(Withdrawal_balance)
                decimal.Decimal(Withdrawal_balance)
                if Withdrawal_balance > 0 and Withdrawal_balance <= Balance:
                    Balance = Balance - Withdrawal_balance
                    decimal.Decimal(Balance)
                    print("The withdrawal completed!\n")
                    usetimes = True
                    User_choosen = 0
                    break
                elif Withdrawal_balance > Balance:
                    print("Sorry, your balance is insufficient!\n")
                    usetimes = True
                    User_choosen = 0
                    break
                else:
                    print("Sorry, the amount is not available.\n")
                    usetimes = True
                    User_choosen = 0
                    break
            else:
                print("Sorry, the password is wrong.\nTry again please.\n")
                usetimes = True
                User_choosen = 0
                break
    while User_choosen == 4:
        if User_choosen == 4:
            print("Thanks for your using.\nLooking forward to seeing you again!")
            is_login = False
            break