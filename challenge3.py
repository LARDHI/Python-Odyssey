def check_password(pw):
    issue = []
    if " " in pw:
        issue.append("The Password Must not Have Spaces")
    if len(pw) <= 8:
        issue.append("The Password Must be 8 characters at least")
    if "@" not in pw:
        issue.append("The Password Must Have @ in it")
    return issue

print("\n\nWelcome in Password Checker!\n")

while True:
    password = input("Enter Your Password: ")
    issues = check_password(password)
    if len(issues) == 0:
        print("Your Password Level Is Strong")
        break
    for issue in issues:
        print(issue)
    if len(issues) == 1:
        print("Your Password Level Is Medium")
    elif len(issues) == 2:
        print("Your Password Level Is Weak")
    else:
        print("Your Password Level Is Very Weak")