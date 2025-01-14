from abc import ABC, abstractclassmethod

class Account(ABC):
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance # Encapsulated Attribute

    @abstractclassmethod
    def deposit(self, amount):
        pass
    
    @abstractclassmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.__balance
    
class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner,balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            return "Invalid input"
    
    def apply_interest(self):
        self.__balance += self.__balance * self.interest_rate

class ChequingAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=100):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            return "Invalid input"
    
def print_account_details(account):
    print(f"Owner: {account.owner}")
    print(f"Balance: {account.get_balance()}")

def process_amount(account, transaction_type, amount):
    if transaction_type == "deposit":
        account.deposit(amount)
    elif transaction_type == "withdraw":
        account.withdraw(amount)

# Creating instances of Saving account and Chequing Account

savings = SavingsAccount("Bob", 1000)
chequing = ChequingAccount("Jack", 500)

# using polymorphism

print_account_details(savings)
print_account_details(chequing)