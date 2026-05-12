sentence = input("Enter sentence: ").upper()
letter = input("Enter letter: ").upper()
count = 0
for l in sentence:
    if l == " ":
        continue
    if l == letter:
        count += 1
print("The Letter", letter, "appears", count)
print("Author: Amer Lardhi")