print("\n\nWelcome in The Guessing Game!\n")
number = 74
count = 0
while True:
    count += 1
    guess = int(input("Try Guessing The Number(1~100): "))
    if guess == number:
        print(guess, "Is Correct!")
        print("You Take", count, "Guess To Do It")
        break
    elif guess > number:
        print("The Number", guess, "is Bigger!")
        continue
    elif number > guess:
        print("The Number", guess, " is Smaller!")
        continue
