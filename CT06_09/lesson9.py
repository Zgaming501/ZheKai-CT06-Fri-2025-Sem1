print("Hello from lesson 9")
numApples = int(input("How many apples? "))
numOranges = int(input("How many oranges? "))

if numApples > 5:
    apple = 0.6 * numApples * 0.9
else:
    apples = 0.6 * numApples

if numOranges > 5:
    orange = 0.9 * numOranges * 0.9
else:
    oranges = 0.9 * numOranges

total = apples + oranges 
print("Please pay me $" + str(total))

positive_days = 0
for count in range(7):
    temp = int(input("What is the temperature for today? "))
    if temp > 30:
        posititve_days = positive_days + 1

print(str(positive_days) + "days are hotter tha 30 deg outside")
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