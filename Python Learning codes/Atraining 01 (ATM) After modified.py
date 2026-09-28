password = "1234"
is_login = False
attempts = 3
User_choosen = 0
Balance = 1000.00
print("Welcome to this ATM!")

while attempts > 0:
    User_input = input("Please enter your password:")
    if User_input == password:
        print("The password is correct!")
        is_login = True
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"The password is wrong!You have {attempts} chances left")
        else:
            print("Sorry, you've made 3 wrong entries!Card locked")

if is_login:
    is_running = True
    while is_running:
        print("\n1.查询余额\n2.存款\n3.取款\n4.退出")
        choice = input("Enter the number to choose your service:")

        if choice == "1":
            print(f"The current balance is {Balance:.2f}")
        elif choice == "2":
            amount = float(input("Enter the deposit amount:"))
            if amount > 0:
                Balance += amount
                print(f"Deposit successful!Current balance:{Balance:.2f}")
            else:
                print("Sorry, the amount is invalid")
        elif choice == "3":
            amount = float(input("Enter the withdrawal amount:"))
            if amount <= 0:
                print("Sorry, the amount is invalid")
            elif amount > Balance:
                print(f"Sorry, insufficient balance!Current balance:{Balance:.2f}")
            else:
                Balance -= amount
                print(f"Withdrawal successful!Current balance:{Balance:.2f}")
        elif choice == "4":
            print("Thanks for using.Looking forward to seeing u again!")
            is_running = False
        else:
            print("Invalid option, please tyr again.")