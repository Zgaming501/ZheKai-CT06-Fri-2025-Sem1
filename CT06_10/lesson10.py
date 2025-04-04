print("Hello from lesson 10")
num = int(input("What number do you want"))
remainder = num % 2
if remainder == 0:
    print("It is an even number")
else: 
    print("It is an odd number")
age = int(input("How old are u?"))
if age == 0:
    print("Age cannot be negative how did u even come to this place")
elif 0 <age< 18:
    print("Not eligible to vote")
else:
    print("U are eligible to vote")