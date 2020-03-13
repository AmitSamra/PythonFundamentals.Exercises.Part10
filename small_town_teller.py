cust_dict = {}
acct_dict = {}
acct_type = ['Checking','Savings']

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
            print(f"Customer {first_name + ' ' + last_name} with ID {id } created.")
        else:
            print('That ID is already in use.')

    def add_account(self, id, number, type):
        if id in cust_dict and type == 'Checking':
            acct_dict[id] = {number:type}
            print(f"{acct_type[0]} account created for {cust_dict[id]}.")
        elif id in cust_dict and type == 'Savings':
            acct_dict[id] = {number:type}
            print(f"{acct_type[1]} account created for {cust_dict[id]}.")

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
my_bank.add_customer(2,'Barry', 'Banana')
my_bank.add_account(1,100,'Checking')
my_bank.add_account(1,101,'Savings')