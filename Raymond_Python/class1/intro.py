"""
1. Printing to the screen
   - we use the `print()` function to print to the screen
"""
# # Basic variable modification and printing to the screen
# health = 100 # int
# name = "Raymond" # string
# speed = 5

# print("The players name is:", name)
# print("The players health is:", health)
# print("The players speed is:", speed)
# print("---------------------")

# print("player took some damage, and it made them slow down!")
# health = health - 10
# speed = speed - 1

# print("The players name is:", name)
# print("The players health is:", health)
# print("The players speed is:", speed)
# print("---------------------")


"""
2. Variables and printing to the screen
   - variables store information! (like text or numbers, name or player health for example)
   - explain types of variables: bool, int, string (Python not type-def though)
"""
# # Storing text in a variable
# name = "Jacob"
# print("My name is", name)

# # Storing numbers in a variable
# age = 22
# print("I am", age, "years old")

# # Updating a variable
# age = age + 1
# print("Next year, I will be", age, "years old")


"""
3. Conditionals
   - conditionals allow different paths of execution depending on the value of variables
"""
# # Simple if-else example
# health = 100

# # take some damage
# health = health - 100

# if health <= 0:
#    print("Player has died!")
# else:
#    print("Player is not dead!")
#    print(health)


# # Checking multiple conditions
# score = 50

# if score >= 90:
#    print("You got an A!")
# elif score >= 80:
#    print("You got a B!")
# else:
#    print("You got a C or lower!")


# LEFT OFF HERE


"""
4. Loops
   - loops allow programs to repeat tasks
"""
# # FOR LOOP: Counting from 1 to 5
# # `for` loops allow us to repeat a specific number of times
# for i in range(1, 6):
#     print("Number:", i)

# # WHILE LOOP: Counting down from 5
# # `while` loops allow us to repeat a task as long as a condition is true
# health = 5
# while health >= 0:
#     print("Health:", health)

#     if health == 0:
#         print("Player has died! Health will now decrease to -1 and we will exit the `while` loop")

#     health -= 1  # Decrease health by 1


"""
5. Get User Input
   - we do this with the `input` function
"""
# # Ask for the user's name
# name = input("What is your name? ")
# print("Hi", name, "nice to meet you!")

# # Ask for a number and echo it
# number = int(input("Enter a number: "))
# print("Your number is", number)


# """
# 6. Functions
#    - functions allow us to make reusable blocks of code
# """
# # Define a function
# def greet(name):
#     print("Hello,", name)

# # Call the function
# greet("Alice")
# greet("Bob")


"""
7. Lists
   - lists store multiple values in one variable
"""
# # Create a list of favorite foods
# foods = ["Pizza", "Burger", "Ice Cream"]
# # Print all foods
# print("My favorite foods are:")
# for food in foods:
#     print(food)

# # Add a new food
# foods.append("Tacos")
# print("Now I also like:", foods[3])