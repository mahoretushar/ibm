# HH:MM:SS
def minMaxTime(time):
    blank_position = time.index('@')
    possible_values = range(10) if blank_position in [1, 4, 7] else range(4) if time[0] == '2' else range(10)
    times = [time[:blank_position] + str(value).zfill(2) + time[blank_position + 1:] for value in possible_values]

    print("Possible values:", possible_values)
    print("MIN Time:", min(times))
    print("MAX Time:", max(times))


# Input from user
user_input = input("Enter the time with a blank represented by @: ")
minMaxTime(user_input)
