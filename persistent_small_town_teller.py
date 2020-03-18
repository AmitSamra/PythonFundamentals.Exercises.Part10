import pickle

class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

class Account:
    def __init__(self, number, type, owner, balance = 0):
        self.number = number
        self.type = type
        self.owner = owner
        self.balance = balance

class Bank():
    def __init__(self):
        self.cust = []
        self.acct = {}
        self.acct_type = ['CHECKING', 'SAVINGS']

    def add_customer(self, person):
        if person.id not in self.cust:
            self.cust.append(person.id)
        else:
            raise ValueError('That ID already exists')

    def add_account(self, account):
        if account not in self.acct:
            self.acct[account.number] = account.balance
        else:
            raise ValueError('That account already exists')

    def remove_account(self, account):
        if account in self.acct:
            del[self.acct[account]]

    def deposit(self, account, amount):
        self.acct[account] += amount

    def withdraw(self, account, amount):
        if amount <= self.acct[account]:
            self.acct[account] -= amount
        else:
            print("Insufficient funds")
            print("Your max withdrawal amount is {self.balance-self.withdraw_amount}")

    def balance_inquiry(self, account):
        print(f"Balance: {self.acct[account]}")

    def save_data(self):
        PersistenceUtils.write_pickle("customers.pkl", self.cust)
        PersistenceUtils.write_pickle("accounts.pkl", self.acct)

    def load_data(self):
        self.cust = PersistenceUtils.read_pickle("customers.pkl")
        self.acct = PersistenceUtils.read_pickle("accounts.pkl")

class PersistenceUtils():

    @staticmethod
    def write_pickle(path, data):
        with open(path, 'wb') as f:
            pickle.dump(data, f)

    @staticmethod   
    def read_pickle(path):
        with open(path, 'rb') as f:
            data = pickle.load(f)
        return data

my_bank = Bank()
alex = Person(1,'Alex','Apple')

my_bank.add_customer(alex)
print(my_bank.cust)

alex_savings = Account(1001, "SAVINGS", alex)
print(my_bank.acct)

my_bank.add_account(alex_savings)
print(my_bank.acct)

my_bank.deposit(1001, 500)
print(my_bank.acct)

my_bank.withdraw(1001, 100)
print(my_bank.acct)

#my_bank.remove_account(1001)
#print(my_bank.acct)

my_bank.balance_inquiry(1001)

my_bank.save_data()
my_bank.load_data()