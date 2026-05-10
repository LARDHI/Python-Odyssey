balance = 0
choose = 0
def menu(balance):
    print("\n\n\nWelcome To The Online Bank!")
    print("\nThe Balance:", balance)
    print("1.Deposit To Balance")
    print("2.Withdraw From Balance")

def deposit(balance, amount):
    balance += amount
    return balance
def withdraw(balance, amount):
    balance -= amount
    return balance
while True:
    menu(balance)
    choose = input("Choose an Option: ")
    if choose == "1":
         amount = int(input("Enter The Amount: "))
         balance = deposit(balance, amount)
         continue
    elif choose == "2":
        amount = int(input("Enter The Amount: "))
        if amount <= balance:
            balance = withdraw(balance, amount)
            continue
        else: 
            print("The amount Greater Then The Balance!")
            continue
    else: break