
age = int(input("How old are u?"))
if age == 0:
    print("Age cannot be negative how did u even come to this place?")
elif age>17:
    print("U can vote eligible")
else:
    print("U are not of eligible age to vote yet Womp Womp")
px = int(input("What price do you want"))
if px <=5:
    print("Sounds good")
elif px <=50:
    print("Are u sure if u need this item?")
elif px <=500:
    print("Where does ur money come from")
elif px >=500:
    print("do you u really need this? If u are so rich, gimmie money$$")

divide = int(input("What number do you want"))
if (divide %3==0) and (divide %7==0):
    print("The nmuber id divisible by 3 and 7")
else:
    print("It is not divisible by 3 and 7")
rider1 = 25
rider2 = 6
if rider1 >= 18 or rider2 >= 18:
    print("you can ride")
else:
    print("need one adult or age > 18 Womp Womp")
age =int(input("How old are u?"))
if age <= 12 or age >= 65:
    print("Ticket price $15 ur a child so u got discount")
else:
    print("Ticket price is $20 so pay up")
