import random

print("Welcome to the Math Quiz!")
print("Solve the math problem or type 'quit' to exit.")

while True:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    answer = input(f"What is {num1} + {num2}? ")
    
    # OPTIONAL
    if answer.lower() == "quit":
        print("Thanks for playing!")
        break
    
    # OPTIONAL
    if not answer.isdigit():
        print("Please enter a number!")
        continue
    
    if int(answer) == num1 + num2:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer was {num1 + num2}.")
