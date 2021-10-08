#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Oct 2021
# This program checks if the input is an odd number or even number


def main():
    # this function checks if the input is an odd number or even number

    # input
    user_input_as_str = input("Enter any positive integer: ")
    print("")

    # process and output
    try:
        user_input_as_int = int(user_input_as_str)
        if user_input_as_int % 2 == 0:
            print("{0} is an even number.".format(user_input_as_str))
            print("")
        elif user_input_as_int % 2 == 1:
            print("{0} is an odd number.".format(user_input_as_str))
            print("")
    except Exception:
        print("{0} is not an integer, try again.".format(user_input_as_str))
        print("")
    finally:
        print("Thanks for checking.")
    print("\nDone.")


if __name__ == "__main__":
    main()
