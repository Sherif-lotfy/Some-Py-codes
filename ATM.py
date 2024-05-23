class Account:
    def __init__(e):
        print("*******WELCOME TO BANK OF HSBC*******")
        print("-------------------------------------------------")
        print("----------ACCOUNT CREATION----------")
        e.userName = input("Enter your Name: ")
        e.accountNumber = int(input("Enter your account number: "))
        e.Balance = 0
        print("Congratulations! Account created successfully...\n")
        x = input("Do you want to do any transaction?(y/n): ")
        print()
        if x.lower() == "y":
            e.transactions()
        else:
            print("Thanks for choosing us as your bank")
            print("******************************************")

    def transactions(e):
        print("   TRANSACTION ")
        print("*********************")
        print("Menu:")
        print("1. Account Detail")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")
        print("*********************\n")
        
        while True:
            tAction = int(input("Enter 1, 2, 3, 4 or 5: "))
            if tAction == 1:
                e.accountDetail()
            elif tAction == 2:
                e.checkBalance()
            elif tAction == 3:
                e.deposit()
            elif tAction == 4:
                e.withdraw()
            elif tAction == 5:
                e.exit()
                break
            else:
                print("Invalid number.. please try again with a valid number...")

    def accountDetail(e):
        print("\n----------ACCOUNT DETAIL----------")
        print("Account Holder:", e.userName)
        print("Account Number:", e.accountNumber)
        print("Available balance:", e.Balance, "\n")

    def checkBalance(e):
        print("Available balance: LE.", e.Balance, "\n")

    def deposit(e):
        a = float(input("How much you want to deposit(LE.): "))
        while a < 0:
            a = float(input("Invalid number... try again: "))
        e.Balance += a
        print("Current account balance: LE.", e.Balance, "\n")

    def withdraw(e):
        w = float(input("How much you want to withdraw(LE.): "))
        while w < 0:
            w = float(input("Invalid number... try again: "))
        if w > e.Balance:
            print("Insufficient fund!")
            print("Your balance is LE.", e.Balance ," only.")
            print("Try with lesser amount than balance.\n")
        else:
            e.Balance -= w
            print("LE.", w, "withdrawal successful!")
            print("Current account balance: LE.", e.Balance, "\n")

    def exit(e):
        print("\n    Printing receipt..............")
        print("******************************************")
        print("Transaction is now complete.")
        print("Transaction number: 213121")
        print("Account holder:", e.userName)
        print("Account number:", e.accountNumber)
        print("Available balance:", e.Balance)
        print("Thanks for choosing us as your bank")
        print("******************************************")

A = Account()

