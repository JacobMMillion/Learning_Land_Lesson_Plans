import random

def get_computer_choice():
    """Randomly selects and returns the computer's choice."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    """Prompts the user for a valid choice and returns it."""
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice. Please try again.")

def determine_winner(user_choice, computer_choice):
    """
    Determines the winner based on traditional rules:
    Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.
    Returns a string indicating the outcome.
    """
    if user_choice == computer_choice:
        return "tie"
    elif ((user_choice == 'rock' and computer_choice == 'scissors') or 
          (user_choice == 'paper' and computer_choice == 'rock') or 
          (user_choice == 'scissors' and computer_choice == 'paper')):
        return "user"
    else:
        return "computer"

def play_round():
    """Plays a single round of Rock, Paper, Scissors."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
    else:
        print("Computer wins!")
    return result

def main():
    """Main game loop for Rock, Paper, Scissors."""
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        play_round()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == '__main__':
    main()

