"""EX02 - One shot wordle - My first python game!"""

__author__ = "730711612"

secret_word = "python"

guess_word = input(f"What is your {len(secret_word)}-letter guess? ")

attempt_counter: int = 0
max_tries: int = 6

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# checks if the entered number of letters matches the number of letters in secret
while (len(guess_word) != len(secret_word)) and (attempt_counter < max_tries):
    guess_word = input(f"That was not {len(secret_word)} letters! Try again: ")
    attempt_counter += 1

word_index: int = 0
resulting_string: str = ""

if len(guess_word) != len(secret_word):
    print("Not quite. Play again soon!")  # game ends if the number of letters doesn't match
else:
    while word_index < len(secret_word):
        # iterates over all charcters in the guessed word
        guessed_character_in_word: bool = False
        if guess_word[word_index] == secret_word[word_index]:
            resulting_string = resulting_string + GREEN_BOX
        else:
            secondary_index: int = 0
            while (guessed_character_in_word is False) and (secondary_index < len(secret_word)):
                # checks if the character can be found elsewhere in the word
                if guess_word[word_index] == secret_word[secondary_index]:
                    guessed_character_in_word = True

                secondary_index += 1

            if guessed_character_in_word is True:
                resulting_string = resulting_string + YELLOW_BOX 
            elif guessed_character_in_word is False:
                resulting_string = resulting_string + WHITE_BOX 

        word_index += True

    print(resulting_string)  # contains all the colored boxes

    if guess_word == secret_word:
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!")