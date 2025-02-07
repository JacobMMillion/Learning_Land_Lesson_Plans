"""
Problem Statement:
You are given two integers. Write a program that calculates and prints their sum.

Output Format:
Print a single integer representing the sum of the two numbers.
"""

# solution function
def solution(a, b):

    answer = a + b
    return answer

# end solution function
# --------------------------------

# MAIN
a = input() # "1000"
b = input() # "500"

a = int(a) # 1000
b = int(b) # 500

ans = solution(a,b)
print(ans)