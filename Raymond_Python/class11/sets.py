# SETS
# change some things, and have type in chat the exact output in console 

# Let's create two sets. Sets don't allow duplicates!
fruits = {"apple", "banana", "orange", "apple"}  # Notice 'apple' appears twice
veggies = {"carrot", "lettuce", "broccoli", "banana"}

# Let's print the sets
print("Fruits:", fruits)
print("Veggies:", veggies)

# Adding something new to a set
fruits.add("grape")
print("Fruits after adding grape:", fruits)

# Removing an item from a set
veggies.remove("lettuce")
print("Veggies after removing lettuce:", veggies)

# Checking if something is in a set
if "apple" in fruits:
    print("Apple is in the fruits set!")

# Finding items in both sets (Intersection)
common_items = fruits.intersection(veggies)
print("Items common to both fruits and veggies:", common_items)

# Combining both sets together (Union)
all_items = fruits.union(veggies)
print("All unique items:", all_items)

# Finding items only in fruits (Difference)
only_fruits = fruits.difference(veggies)
print("Items only in fruits:", only_fruits)