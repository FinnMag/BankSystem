class Account(object):
    def __init__(self):
        f = open("demofile.txt", "r")
        print(f.read())


class SavingAccount(Account):
    pass

class CheckingAccount(Account):
    pass

class Customer():
    def __init__(self):
        pass
    
    def createAccount(self):
        test = 'Hello World'
        f = open("customers.txt", "a")
        f.write(test)
        f.close()

def manageFunds():
    print("\nYou have chosen to mangage your funds\n")
    print("1. View Balance")
    print("2. Deposit")
    print("3. Transfer")
    print("4. Withdraw")
    print("5. Return")
    
    return int(input("\nPlease enter an option: "))

    
end = 1
while end != 0:
    print("\nWelcome to the Bank!\n")
    print("\nPlease select an option:")

    print("1. Manage Funds")
    print("2. Manage Accounts")
    print("3. Exit")

    option = int(input("\nPlease enter an option: "))

    if option == 1:
        fundOption = manageFunds()
        
        #Views Balance
        if fundOption == 1:
            print("You have selected to view balance")
        
            account = Customer()
            account.createAccount()
      
            

        
        













