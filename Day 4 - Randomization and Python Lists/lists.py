import string
import random

fruits ={"apple", "banana", "cherry"}
print(fruits)

str_inp = input("Enter your names: ")
names = str_inp.split(", ")
personas = len(names)

rng = random.randint(0, personas-1)

print("The winner is: " + names[rng])