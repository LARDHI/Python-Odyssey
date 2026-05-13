print("\n\nWelcome in Password Checker!\n")
while True:
    counter = 3
    password = input("Enter Your Password: ")
    if " " in password or len(password) < 9 or "@" not in password:
        if " " in password:
            print("The Password Must Not Have Space")
            counter -= 1
        if len(password) < 9:
            print('The Password Must be 8 character at Least')
            counter -= 1
        if "@" not in password:
            print("The Password Must have @ in it")
            counter -= 1

        if counter == 2:
            print("Your Password is Medium")
        elif counter == 1:
            print("Your Password is Weak")
        else: print("Try Another Password!")
        continue
    else: 
        print(f'Your Password: {password} is Strong and Passed!')
        break