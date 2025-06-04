class Account:
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. The balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal denied: Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}. The balance: ${self.balance:.2f}")

acc = Account("Oeeaeooaeeae", 100.0)
print(f"Account owner: {acc.owner}, Initial balance: ${acc.balance:.2f}\n")

acc.deposit(50)
acc.withdraw(30)
acc.withdraw(200)
acc.withdraw(-10)
acc.deposit(-20)