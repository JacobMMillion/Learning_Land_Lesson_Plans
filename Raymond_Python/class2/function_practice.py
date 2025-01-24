import time

# player info
player = "Will"  # string (text)
health = 100  # integer (number)
isAlive = True  # boolean (T/F)

# take_damage function
def take_damage(damage_value):
    global health  # Declare health as global to modify the global variable
    global isAlive # Declare global

    health = health - damage_value # modify the health value

    # check if player is dead
    if health <= 0:
        isAlive = False

"""
Loop

Context: Player is in a pool of lava
"""

# game loop
print("Inital health: ", health)
while isAlive == True:

    # player is in lava, so take damage
    take_damage(10)

    print("------")
    print("Player health: ", health)  # Print initial health
    print("Player is alive? ", isAlive) # Print whether player is alive
    print("------")

    time.sleep(1) # pauses for a second

print("Loop exits, game over, player has died!")

"""
Non-loop logic
"""
# # stuff happens
# print("Player health: ", health)  # Print initial health
# print("Player is alive? ", isAlive) # Print whether player is alive
# print("------")

# take_damage(20)  # Call the function to reduce health

# print("Player health: ", health)  # Print initial health
# print("Player is alive? ", isAlive) # Print whether player is alive
# print("------")

# take_damage(80)

# print("Player health: ", health)  # Print initial health
# print("Player is alive? ", isAlive) # Print whether player is alive
# print("------")