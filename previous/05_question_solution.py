def find_occurrences(arr, target):
    first_occurrence = -1
    last_occurrence = -1

    for i in range(len(arr)):
        if arr[i] == target:
            if first_occurrence == -1:
                first_occurrence = i
            last_occurrence = i

    return first_occurrence, last_occurrence


# Input from user
input_array = list(map(int, input("Enter the elements of the array separated by space: ").split()))
target_element = int(input("Enter the target element: "))

# Find occurrences
first_index, last_index = find_occurrences(input_array, target_element)

# Output
print("First occurrence index:", first_index)
print("Last occurrence index:", last_index)
