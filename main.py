import random
import hangman_art
import hangman_words
from replit import clear

#logo
print(hangman_art.logo)

#variables
lives = 6
guess_collector = []

#Word selector
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

#displays the number of letters required
display = []
for i in range (word_length):
    display.append("_")
print(display)


game_end = False
while not game_end:

    #user prompt for a letter
    guess = input("Enter a letter: ").lower()
    clear()
    if guess in guess_collector:
        print(f"you have already guessed {guess}")
    else:
    #iterates through the word to check if the letter is present
        j = 0
        for letter in chosen_word:
            if letter == guess:
                display[j] = guess
            j += 1
        
        guess_collector.append(guess)

    #checks to see if the letter was correct, else subtracts a life
        if guess not in chosen_word:
            lives -= 1  
            print(f"{guess} is not in the word")

        print(display)
        print(hangman_art.stages[lives])
        print('=================================')

        if not "_" in display:
            game_end= True
            print("You Win!")
        elif lives == 0:
            game_end= True
            print(f"You Lose! The word was {chosen_word}")




