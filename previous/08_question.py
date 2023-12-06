def appendAndDelete(s, t, k):
    common_length = 0

    # Find the length of the common prefix of s and t
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            common_length += 1
        else:
            break

    # Calculate the total operations needed to delete characters from s and append characters from t
    total_operations = len(s) - common_length + len(t) - common_length

    # Check if it's possible to perform exactly k operations
    if total_operations <= k and (k - total_operations) % 2 == 0 or k >= len(s) + len(t):
        return "Yes"
    elif common_length == len(s) and total_operations <= k:
        # Handle case where s is a prefix of t and additional characters need to be appended
        remaining_operations = k - total_operations
        return "Yes" if remaining_operations % 2 == 0 or remaining_operations >= len(t) - common_length else "No"
    else:
        return "No"


# Sample Input
s = input().strip()
t = input().strip()
k = int(input().strip())

# Output
result = appendAndDelete(s, t, k)
print(result)
