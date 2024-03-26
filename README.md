# Hangman-game
This is a hangman game on python terminal
This Python code implements a simple Hangman game. Here's a breakdown of what each part does:

import random: This imports the random module, which is used to generate random choices.

from hangman_art import logo: This imports a ASCII art representation of the Hangman logo from a module named hangman_art.

from hangman_words import word_list: This imports a list of words that can be used for the game from a module named hangman_words.

from hangman_art import stages: This imports a list of ASCII art representing the different stages of the hangman game (i.e., the hangman drawings as the player makes incorrect guesses).

print(logo): This prints out the Hangman logo when the game starts.

chosen_word = random.choice(word_list): This randomly selects a word from the word_list to be the word the player needs to guess.

length = len(chosen_word): This calculates the length of the chosen word.

lives = 6: This initializes the number of lives the player has. In this game, the player starts with 6 lives.

end_of_game = False: This flag is used to control when the game ends.

display = []: This initializes an empty list called display, which will be used to show the progression of correct guesses.

for _ in range(length): display += "_": This loop populates the display list with underscores representing each letter of the chosen word.

while not end_of_game:: This starts a loop that continues until end_of_game is set to True.

guess = input("Guess a letter :").lower(): This prompts the player to input a letter guess. .lower() is used to convert the input to lowercase for consistency.

for position in range(length):: This loop iterates through each position in the chosen word.

letter = chosen_word[position]: This retrieves the letter in the chosen word at the current position.

if letter == guess: display[position] = letter: If the guessed letter matches the letter in the chosen word at the current position, it updates the display accordingly.

if guess not in chosen_word:: If the guessed letter is not in the chosen word, the player loses a life.

if "_" not in display:: If there are no more underscores in the display, it means the player has guessed all the letters correctly and wins the game.

print(stages[lives]): This prints the current hangman stage corresponding to the number of lives left.

The game continues looping until either the player wins or loses, at which point a message is printed indicating the outcome.






