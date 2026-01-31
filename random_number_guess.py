# ROJECT 2 – THE PERFECT GUESS 
# We are going to write a program that generates a random number and asks the user to 
# guess it. 
# If the player’s guess is higher than the actual number, the program displays “Lower 
# number please”. Similarly, if the lease” When the user guesses the correct number, the program duser’s guess is too low, the program prints “higher 
# number pisplays the 
# number of guesses the player used to arrive at the number. 
# Hint: Use the random module. 

import random
print("Now you have to do a random guess of numbber")
a= int(input("Enter the number you want\t"))
list = []
for i in range(1,101,1):
    list.append(i)

b = random.choice(list)

# we have to use loop here, so that it ask again and again someone wins
# the executed loop number can be said the guess the user took
i=1
while (a>b or b<a):
    i+=1
    if (a == b):
        print("You entered the correct number\t")
        break
    elif(a<b):
        print("Higher number please")
        a= int(input("Enter the number you want\t"))

    else:
        print("Lower number please")
        a= int(input("Enter the number you want\t"))

print(f"Number of guesses = {i}")

