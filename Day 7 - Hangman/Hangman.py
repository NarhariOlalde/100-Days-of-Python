import random
word_list = ["python", "java", "kotlin", "javascript"]
contador = 0
switch = True
chosen_word = random.choice(word_list)

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

letter_inventory = []
lives = 6

print("H A N G M A N")
contador = len(display)

while switch == True:
    guess = input("Guess the letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            if guess in letter_inventory:
                print("You already typed this letter")
                break
            else:
                letter_inventory.append(guess)
            display[position] = letter
            print("You guessed the right letter!")
        if not "_" in display:
            print("You guessed the word!")
            switch = False
            break
    if guess not in chosen_word:
        lives -= 1
        print("No such letter in the word")
        print("You have " + str(lives) +  " lives left")
        if lives == 0:
            print("You are hanged!")
            switch = False
            break
    print(f"{' '.join(display)}")
