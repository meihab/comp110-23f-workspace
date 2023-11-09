"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730711612"

user_word: str = input("Enter a 5-character word: ")
if len(user_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

user_character: str = input("Enter a single character: ")
if len(user_character) != 1:
    print("Error: Character must be a single character.")
    exit()

character_counter: int = 0 

print("Searching for " + user_character + " in " + user_word)

for i in range(len(user_word)):
    if user_word[i] == user_character:
        print(user_character + " found at index " + str(i))
        character_counter += 1

if character_counter == 0:
    print("No instances of " + user_character + " found in " + user_word)
elif character_counter == 1:
    print("1 instance of " + user_character + " found in " + user_word)
else:
    print(str(character_counter) + " instances of " + user_character + " found in " + user_word)