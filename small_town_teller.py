cust_dict = {}
acct_dict = {}
acct_types = ['checking','savings']

class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id,
        self.first_name = first_name,
        self.last_name = last_name

class Account:
    def __init__(self, number, type, owner, balance = 0.00):
        self.number = number,
        self.type = type,
        self.owner = owner,
        self.balance = balance

class Bank(Person, Account):
    def __init__(self):
        pass

    def add_customer(self, id, first_name, last_name):
        if (id not in cust_dict):
            cust_dict[id] = first_name + " " + last_name
        else:
            print('That id is already in use.')

    def add_account(self, id, number, type):
        self.id = id,
        self.number = number,
        self.type = type
        if self.id in cust_dict:
            self.acct_dict[self.number] = self.id

    def remove_account(self, account):
        pass

    def deposit(self):
        deposit_amount = float(input('Enter a deposit amount: '))
        self.balance += deposit_amount
        print(f"{deposit_amount} deposited.")

    def withdraw(self):
        withdraw_amount = float(input('Enter a deposit amount: '))
        if withdraw_amount > self.balance:
            print("Insufficient funds")
            print("Your max withdrawal amount is {self.balance-self.withdraw_amount}")
        else:
            self.balance += withdraw_amount
            print(f"{withdraw_amount} withdrawn.")

    def balance_inquiry(self):
        print(f"Your balance is {self.balance}")

my_bank = Bank()
my_bank.add_customer(1,'Alex', 'Apple')
print(cust_dict)
my_bank.add_customer(2,'Barry', 'Banana')
print(cust_dict)
my_bank.add_account(1,1,'checking')
print(acct_dict)