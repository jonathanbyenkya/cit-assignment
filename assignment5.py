#Using classes, Create a basic banking application with the following features:

# Create a class called BankAccount with the following attributes:

# account_number - a string
# balance - a float
# owner - a string
# type - a string
# Create a class called Bank with the following attributes:

# name - a string
# accounts - a list of BankAccount objects
# Create a class called Customer with the following attributes:

# name - a string
# accounts - a list of BankAccount objects
# Create a class called Transactions with the following attributes:

#  1. `account` - a `BankAccount` object
#  2. `amount` - a float
#  3. `type` - a string
# The application should have the following functionality:

# Create a new Bank object
# Create a new Customer object
# Create a new BankAccount object
# Add the BankAccount object to the Bank object
# Add the BankAccount object to the Customer object
# Print the Bank object
# Print the Customer object
# Print the BankAccount object
# Create a new Transaction object
# Add the Transaction object to the BankAccount object





class BankAccount:

    def __init__(self, account_number: str, balance: float, owner: str, type: str):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.type = type
    def __repr__(self) -> str:
        return (f"Account Number: {self.account_number}, Available balance: {self.balance}, Account Owner: {self.owner}, Account Type: {self.type}..... ")

    # def Transactions(self, BankAccount, amount, type):
    #     if type == "Deposit":
    #         balance = BankAccount.balance + amount
    #     elif type == "Withdraw":
    #         balance = BankAccount.balance - amount
    #     else:
    #         balance = BankAccount.balance
    #     return (BankAccount) - need some help here sir
  

class Bank:
        def __init__(self, name: str, accounts: list["BankAccount"]):
            self.name = name
            self.accounts = accounts

        def __repr__(self):
            return(f"Welcome to {self.name} Bank, Open any one of the available accounts to get started: {self.accounts}..... ")
            
        def add_BankAccount(self, account_number):
            self.account.add(account_number)
            return(Bank)


class Customer:

    def __init__(self, name: str, account: list):
        self.name = name
        self.account = account

    def __repr__(self):
        return (f"The customer {self.name} has the following account details: {self.account}.......")

    def add_account(self, account):
        self.account.append(account)
        return(Customer)


class Transactions:

    def __init__(self, account: "BankAccount", amount: float, type: str):
        self.account = account
        self.amount = amount
        self.type = type

    def __repr__(self):
        return(f'DETAILS! {self.account}, Transaction type: {self.type}, Amount in question: {self.amount}......')
 

           
#create a new bank object
myBank = Bank("Pheonix", ['Savings', 'Current', 'Fixed Deposit', 'Student'])

#create a new customer object
new_customer = Customer('Jonathan', ['Fixed deposit account', 'Account number 0123456789'])

# Create a new BankAccount object
my_account = BankAccount(9876543210, 10000000, "Jonathan Mbonabyenkya", "Savings")

# Add the BankAccount object to the Bank object
bank = Bank(myBank, 9876543210)

# Add the BankAccount object to the Customer object
customer = Customer("Jonathan", my_account)

# Print the Bank object
print(myBank)

# Print the Customer object
print(new_customer)

# Print the BankAccount object
print(my_account)

# Create a new Transaction object

mytransaction = Transactions(my_account, 200000, "deposit")
print(mytransaction)

# # Add the Transaction object to the BankAccount object
# post_transact = Transactions(my_account, 200000, "Deposit")
# print(post_transact) - need some help here sir 