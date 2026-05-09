sentence = input("Enter sentence: ")
letter = input("Enter letter: ")
count = 0
for l in sentence:
    if l == letter:
        count += 1
print("The Letter", letter, "appears", count)