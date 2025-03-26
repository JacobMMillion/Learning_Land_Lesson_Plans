# This will be where we do our testing
# TOPIC: The `random` library
import random

# TODO 4: Modify the print statements, so there is better spacing
# we want a clear user interface


# COMPUTER
# TODO 5 (the very last thing): explore lists! Transition to Hangman!
def get_computer_choice():   
    choices = ["rock", "paper", "scissors"]
    return random.choices(choices)[0]
    
    
# PLAYER
# TODO 3: let's slightly modify this so that we add more robust error checking
# TODO part 3.1: modify the code so that whether the user enters "Rock" and "rock", we treat it the same
# TODO part 3.2: modify the code so if they input aything random, we will detect this and reprompt them
def get_user_choice():
    print("Choose rock, paper, or scissors")
    user_choice = input()
    return user_choice
    
    
# DETERMINE THE WINNER
# TODO 1: determine if the computer won, or if the player run, in the case it is not a tie
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"


def play_round():
    # Get the user's choice:
    user_choice = get_user_choice()
    print(f"You chose {user_choice}")
    
    # Get the computer's choice, and display
    computer_choice = get_computer_choice()
    print(f"The computer chose {computer_choice}")

    # Determine the winner
    winner = determine_winner(user_choice, computer_choice)

    # Dinner display the winner to the user
    if winner == "tie":
        print("It's a tie!")
    if winner == "computer":
        print("The computer won!")
    if winner == "player":
        print("You won!")







"""
----------------------------------------------
This kicks off the play_round function, and starts a round.

TODO 2: Can we modify this so that we continuously call it while the user wants to play another round?
----------------------------------------------
"""
play_round()