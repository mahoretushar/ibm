# Write a program to print all the unique characters in a String. For instance, if the input string is “abcb”, the
# output will be the characters ‘a’ and ‘c’ as they are unique. The character ‘b’ repeats twice and so it will
# not be printed.


input_string = input("Enter a string: ")
unique_characters = set(input_string)
print("Unique characters:", unique_characters)
