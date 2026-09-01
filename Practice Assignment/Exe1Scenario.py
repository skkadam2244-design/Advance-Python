class ATM:
    # Class variable
    bank_name = "ABC Bank"

    def __init__(self, name, balance=0):
        # Private instance variable
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully.")
            print("Current Balance:", self.__balance)
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        # Withdrawal validation
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > 25000:
            print("Withdrawal limit is Rs. 25,000 per transaction.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print("Please collect your cash.")
            print("Remaining Balance:", self.__balance)

    def check_balance(self):
        print("Account Holder:", self.name)
        print("Bank:", ATM.bank_name)
        print("Available Balance:", self.__balance)

    def menu(self):
        while True:
            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.check_balance()

            elif choice == "2":
                amount = float(input("Enter deposit amount: "))
                self.deposit(amount)

            elif choice == "3":
                amount = float(input("Enter withdrawal amount: "))
                self.withdraw(amount)

            elif choice == "4":
                print("Thank you for using", ATM.bank_name)
                break

            else:
                print("Invalid choice. Please try again.")


# Create ATM object
user = ATM("Shree", 10000)

# Start ATM
user.menu()