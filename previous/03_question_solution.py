def decimal_to_binary(decimal_number):
    binary_representation = bin(decimal_number)
    return binary_representation[2:]  # Removing the '0b' prefix


# Input
decimal_number = int(input("Enter a decimal number: "))

# Convert to Binary
binary_representation = decimal_to_binary(decimal_number)

# Output
print(f"The binary representation of {decimal_number} is: {binary_representation}")
