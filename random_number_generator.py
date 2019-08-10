#!/usr/bin/python3.6

import sys
import random

"""

Program creates a randomized list of numbers with 6 decimals
places based on the user input of starting and ending numbers, also
the overall size of the list

"""

def create_random_pvalue_list(lowest_value, highest_value, size_of_list):

    """

    Creates the random list of p-values based on user inputs

    : parameter lowest_value: lowest value range
    : parameter highest_value: highest value range
    : size_of_list: number of random values to create

    : return random_pvalue_list: list of random pvalues based
        on user inputs

    """

    # Create an empty list to store value
    random_pvalue_list = []

    # Create a random assortment of p-values
    x = 0

    # Loop until list limit reached
    while x < size_of_list:

        # Create a random number between set values
        random_pvalue = round(random.uniform(lowest_value, highest_value), 6)

        # Add value to list
        random_pvalue_list.append(random_pvalue)

        # Increase the counter by 1
        x += 1

    return (random_pvalue_list)


def main():

    # User Input Parameters
    lowest_value = 0
    highest_value = 1
    size_of_list = 100

    ##############################################
    ########## DO NOT CHANGE BELOW ###############
    
    random_pvalue_list = create_random_pvalue_list(lowest_value, highest_value,
                                                   size_of_list)

    print (random_pvalue_list)


if __name__ == "__main__":
    
    main()
