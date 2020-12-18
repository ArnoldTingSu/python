class BankAccount:
    def __init__(self, int_rate, balance):
        self.interestRate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self

    def withdraw(self, amount):
        self.balance -= amount
        print(self.balance)
        return self
    
    def account_balance(self):
        print(f"Balance : ${self.balance}")
        return self
    

    def yield_interest(self):
        #print(f"Your current balance : ${self.balance}")
        #print(f"Your current interest rate is {self.interestRate}")
       self.balance =  self.balance * (self.interestRate + 1)
       print(f"Your new balance is : ${self.balance}")
       return self
    

class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(.004, 10000)
        self.wallet = 1000
    
    def make_deposit(self, amount):
        if amount > self.wallet:
            print("not enough money to deposit")
            return self
        else : 
            self.account.balance += amount
            self.wallet -= amount
            print(f"{self.name}, Balance: ${self.account.balance}")
            print(f"Amount in wallet: ${self.wallet}")
            return self

    def user_balance(self):
        print(f"{self.name}, Balance: ${self.account.balance}")
        return self


    def make_withdraw(self, amount):
        if amount > self.account.balance:
            print("insufficent funds in account balance!!")
        else :
            self.account.balance -= amount
            self.wallet += amount
            print(f"{self.name}, Balance: ${self.account.balance}")
            print(f"Amount in wallet: ${self.wallet}")
            return self
    
    def makeTransfer(self, recipient, amount):
        if amount > self.account:
            print("insufficient funds in account balance!!")
            return self
        else:
            self.account.balance -= amount
            recipient.account.balance += amount
            self.user_balance()
            recipient.displayUserbalance()
            return self
    

arnold = User("Arnold Su", "a.su@gmail.com")



