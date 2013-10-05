class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance

    def info(self):
        print(self.__balance)
