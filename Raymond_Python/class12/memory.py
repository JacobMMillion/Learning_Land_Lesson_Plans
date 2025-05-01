import random
import time

colors = ["red", "blue", "green", "yellow"]
pattern = []

print("Memorize the pattern and repeat it!")

for level in range(1, 6):  # 5 rounds
    pattern.append(random.choice(colors))
    print("Pattern:")
    for color in pattern:
        print(color)
        time.sleep(2)
    print("\n" * 100)  # "Clear" the screen

    guess = input("Enter the pattern (space-separated): ").split()
    if guess != pattern:
        print("Wrong pattern! Game over.")
        break
    else:
        print("Good job!\n")

print("Game over. Thanks for playing!")
