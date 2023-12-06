def minMaxTime(time):
    # Identify the position of the blank in the time string
    blank_position = time.index('@')

    # Determine the possible values for the blank position
    if blank_position == 0:
        start_range, end_range = (2, 3) if time[1] == '2' else (0, 2)
    elif blank_position == 1:
        start_range, end_range = (0, 9)
    elif blank_position == 3:
        start_range, end_range = (0, 5)
    elif blank_position == 4:
        start_range, end_range = (0, 9)
    elif blank_position == 6:
        start_range, end_range = (0, 5)
    elif blank_position == 7:
        start_range, end_range = (0, 9)

    # Initialize minimum and maximum times as None
    min_time, max_time = None, None

    # Iterate through all possible values for the blank position
    for value in range(start_range, end_range + 1):
        # Replace the blank position with the current value
        updated_time = time[:blank_position] + str(value) + time[blank_position + 1:]

        # Update minimum and maximum times
        if min_time is None or updated_time < min_time:
            min_time = updated_time
        if max_time is None or updated_time > max_time:
            max_time = updated_time

    print("MIN Time:", min_time)
    print("MAX Time:", max_time)


# Input from user
user_input = input("Enter the time with a blank represented by @: ")
minMaxTime(user_input)
