print("welcome in the billing Calculator")
total_price = 0
while True:
    item_name = input("Enter The Item Name: ").capitalizw()
    if item_name == 'Exit':
        break
    try:
        item_price = float(input("Enter The Item Price: "))
        total_price += item_price
    except ValueError:
        print("Enter A valid Number!")
        continue
print('The Final Price is', total_price, '+ 15%:', total_price * 1.15)