class ATM:
    def __init__(self, account_balance=0.0):
        self.account_balance = account_balance
        self.pin = None
        self.transaction_history = []

    def set_pin(self, pin):
        self.pin = pin
        print("PIN has been set successfully.")

    def validate_pin(self, entered_pin):
        return self.pin == entered_pin

    def account_balance_inquiry(self):
        print(f"Your current balance is: ${self.account_balance:.2f}")
        self.transaction_history.append("Balance Inquiry")

    def cash_withdrawal(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        if amount > self.account_balance:
            print("Insufficient balance!")
        else:
            self.account_balance -= amount
            print(f"Withdrawal successful. You withdrew ${amount:.2f}.")
            self.transaction_history.append(f"Withdrew ${amount:.2f}")

    def cash_deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.account_balance += amount
        print(f"Deposit successful. You deposited ${amount:.2f}.")
        self.transaction_history.append(f"Deposited ${amount:.2f}")

    def pin_change(self, current_pin, new_pin):
        if self.validate_pin(current_pin):
            self.pin = new_pin
            print("PIN successfully changed.")
            self.transaction_history.append("PIN Change")
        else:
            print("Incorrect current PIN. PIN change failed.")

    def transaction_history_inquiry(self):
        if not self.transaction_history:
            print("No transactions to show.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(f"- {transaction}")


def atm_interface():
    atm = ATM(account_balance=500.0)

    print("Welcome to the ATM!")
    while atm.pin is None:
        pin = input("Please set your 4-digit PIN: ")
        if len(pin) == 4 and pin.isdigit():
            atm.set_pin(pin)
        else:
            print("Invalid PIN. Please enter a 4-digit number.")

    while True:
        print("\nPlease choose an option:")
        print("1. Account Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            atm.account_balance_inquiry()
        
        elif choice == "2":
            amount = float(input("Enter the amount to withdraw: $"))
            atm.cash_withdrawal(amount)
        
        elif choice == "3":
            amount = float(input("Enter the amount to deposit: $"))
            atm.cash_deposit(amount)
        
        elif choice == "4":
            current_pin = input("Enter your current PIN: ")
            new_pin = input("Enter your new PIN: ")
            atm.pin_change(current_pin, new_pin)
        
        elif choice == "5":
            atm.transaction_history_inquiry()
        
        elif choice == "6":
            print("Thank you for using the ATM. Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")

atm_interface()
