"""
The modulus operation allows us to take the remainder of a division!

"Like a remainder calculator"

eg. 5 % 4 = 1, because 4 divides 5 one time, with a remainder of 1
eg. 4 % 4 = 0, because 4 divides 4 one time, without a remainder
eg. 20 % 5 = 0, because 5 divides 20 four times, with no remainder

In game design, this might be used to scheduele events that occur every x seconds
for example:
"""

import time

# Initialize a counter to simulate ticks in a game loop
counter = 0

# Start of the game loop (simulation of frame updates)
while True:
    # Increase the counter on each loop iteration
    counter += 1

    # Check if the counter is a multiple of 10 (every 10th frame)
    if counter % 10 == 0:
        print("This could be an event that occurs every 10 frames. Maybe an enemy shoots at the player.")

    # Simulate a break in the loop to prevent it from running forever
    if counter >= 50:  # Let's stop after 50 iterations
        print("Game Over!")
        break

    # this can be ignored for now, it is so the loop does not run too quickly
    time.sleep(.1)

# """
# Here is another example, less related to games, but to better explain the operation itself
# Task:
# Write a function that accepts an integer to calculate the multiples of 4 or 6
# below the specified number and output the sum of those multiples

# Time complexity: O(n)
# Space complexity: O(1)
# """

# # get user input and cast it to an int
# n = int(input("Enter a number: "))

# sum_of_multiples = 0

# for i in range(n):

#     # if i is a multiple of 4 or 6, we add that number (i) to the sum
#     if i % 4 == 0 or i % 6 == 0:
#         print(i, "is a multiple of 4 or 6")
#         sum_of_multiples = sum_of_multiples + i

# print("Final sum of multiples:", sum_of_multiples)