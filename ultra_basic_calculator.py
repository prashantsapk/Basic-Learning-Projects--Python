# Basic Calculator

operation=input("Welcome !! You are using Prashant's Calculator \nWhat operation you would like to perform\n\nadd for to add two numbers\nmuniply for to muntiply two numbers\ndivision to divide two numbers\nsubtract for to subtract two numbers")
a=int(input("Enter first number"))
b=int(input("Enter second number"))
sum1 = lambda a,b: a+b
muntiply = lambda a,b: a*b 
subtract = lambda a,b: a-b
division= lambda a,b: a/b

if(operation=="add"):
    print(sum1(a,b))
elif(operation=="muntiply"):
    print(muntiply(a,b))
elif(operation=="subtract"):
    print(subtract(a,b))
elif(operation=="division"):
    print(division(a,b))
else:
    print("You are trying to perform invalid operations")



