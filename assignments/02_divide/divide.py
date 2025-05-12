#!/usr/bin/env python3
"""
Author : Parker Geffre <parkergeffre@arizona.edu>
Date   : 2025-02-09
Purpose: To successfully divide two numbers.
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Divisor", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # This is for named argument for one single number you need to use a positional argument to get a list of numbers
    #    parser.add_argument('-i',
    #                        '--int',
    #                        help='A named integer argument',
    #                        metavar='int',
    #                        nargs='+',
    #                        type=int,
    #                        default=0)

    parser.add_argument(
        "nums",
        metavar="int",
        type=int,
        nargs="+",  # you can set this to 2, so you don't have to check below.
        help="Two numbers to divide",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Divide the integers"""

    args = get_args()
    # I changed int_arg to num_list to show it is a list coming in...
    num_list = args.nums

    # Your code had this error:
    # TypeError: object of type 'int' has no len()
    # The error above was due to the fact that only one number was being passed in.
    # Note that you are checking the number of arguments here, which is fine
    # But, it is just way more code than you need. You can do this by using argparse to check for you
    # see comment above.

    if len(num_list) > 2:  # ensure no more than two args.
        print("usage : too many arguments.")
        quit(1)  # set to 1 to output an error, 0 means success.

    # I added this to fix another error that crops up...
    # what if the user only gives you 1 number?
    if len(num_list) < 2:
        print("usage : too few arguments.")
        quit(1)  # set to 1 to output an error, 0 means success.

    num = num_list[0]
    den = num_list[1]

    if den == 0:
        # needs to have a lower case message, ugh.
        # print("Cannot divide by zero, dum-dum!")
        print("usage: Cannot divide by zero, dum-dum!")
        quit(1)  # set to 1 to output an error, 0 means success.
    # should use floor division
    res = num // den

    print(f"{num} / {den} = {res}")


# --------------------------------------------------
if __name__ == "__main__":
    main()
