
print("This is as test Phone Shop")
phone_man = input("Chose your phone manufacturer: iPhone or Pixel \n")
order = 0
if phone_man == "iPhone":
    choice1 = input("Choose iPhone model: 13, 13mini or 13Pro \n")
    if choice1 == "13mini":
        order += 600
        print(f"Your choice is {phone_man}{choice1} and price is ${order}")
    elif choice1 == "13":
        order += 650
        print(f"Your choice is {phone_man}{choice1} and price is ${order}")
    elif choice1 == "13Pro":
        order += 750
        print(f"Your choice is {phone_man}{choice1} and price is ${order}")
else:
    choice3 = input("Choose Google Pixel mode: 5, 6 or 6Pro \n")
    if choice3 == "5":
        order += 500
        print(f"Your choice is {phone_man}{choice3} and price is ${order}")
    elif choice3 == "6":
        order += 600
        print(f"Your choice is {phone_man}{choice3} and price is ${order}")
    elif choice3 == "6Pro":
        order += 700
        print(f"Your choice is {phone_man}{choice3} and price is ${order}")




 
