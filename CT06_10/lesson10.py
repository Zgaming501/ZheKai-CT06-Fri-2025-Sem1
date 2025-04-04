
age = int(input("How old are u?"))
if age == 0:
    print("Age cannot be negative how did u even come to this place")
elif 0 <age< 18:
    print("Not eligible to vote")
else:
    print("U are eligible to vote")