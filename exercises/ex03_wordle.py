"""EX03 - Wordle with functions - The next step!"""

__author__ = "730711612"


def contains_char(word: str, letter: str) -> bool:
    """Searches for an occurence of letter in word."""
    assert len(letter) == 1

    counter: int = 0

    while counter < len(word):
        if letter == word[counter]:
            return True
        counter += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns a string of white, green and yellow boxes depending on how guess matches secret."""
    assert len(guess) == len(secret)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    
    counter: int = 0

    emoji_str: str = ""

    while counter < len(guess):
        if contains_char(secret, guess[counter]) is False:
            emoji_str = emoji_str + WHITE_BOX
        elif contains_char(secret, guess[counter]) and guess[counter] == secret[counter]:
            emoji_str = emoji_str + GREEN_BOX
        else: 
            emoji_str = emoji_str + YELLOW_BOX
        
        counter += 1
   
    return emoji_str


def input_guess(expected_length: int) -> str:
    """Makes sure the inputted word is of the correct length."""
    guess: str = input(f"Enter a {expected_length} character word: ")

    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    word: str = "codes"
    turns: int = 1
    win: bool = False
    guess: str

    while turns <= 6 and not win:
        print(f"=== Turn {turns}/6 ===")

        guess = input_guess(len(word))

        print(emojified(guess, word))

        if guess == word:
            win = True
        else:
            turns += 1
    
    if guess == word:
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")
    

if __name__ == "__main__":
    main()