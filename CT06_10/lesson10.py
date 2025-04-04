
age = int(input("How old are u?"))
if age == 0:
    print("Age cannot be negative how did u even come to this place?")
elif age>17:
    print("U can vote eligible")
else:
    print("U are not of eligible age to vote yet Womp Womp")
px = int(input("What price do you want"))
if px < 5:
    print("Sounds good")
elif px <=50:
    print("Are u sure if u need this item?")
elif px <=500:
    print("Where does ur money come from")
elif px >=500:
    print("do you u really need this? If u are so rich, gimmie money$$")