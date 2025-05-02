print("Hello from lesson 13")
# import random
# num1 = random.randint(1,10)
# num2 = random.randint(1,10)
# question = "what is " + str(num1) + "+" + str(num2) + "?"
# answer = input(question)
# answer = int(answer)
# hidden_answer = num1 + num2
# if answer == hidden_answer:
#     break

import random
counter = 0
score = 0
while True:
    counter = counter + 1
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    operator = random.randint(1,3)
    if operator == 1:
         question = "What is " + str(num1) + " + " +str(num2) + "?"
         hidden_answer = num1 + num2
    elif operator == 2:
        question = "What is " + str(num1) + " - " +str(num2) + "?"
        hidden_answer = num1 - num2
    else:
        question = "What is " + str(num1) + " x " +str(num2) + "?"
        hidden_answer = num1 *18
        num2
    answer = input(question)
    answer = int(answer)
    if answer == hidden_answer:
        score = score + 1
    if counter == 10:
        break
print("yur score is" + str(score))

balance = 1000
while True:
    print("Welcome to my bank")
    print("1. withdraw")
    print("2.deposit")
    print("3.check balance")
    print("4.exit")
    answer = input("What is ur choice? ")
    if answer == 4:
        print("thank u for using my bank")
        break
    elif answer == 3:
        print("your balance is $")
    elif answer ==2:
        amount = input("How much to deposit?")
        amount = int(amount)
        balance = int(amount)
        break
    elif answer== "1":
        amount = input("how much to withdraw?")
        amount = int(amount)
        if amount <=balance:
            balance = balance - amount
            print("successful, ur cash is dispensed")
        else:
            print("you have insufficient balance to make that withdraw go home brokie!")
    else:
        print("invalid choice")