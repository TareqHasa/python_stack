from bank_account import BankAccount
class user :
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.account=BankAccount(int_rate=0.01,balance=0)
    
    def make_deposit(self,amount):
        self.account.balance+=amount
    
    def make_withdrawal(self, amount):
        self.account.balance-=amount

    def display_user_balance(self):
        print(self.name +" account balance is currently :" +" "+str(self.account.balance))

    def tarnsfer_money(self,other_user,amount):

        self.account.balance-=amount
        other_user.account.balance+=amount



tariq=user("tariq","tariq@bank.com")
aws=user("aws","aws@bank.com")
laith=user("laith","laith@bank.com")

tariq.make_deposit(10000)
tariq.tarnsfer_money(aws,2000)
tariq.display_user_balance()
aws.display_user_balance()
