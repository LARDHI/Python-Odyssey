def check_password(pw):
    issue = []
    if " " in pw:
        issue.append("The Password Must not Have Spaces")
    if len(pw) <= 8:
        issue.append("The Password Must be 8 character at Least")
    if '@' not in pw:
        issue.append("The Password Must Have @ in it")
    return issue
print("\n\nWelcome in Password Checker!\n")
while True:
    password = input("Enter Your Password: ")
    issues = check_password(password)
    for issue in issues:
        print(issue)
    if len(issues) == 0:
        print("Well Done!")
        break
print(f'Your Password: {password} is Strong and Passed!')