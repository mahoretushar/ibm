# Consider a string, S, that is a series of characters, each followed by its frequency as an integer.
# The string is not compressed correctly, so there may be multiple occurrences of the same character.
# A properly compressed string will consist of one instance of each character in alphabetical order followed by the
# total count of that character within the string.

def compress_string(string):
    compressed_string = ""
    for i in range(0, len(string), 2):
        compressed_string += string[i] * int(string[i + 1])
    return compressed_string


# def decompress_string(string):
#     decompressed_string = ""
#     for i in range(len(string)):
#         if i % 2 == 0:
#             decompressed_string += string[i]
#         else:
#             decompressed_string += str(string.count(string[i - 1]))
#     return decompressed_string


def main():
    input_string = input("Enter a string: ")
    print("Compressed string:", compress_string(input_string))
    # print("Decompressed string:", decompress_string(input_string))


if __name__ == "__main__":
    main()
