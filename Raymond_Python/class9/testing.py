# This will be where we do our testing
# TOPIC: The `random` library
import random

print("Welcome to the math quiz!")
print("Solve the math problem to win!")

while True:

    # 1. Generate a random math problem
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # 2. Show the user math problem
    print(f"What is {num1} + {num2}?")

    # 3. Determine whtether the user got the answer right or wrong
    # 4. Tell them the above information
    answer = num1 + num2


    user_answer = int(input())

    if user_answer == answer:
        print("You got it right!")
    else:
        print("You got it wrong!")