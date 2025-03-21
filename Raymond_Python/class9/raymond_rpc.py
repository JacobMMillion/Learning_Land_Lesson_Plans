# This will be where we do our testing
# TOPIC: The `random` library
import random


# COMPUTER
def get_computer_choice():   
    choices = ["rock", "paper", "scissors"]
    return random.choices(choices)[0]
    
    
# PLAYER
def get_user_choice():
    print("Choose rock, paper, or scissors")
    user_choice = input()
    return user_choice
    
    
# DETERMINE THE WINNER
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
        print("The computer won")
# START TO THE GAME, don't change


play_round()