import random

def choose_word(word_list):
    """Selects a random word from the provided list."""
    return random.choice(word_list).lower()

def display_word(word, guessed_letters):
    """
    Returns a string showing the current state of the word.
    Letters that have been guessed are shown; others are displayed as underscores.
    """
    displayed = ''
    for letter in word:
        if letter in guessed_letters:
            displayed += letter + ' '
        else:
            displayed += '_ '
    return displayed.strip()

def get_guess(guessed_letters):
    """
    Prompts the player to enter a letter.
    Checks that the input is a single alphabet character and hasn't been guessed before.
    """
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        else:
            return guess

def play_hangman():
    """Runs the Hangman game."""
    # List of words to choose from
    word_list = ["python", "hangman", "programming", "code", "computer"]
    word = choose_word(word_list)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6  # Maximum number of incorrect guesses allowed

    print("Welcome to Hangman!")
    print("Try to guess the word, one letter at a time.")

    # Game loop
    while incorrect_guesses < max_incorrect:
        print("\nWord:", display_word(word, guessed_letters))
        print("Incorrect guesses left:", max_incorrect - incorrect_guesses)
        guess = get_guess(guessed_letters)
        
        guessed_letters.add(guess)
        if guess in word:
            print("Good guess!")
            # Check if all letters have been guessed
            if all(letter in guessed_letters for letter in word):
                print("\nCongratulations! You guessed the word:", word)
                return
        else:
            print("Sorry, wrong guess.")
            incorrect_guesses += 1

    print("\nGame over! The word was:", word)

def main():
    play_hangman()

if __name__ == '__main__':
    main()