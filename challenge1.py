sentence = input("Enter sentence: ").upper()
letter = input("Enter letter: ").upper()
count = 0
most_char = None
most_count = 0
z = []
for l in sentence:
    if l == " ":
        continue
    if l == letter:
        count += 1
    z.append(l)
    if z.count(l) > most_count:
        most_count = z.count(l)
        most_char = l
print("The Letter", letter, "appears", count)
print("The Most Counted Character is", most_char, 'Counted', most_count, 'Times.')
print("Author: Amer Lardhi")