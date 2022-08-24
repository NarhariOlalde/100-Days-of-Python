programming_dictionariy = {
"Bug": "A software error.",
"Feature": "A new feature of a software.",
"Enhancement": "A new feature of a software.",
}

#print Dictionary
print(programming_dictionariy["Bug"])

#Add a new key-value pair to the dictionary.
programming_dictionariy["Loop"] = "The action of repeating a sequence of instructions until a condition is met."

print(programming_dictionariy["Loop"])

#Edit an existing key-value pair in the dictionary.
programming_dictionariy["Loop"] = "The action of repeating a sequence."
print(programming_dictionariy["Loop"])

#Loop through the dictionary and print all the key-value pairs.
for key, value in programming_dictionariy.items():
    print(key, value)

for key in programming_dictionariy.keys():
    print(key)
    print(programming_dictionariy[key])

#Wipe out the dictionary.
programming_dictionariy.clear()
programming_dictionariy = {}
print(programming_dictionariy)