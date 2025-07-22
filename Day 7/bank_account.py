class BankAccount:
    def __init__(self,owner,amount):
        self.__balance=amount
        self.owner=owner
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
    def withdraw(self,amount):
        if amount>self.__balance:
            print("Insufficient balance")
        else:
            self.__balance-=amount
    def get_balance(self):
        return self.__balance

b=BankAccount("John",1200)
b.deposit(500)
b.withdraw(200)
b.withdraw(2000)
print(b.get_balance())