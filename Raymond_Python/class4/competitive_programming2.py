"""
One hot summer day Pete and his friend Billy decided to buy a watermelon. 
After that the watermelon was weighed, and the scales showed w pounds. 
They rushed home, dying of thirst, and decided to divide the fruit,
however they faced a hard problem.

Pete and Billy are great fans of even numbers, 
that's why they want to divide the watermelon in such a way that each of the two parts weighs even number of pounds, 
at the same time it is not obligatory that the parts are equal. 
The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, 
if they can divide the watermelon in the way they want. For sure, each of them should get a part of positive weight.
"""

# variable w: the weight of the watermelon
# the boys both like even numbers
def solution(w):

    # input: w: the weight of the watermelon
    # output: "YES" or "NO" depending on whether the melon can be split into two even numbers

    # what is this problem asking?
    # given a watermelon, can we divide it into two parts, where each part is an even number?
    # 8 --> 2,6 4,4

    # CRITICAL INSIGHT: if w is even, we can always divide it into two equal parts
    # if odd, we can never divide it into two equal parts.

    if w % 2 == 0 and w > 2:
        return "YES"
    else:
        return "NO"


# end of solution function


# MAIN

# getting the weight of the watermelon from the user
w = input()
w = int(w)
print("The watermelon weighs:", w, "pounds")

# call our solution function to get the solution
answer = solution(w)

# print the answer
print(answer)