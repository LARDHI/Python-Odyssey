names = []
name = ''
while True:
    name = input("Enter a Name To Add In The List: ").capitalize()
    if name == 'done'.capitalize():
        break
    if name in names:
        continue
    names.append(name)
print(names)