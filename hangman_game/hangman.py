import random
from hangman_words import word_list
from hangman_art import stages, logo
from replit import clear

lives = 6
end_of_game = False
display = []

print(logo)

chosen_word = random.choice(word_list)

for x in range(len(chosen_word)):
    display.append("_")
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

    for current_guess in range(len(chosen_word)):
        if chosen_word[current_guess] == guess:
            display[current_guess] = guess
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that is not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lost.")
    print(display)
    print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You win.")
