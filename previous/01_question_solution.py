# Question 1: Write a program to find HCF of two numbers by without using recursion.
#
#
# Input format: The first line contains any 2 positive numbers separated by space.
# Output format: Print the HCF of given two numbers.
#
# Sample Input:
# 70 15
#
# Sample Output:
# 5

def find_hcf(a, b):  # a = 70, b = 15
    while b:
        a, b = b, a % b  # a = 15, b = 10 because 70 % 15 = 10
    return a


# the above function finds the HCF of two numbers by using Euclid's algorithm by using iteration.
# The iteration is done by using while loop. The while loop will run until b is not equal to 0. And when b is equal
# to 0, the loop will stop and the value of a will be returned. This value is the HCF of the two numbers because
# the last value of b is the remainder of the division of a and b. And the last value of a is the HCF of the two
# numbers.


input_numbers = input("Enter two positive numbers separated by space: ")
num1, num2 = map(int, input_numbers.split())

hcf = find_hcf(num1, num2)

print("HCF of", num1, "and", num2, "is:", hcf)

# import math
#
# # Input
# num1, num2 = map(int, input("Enter two positive numbers separated by space: ").split())
#
# # Finding HCF using math.gcd
# hcf = math.gcd(num1, num2)
#
# # Output
# print("HCF of", num1, "and", num2, "is:", hcf)
