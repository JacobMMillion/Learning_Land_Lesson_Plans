import random

def choose_word(word_list):
    return random.choices(word_list)[0]

def display_word(word, guessed_letters):
    """
    Step 2: Returns a string showing the current state of the word.
    Letters that have been guessed are shown; others are displayed as underscores.
    """
    # 2.1: Initialize an empty string to build the display.
    # 2.2: Loop through each letter in the word.
    # 2.3: If the letter is in guessed_letters, add the letter and a space.
    # 2.4: Otherwise, add an underscore and a space.
    # 2.5: Return the final string (trim extra spaces if needed).
    pass

def get_guess(guessed_letters):
    """
    Step 3: Prompts the player to enter a letter.
    Checks that the input is a single alphabet character and hasn't been guessed before.
    """
    # 3.1: Prompt the user for a guess using input().
    # 3.2: Check that the input is exactly one letter.
    # 3.3: Verify that the letter is alphabetical.
    # 3.4: Ensure that the letter has not been guessed already.
    # 3.5: If invalid, prompt again until a valid guess is entered.
    # 3.6: Return the valid guess.
    pass

def play_hangman():
    """Step 4: Runs the Hangman game."""
    # 4.1: Create a list of possible words.
    word_list = ["apple","banana","melon","kiwi","tomato","berry","grape","coconut"]
    
    # 4.2: Choose a random word using choose_word().
    word = choose_word(word_list)
    print(f"The word for this game is: {word}") #DEBUG

    # 4.3: Initialize guessed_letters as an empty set.
    # 4.4: Initialize incorrect_guesses to 0.
    # 4.5: Set max_incorrect (e.g., 6) for the allowed number of wrong guesses.
    
    print("Welcome to Hangman!")
    print("Try to guess the word, one letter at a time.")
    
    # 4.6: Begin the game loop (while incorrect_guesses < max_incorrect).
    # 4.7: Display the current state of the word using display_word().
    # 4.8: Display the number of incorrect guesses remaining.
    # 4.9: Get a guess from the player using get_guess().
    # 4.10: Add the guessed letter to guessed_letters.
    # 4.11: Check if the guessed letter is in the word:
    #       - If yes: Print a "Good guess!" message.
    #         - Check if all letters in the word are guessed; if so, congratulate and exit.
    #       - If no: Print a "Sorry, wrong guess." message and increment incorrect_guesses.
    # 4.12: End the loop when the word is fully guessed or max_incorrect is reached.
    # 4.13: If the word was not guessed correctly, print a "Game over" message along with the word.
    pass

def main():
    """Step 5: Start the game by calling play_hangman()."""
    play_hangman()

if __name__ == '__main__':
    main() 