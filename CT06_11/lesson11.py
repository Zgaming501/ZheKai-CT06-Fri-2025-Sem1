print("Hello from lesson 11")
score = int(input("What score did you get? I am curious?"))
if 89<score<101:
    print("AL1")
elif 79 <score< 90:
    print("AL2")
elif 69 <score< 80:
    print("AL3")
elif 59 <score< 70:
    print("AL4")
else:
    print("AL5-AL6,AL7,AL8, try harder next time study more")

colour = int(input("What colour do you like?"))

if not (colour=="Green"):
    print("You are wrong, you must choose green")
else:
    print("You are absolutely correct. Good choice")
day = int(input("What day of the week is it?"))
if not (day == "Saturday"):
    print("It is not the weekends!!")
else:
    print("It's the weekend! No school!")
print("Welcome to McDonalds")
burger = int(input("Do you want a burger?"))
drinks = int(input("What drink do you want?"))
fries = int(input("Do u want fries?"))
if burger == "yes" and fries == "yes"and not drinks == "yes":
    print("Won't you get thirsty?")
else:
    print("Good choice of food and drinks, your order is sent to the kitchen")
    