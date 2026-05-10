print("\n\nWelcome in Password Checker!\n")
while True:
    password = input("Enter Your Password: ")
    if " " in password:
        print("The Password Must not Have space in it")
        continue
    elif len(password) < 9:
        print("The Password must be 8 character at Least")
        continue
    elif "@" not in password:
        print("The Password Must have @ in it")
        continue
    else: break