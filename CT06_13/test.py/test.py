#task 1
# use the while loop to print numbers 10 to 200
# print in multiples of ten
# number 10 first and 200 last
#for counter in range(9,201):
    #print(int(counter))
#task 2
#password checker to protect superpass123
# ask user for password
# password dorrect = access granted
# password incorrect = access denied
#password = int(input("What is the password?"))
#if password == "superpassword123":
    #print("Access denied")
#else:
    #print("Access granted")

# queston 2
# Print the third item mars
# append neptune
# rename mars to muskworld
# remove uranus 
# use for to print planets one by one
planets = ["mecury", "venus", "earth", "mars", "jupiter","saturn","urnaus"]
planets[3] = "mars"
planets.append("neptune")
del(planets[3])
planets[3] = ("muskworld")
del(planets[6])
print(planets)

