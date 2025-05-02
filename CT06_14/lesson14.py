print("Hello from lesson 15")
groceries = ["Apples", "Bread", "carrots", "Dates", "Eggs", "Flour", "grapes", "Honey"]
groceries[7] = "Herbs"
groceries.append("Ice")
groceries.append("water")
del(groceries[1])
print(groceries)

# zoo = ["flamingo", "bats"]
# zoo.append("elephant")
# zoo.append("tiger")
# zoo.inserts(1, "deer")
# print(zoo)
# print(zoo[3-1])
# for a in zoo:
#     print(a)
# zoo.pop()
# print(zoo)
# del(zoo[0])
# print(zoo)
for item in groceries:
    if item == " Apples":
        print(item + ": I need 5 of these")
    elif item == "Carrots":
        print(item + ": I need 3 of these")
    elif item == "Dates":
        print(item + ": I need five of these")
    elif item == "Grapes":
        print("Go get farm fresh ones")
    else:
        print("I need 10 of these")
start = 14
while start <= 168:
    print(start)
else:
    print("end of list")