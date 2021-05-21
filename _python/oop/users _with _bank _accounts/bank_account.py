class BankAccount:
    def __init__ (self,int_rate,balance):
        self.int_rate=0.01
        self.balance=0

    def deposit (self,amount):
        self.balance += amount
        return self

    def withdraw (self,amount):
        
        if self.balance >= amount:
            self.balance -= amount
        else :
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
            
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest (self):
        if self.balance>0 :
            self.balance += self.balance * self.int_rate
        return self    

# account_1=BankAccount (.01 , 0)
# account_2=BankAccount (.02 , 0)

# account_1.deposit(100).deposit(200).deposit(300).withdraw(500).yield_interest().display_account_info()
# account_2.deposit(1000).deposit(300).withdraw(2000).withdraw(1000).yield_interest().display_account_info()