class BankAccount:
    def __init__(self,account_holder,balance=0):
        self.account_holder=account_holder
        self.__balance=balance
    def deposit(self,amount):
        self.__balance += amount
        print(f"Deposited: ${amount}")
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"withdrew : {amount}")
        else:
            print(f"Insufficient balance")
    def get_balance(self):
        return self.__balance

account= BankAccount('Govardhan',1000)
print("Balance :",account.get_balance())
account.deposit(200)
print("Balance :",account.get_balance())
account.withdraw(500)
print("Balance :",account.get_balance())

