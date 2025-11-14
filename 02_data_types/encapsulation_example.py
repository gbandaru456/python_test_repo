class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance += amount
    def getbalance(self):
        return self.__balance
account = BankAccount(1500)
account.deposit(1000)
print(account.getbalance())


