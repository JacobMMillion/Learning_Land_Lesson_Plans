# Guessing game
secret_number = 7
guess = 0

print("I'm thinking of a number between 1 and 10. Can you guess it?")

while guess != secret_number:
    guess = int(input("Your guess: "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("You guessed it! The number was", secret_number)