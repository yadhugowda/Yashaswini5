#Implement a Banking Account

class Account:
    def _init_(self,title=0,balance=0):
        self.title=title
        self.balance=balance

class SavingAccount(Account):
    def _init_(self,title,balance,interestRate):
        self.interestRate=interestRate
        super(). _init_(title,balance)

    def display(self):
        return(f"{self.title} is the title ,and  {self.balance} is the balance,and {self.interestRate} is the interestRate")


obj=SavingAccount("yashu",2000,5) 
print(obj.display())