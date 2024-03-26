import random
from hangman_art import logo
from hangman_words import word_list
from hangman_art import stages

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)
length = len(chosen_word)

lives = 6
end_of_game = False
display = []
for _ in range(length):
    display += "_"
print(display)

while not end_of_game:
    guess = input("Guess a letter :").lower()

    for position in range(length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose !")
    if "_" not in display:
        end_of_game = True
        print("You won !")
    print(stages[lives])

    

# org_word = random.choice(word_list)
# print(org_word)

# temp_word = []
# lives = 7
# empty = False
# draw = -1

# for _ in range(0, len(org_word)):
#     temp_word.append("_")
# print(temp_word)

# while lives > 0 or empty == True:
#     guess = input("Guess a letter :").lower()
#     if guess in org_word:
#         print("You guessed a letter correctly")
#         for i in range(0, len(org_word)):
#             if guess == org_word[i]:
#                 temp_word[i] = guess
#         print(temp_word)
#     else:
#         print(stages[draw])
#         print(temp_word)
#         draw -= 1
#         lives -= 1
#     if "_" in temp_word:
#         empty = True
#     else:
#         print("You won !")
#         break
#     if lives == 0:
#         print("You ran over lives ! You lose !")
#         break



# word = "butterfly"
# if "t" in word:
#     print("yes")
