from ast import main


def greet(name, location):
    print(f"Hello {name}, from {location}")
    print("What do you want to do?")

def get_name():
    name = input("What's your name? ")
    location = input("Where do you live? ")
    greet(name, location)

get_name()
