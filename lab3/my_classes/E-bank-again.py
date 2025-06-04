class Account:

    def __init__(self):
        self.name = input("What is your name?: ")
        self.balance = int(input("How much money you want to put on your account?: "))

    def deposit(self):
        self.amount = int(input("How much?: "))
        if self.amount > self.balance:
            print(f"You can't put more than you have. Balance: ${self.balance:.2f}")
        elif self.amount <= 0:
            print("Deposit denied: Incufficient funds.")
        else:
            self.balance += self.amount
            print(f"Deposited: {self.amount:.2f}$, Your balance is: {self.balance:.2f}$")
    
    def withdraw(self):
        self.amount = int(input("How much?: "))
        if self.amount > self.balance:
            print("Withdrawal denied: Incufficient funds.")
        elif self.amount <= 0:
            print("Withdrawal denied: Amount must be positive.")
        else:
            self.balance -= self.amount
            print(f"Withdrew: {self.amount:.2f}$. The balance: {self.balance:.2f}$")

acc = Account()
print(f"Account owner: {acc.name}, Initial balance: {acc.balance:.2f}. To do operations write 'withdraw' or 'deposit'. If you want to check your balance write 'balance' To quit press 'q' button.\n")

while True:
    users_wish = input("What do you want to do with your bank account?: ")
    if users_wish == "q":
           print("Quitting...")
           break
    if users_wish == "withdraw":
        acc.withdraw()
    elif users_wish == "deposit":
        acc.deposit()
    elif users_wish == "balance":
        print(f"Your balance is {acc.balance}.")
    else:
        print("Unknown command.")