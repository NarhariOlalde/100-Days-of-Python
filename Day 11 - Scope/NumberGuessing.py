import os
import random

def Procedure(key, chances):
    chances_remaining = chances
    while chances_remaining > 0:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess > key:
            chances_remaining -= 1
            print(f"Too high, you have {chances_remaining} chances remaining")
        elif guess < key:
            chances_remaining -= 1
            print(f"Too low, you have {chances_remaining} chances remaining")
        elif guess == key:
            print("You got it!")
            return 0
        else:
            print(f"You lost. The number was {key}")

def game():
    playing = True
    print("Welcome to the Number Guessing Game")
    while playing == True:
        choice = input("Do you want to play? (y/n) ")
        if choice == "y":
            dificulty_selector = True
            os.system("cls")
            while dificulty_selector == True:
                dificulty = input("Please choose a dificulty level: easy, medium, hard: ")
                key = random.randint(1, 100)
                if dificulty == "easy":
                    Procedure(key, 10)
                    dificulty_selector = False
                elif dificulty == "medium":
                    Procedure(key, 7)
                    dificulty_selector = False
                elif dificulty == "hard":
                    Procedure(key, 5)
                    dificulty_selector = False
                else:
                    print("Invalid dificulty level")
        elif choice == "n":
            print("Goodbye")
            playing = False
        else:
            print("Invalid input")

game()