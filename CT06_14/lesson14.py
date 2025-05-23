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
#  
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

found = false
catalogue = ["IPhone", "IPad", "Nintendo Switch", "Durians"]
answer = input("What are u looking for?")
for item in catalogue:
    print("Yes, we do sell them and is costs $1000")
    found = True
    break

if not found:
    print("No, we don't sell that get out!!!!")

import turtle

window = turtle.Screen()
window.setup(width=400, height=400)

daisy = turtle.Turtle()
daisy.goto(0,0)
daisy.up()

while daisy.xcor() < 198:
  daisy.forward(1)
   
daisy.down()
daisy.seth(90)

while daisy.ycor() < 198:
  daisy.forward(1)
  
daisy.seth(180)

while daisy.xcor() > -198:
  daisy.forward(1)
  
daisy.seth(270)
while daisy.ycor() > -198:
   daisy.forward(1)
   
daisy.seth(0)
while daisy.xcor() < 198:
  daisy.forward(1)
  
daisy.seth(90)
while daisy.ycor() < 0:
  daisy.forward(1)










    