import random

def word_scramble():
    # List of words to choose from
    words = ["python", "school", "computer", "hangman", "adventure"]
    word = random.choice(words)
    
    # Scramble the word
    scrambled = list(word)
    random.shuffle(scrambled)
    scrambled_word = ''.join(scrambled)

    print("Unscramble the letters to form a word!")
    print("Scrambled word:", scrambled_word)
    
    attempts = 0
    while True:
        guess = input("Your guess: ").lower()
        attempts += 1
        
        if guess == word:
            print(f"Great job! You guessed it in {attempts} attempts.")
            break
        else:
            print("That's not it. Try again!")

word_scramble()
