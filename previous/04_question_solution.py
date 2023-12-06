def opposite_case_conversion(input_string):
    result_string = ""

    for char in input_string:
        if char.islower():
            result_string += char.upper()
        elif char.isupper():
            result_string += char.lower()
        else:
            result_string += char

    return result_string


# Input
input_string = input("Enter a string: ")

# Convert to Opposite Case
converted_string = opposite_case_conversion(input_string)

# Output
print("String with opposite case:", converted_string)
