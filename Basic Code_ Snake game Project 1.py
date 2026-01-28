# PROJECT 1: SNAKE, WATER, GUN GAME 
# We all have played snake, water gun game in our childhood. If you haven’t, google the 
# rules of this game and write a python program capable of playing this game with the 
# # user.
# Water
# Gun
# Snake
# Rules:
# Snake drinks Water → Snake wins
# Gun shoots Snake → Gun wins
# Water damages Gun → Water wins
# So:
# Water vs Gun → Water wins
# Gun vs Snake → Gun wins
# Snake vs Water → Snake wins
import random
entitiyused =["Snake","Water","Gun"]
Computer = random.choice(entitiyused)
i=0
b=0
while(i==0):
    a = input("Enter your Gun or water snake ")
    if((a=="Snake" and Computer =="Water")):
        print("Computer selected Water, Snake eats water, You won")
        b+=1
    elif(a=="Gun" and Computer =="Snake"):
        print("Computer selected snake, You won as gun kills snake")
        b+=1
    elif(a=="Water" and Computer =="Gun"):
        print("Computer selected gun, You won as Water Damages gun")
        b+=1
    else:
        print("You lose, Computer won")
        print(f"Your total score is {b}")
        break
