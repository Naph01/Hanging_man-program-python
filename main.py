#This is the hanging man game. It is a simple text-based game where the player has to guess a word by suggesting letters within a certain number of guesses.

import random  
from wordlist import words  # The various words are in another file called wordlist.py

hangman_art = {
    0: ("     ",
        "     ",
        "     "),

    1: ("  o  ",
        "     ",
        "     "),

    2: ("  o  ",
        "  |  ",
        "     "),

    3: ("  o  ",
        " /|  ",
        "     "),

    4: ("  o  ",
        " /|\\ ",
        "     "),

    5: ("  o  ",
        " /|\\ ",
        " /   "),

    6: ("  o  ",
        " /|\\ ",
        " / \\  ")
}

#creating functions

def display_hangman(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_answer(answer):
    print(" ".join(answer))  # the answer is spaced in between 

def display_hint(hint):
    print(" ".join(hint)) # since the hint is a list, this line of code converts it into a string with spaces in between them

#creating the main function to make it easier for te code to be re-used

def main():
    answer = random.choice(words).lower()
    hint = ["_"] * len(answer)  #the hint will be the number of "_" present
    guessed_words = set()  # sets cannot be created normally like lists, they need to have the word set followed by ()
    wrong_guesses = 0
    is_running = True  # run the program only when is_running is True

    while is_running:
        display_hangman(wrong_guesses) #displays the hangman art 

        display_hint(hint) # displays the hint 

        guess = input("Enter your guess: ").lower()

        if guess in guessed_words:
            print("You have already guessed the letter....")
            continue

        guessed_words.add(guess)

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input....")
            continue


        if guess in answer:
            for i in range(len(answer)):
                if guess == answer[i]:
                    hint[i] = guess

        else:
            wrong_guesses += 1

        
        if "_" not in hint:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print("Congratulations..... you have guessed the correct word.....")
            is_running = False

        elif wrong_guesses >= len(hangman_art) - 1:
            display_hangman(wrong_guesses)
            display_answer(answer) 
            print("You lost ......")
            is_running = False

    print("Thank you for playing and have a nice day ......")
        
if __name__ == "__main__":
    main()