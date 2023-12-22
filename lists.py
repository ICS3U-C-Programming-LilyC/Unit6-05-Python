#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Dec/20/2023
# This program will get user input of marks between 0 and 100.
# It uses a loop to get marks and will stop once the user enters -1.
# Then it will calculate/display their average.


def calc_average(list_of_marks):
    # Initializing variable sum to 0
    sum = 0

    # Check to see if 0 was entered, if it was then return -1 to function.
    if len(list_of_marks) == 0:
        return -1

    else:
        # Using a for loop to calculate average.
        for a_num in list_of_marks:
            sum = sum + a_num

        average = sum / len(list_of_marks)

        # Returning the average to the function.
        return average


def main():
    # Explaining my program to the user.
    print(
        "Welcome to my average calculator program. Please enter in your marks (between 0-100) and enter -1 to exist. I will calculate your average based on your mark inputs."
    )

    # Declaring list for user's marks.
    list_of_user_marks = []

    # Using a for loop to repeat this part of the program.
    for counter in range(0, 100):
        # Getting user input as a string.
        mark_as_string = input("Enter a mark: ")

        # Using a try catch to catch any invalid inputs.
        try:
            # Converting user input into a integer.
            mark_as_float = float(mark_as_string)

            # Check if the user wants to break
            if mark_as_float == -1:
                break

            # Check if the mark is outside the valid range
            if mark_as_float < 0 or mark_as_float > 100:
                # Display error message for invalid input.
                print("Invalid mark.")
            else:
                # Append valid numbers to the list
                list_of_user_marks.append(mark_as_float)

        # Catching any errors.
        except:
            print("Invalid mark.")
            # Using a continue statement to continue asking for the user's marks.
            continue

    # Check if the user entered any marks.
    if len(list_of_user_marks) == 0:
        print("Invalid mark")
    else:
        # Call function to display the average.
        average = calc_average(list_of_user_marks)
        # Displaying the average of the user's marks.
        print("The average of your marks entered is {:.2F} %.".format(average))


if __name__ == "__main__":
    main()
