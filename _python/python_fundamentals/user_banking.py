class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 1000
        self.wallet = 1
    
    def make_deposit(self, amount):
        if amount > self.wallet:
            print("not enough money to deposit")
        else : 
            self.account_balance += amount
            self.wallet -= amount
            print(f"{self.name}, Balance: ${self.account_balance}")
            print(f"Amount in wallet: ${self.wallet}")

    def displayUserbalance(self):
        print(f"{self.name}, Balance: ${self.account_balance}")



    def make_withdraw(self, amount):
        if amount > self.account_balance:
            print("insufficent funds in account balance!!")
        else :
            self.account_balance -= amount
            self.wallet += amount
            print(f"{self.name}, Balance: ${self.account_balance}")
            print(f"Amount in wallet: ${self.wallet}")
    
    def makeTransfer(self, recipient, amount):
        if amount > self.account_balance:
            print("insufficient funds in account balance!!")
        else:
            self.account_balance -= amount
            recipient.account_balance += amount
            self.displayUserbalance()
            recipient.displayUserbalance()
    

arnold = User("Arnold Su", "a.su@gmail.com")
arnold.displayUserbalance()