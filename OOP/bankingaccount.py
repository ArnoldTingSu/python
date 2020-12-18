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
    
    def display_account_info(self):
        print(f"Balance : ${self.balance}")
        return self
    

    def yield_interest(self):
        #print(f"Your current balance : ${self.balance}")
        #print(f"Your current interest rate is {self.interestRate}")
       self.balance =  self.balance * (self.interestRate + 1)
       print(f"Your new balance is : ${self.balance}")
       return self
    

        

arnold = BankAccount(.004, 4000)
