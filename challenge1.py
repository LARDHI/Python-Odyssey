def is_file(sentence):
    try:
        file_content = open(sentence)
        return file_content.read().upper()
    except:
        return sentence
sentence = input("Enter File Name or Sentence: ")
content = is_file(sentence)
letter = input("Enter letter: ").upper()
count = 0
most_char = None
most_count = 0
seen_letter = []
for l in content:
    if l == " ":
        continue
    if l == letter:
        count += 1
    seen_letter.append(l)
    if seen_letter.count(l) > most_count:
        most_count = seen_letter.count(l)
        most_char = l
print("The Letter", letter, "appears", count)
print("The Most Counted Character is", most_char, 'Counted', most_count, 'Times.')
print("Author: Amer Lardhi")