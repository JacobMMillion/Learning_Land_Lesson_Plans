def intro():
    """Introduction to the adventure and first decision point."""
    print("Welcome to the Text Adventure Game!")
    print("You wake up in a mysterious cave with two paths ahead.")
    print("One path leads deeper into the cave, and the other appears to lead outside.")
    return choose_path()

def choose_path():
    """Prompts the player to choose a path and directs them accordingly."""
    while True:
        choice = input("Do you want to go 'left' (deeper into the cave) or 'right' (toward the exit)? ").lower()
        if choice == 'left':
            return treasure_room()
        elif choice == 'right':
            return dragon_room()
        else:
            print("Invalid choice. Please type 'left' or 'right'.")

def treasure_room():
    """Scene where the player discovers treasure."""
    print("\nYou head left and enter a glittering treasure room.")
    print("There is a shiny sword and a pile of gold on a pedestal.")
    while True:
        choice = input("Do you take the 'sword' or the 'gold'? ").lower()
        if choice == 'sword':
            print("\nYou take the sword. As you lift it, a secret door opens revealing an exit!")
            print("You escape the cave as a brave adventurer. You win!")
            break
        elif choice == 'gold':
            print("\nYou are dazzled by the gold and spend too much time admiring it.")
            print("While you are distracted, the room starts to collapse!")
            print("You barely escape, but without any treasure. Game over!")
            break
        else:
            print("Invalid choice. Please type 'sword' or 'gold'.")

def dragon_room():
    """Scene where the player encounters a sleeping dragon."""
    print("\nYou head right and walk into a dark chamber.")
    print("There, lying across the path, is a massive, sleeping dragon!")
    while True:
        choice = input("Do you try to 'sneak' past the dragon or 'run' back? ").lower()
        if choice == 'sneak':
            print("\nYou carefully tiptoe past the dragon and discover a hidden exit behind it!")
            print("Quiet and brave, you slip out of the cave. You win!")
            break
        elif choice == 'run':
            print("\nYou decide to run back, but in your haste, you trip and wake the dragon!")
            print("The dragon chases you down the cave. Game over!")
            break
        else:
            print("Invalid choice. Please type 'sneak' or 'run'.")

def main():
    """Starts the adventure game."""
    intro()

if __name__ == '__main__':
    main()

