# Level 1 — Beginner Projects (Start here)
# These will teach logic, file handling, and real usage.
# 1. Password Generator
# Learn:
# random
# strings
# functions
# Example:
# Enter length: 12
# Password: A8k$2Lp9!xQz


import random
passwordlength = int(input("Enter the length of password you would like to generate"))
passowrdelements='''abcdefghijklmnopqrstuvwxyz1234567890,./;':"*&^%$#@!'''
while((len(passowrdelements))==passwordlength or (len(passowrdelements))>passwordlength):
    randompassword = random.sample(passowrdelements,passwordlength) # random sampling
    print(''.join(randompassword))#converts list into string
    break
else:
    print("Password length is too long")
