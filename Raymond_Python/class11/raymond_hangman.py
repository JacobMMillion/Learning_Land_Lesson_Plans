import random

def choose_word(word_list):
    return random.choice(word_list)

def display_word(word, guessed_letters):
    """
    Step 2: Returns a string showing the current state of the word.
    Letters that have been guessed are shown; others are displayed as underscores.
    """
    # 2.1: Initialize an empty string to build the display.
    display = ""
    # 2.2: Loop through each letter in the word.
    # 2.3: If the letter is in guessed_letters, add the letter and a space.
    # 2.4: Otherwise, add an underscore and a space.
    for char in word:
        if char in guessed_letters:
            display += char
            display += " "
        else:
            display += "_"
            display += " "
    # 2.5: Return the final string (trim extra spaces if needed).
    return display
def get_guess():
    """
    Step 3: Prompts the player to enter a letter.
    Checks that the input is a single alphabet character and hasn't been guessed before.
    """
    # 3.1: Prompt the user for a guess using input().
    print("Guess a letter.")
    guess = input()
    # 3.2: Check that the input is exactly one letter.
    # 3.3: Verify that the letter is alphabetical.
    # 3.4: Ensure that the letter has not been guessed already.
    # 3.5: If invalid, prompt again until a valid guess is entered.
    # 3.6: Return the valid guess.
    return guess
    
    
def play_hangman():
    """Step 4: Runs the Hangman game."""
    # 4.1: Create a list of possible words.
    word_list = ["apple","banana","melon","kiwi","tomato","berry","grape","coconut"]
    
    # 4.2: Choose a random word using choose_word().
    word = choose_word(word_list)
    print(f"The word for this game is: {word}") #DEBUG

    # Greet the user
    print("Welcome to Hangman!")
    print("Try to guess the word, one letter at a time.")

    # 4.3: Initialize guessed_letters as an empty set.
    guessed_letters = set()
    # 4.4: Initialize incorrect_guesses to 0.
    incorrect_guesses = 0

    # 4.5: Set max_incorrect (e.g., 6) for the allowed number of wrong guesses.
    max_incorrect = 6

    # 4.6: Begin the game loop (while incorrect_guesses < max_incorrect).
    while incorrect_guesses <= max_incorrect:
        # 4.7: Display the current state of the word using display_word().
        print(display_word(word, guessed_letters))
        # 4.8: Display the number of incorrect guesses remaining.
        print("incorrect_guesses remaining ", incorrect_guesses)
        # 4.9: Get a guess from the player using get_guess().
        guess = get_guess()
        # 4.10: Add the guessed letter to guessed_letters.
        guessed_letters.add(guess)
        # 4.11: Check if the guessed letter is in the word:
        if guess in word:
            print("Good guess!")
            for i in range(len(word)):
                tempt = word[i]
                if tempt in guessed_letters:
                    if i == len(word) - 1:
                        print("You won!")
                        print("The word was ", word)
                        return
                else:
                    break
        else:
            print("Incorrect, try again.")
            incorrect_guesses = incorrect_guesses + 1
            
            
    print("Game over, the word was", word)
            
def main():
    """Step 5: Start the game by calling play_hangman()."""
    play_hangman()

if __name__ == '__main__':
    main()