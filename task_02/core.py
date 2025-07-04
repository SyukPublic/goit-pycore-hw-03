# -*- coding: utf-8 -*-"

"""
Core functions for task 02
"""

import typing
import random


def get_numbers_ticket(min_number: int, max_number: int, quantity: int) -> typing.List[int]:
    """The function generates a list of unique random numbers of the specified length within the given range.

    :param min_number: Minimum possible number in the set (int, mandatory, must be equal or greater than 1)
    :param max_number: Maximum possible number in the set (int, mandatory, must be equal or greater than 1000)
    :param quantity: Number of values to be selected (int, mandatory, must be in the range of min_number and max_number)
    :return: A list of unique random numbers within a specified range (list of integer)
    """

    try:
        # Validate the input parameters' value
        if min_number < 1:
            raise ValueError('The minimal possible number can`t be less than 1')
        if max_number > 1000:
            raise ValueError('The maximum possible number can`t be greater than 1000')
        if min_number >= max_number:
            raise ValueError(
                'The minimal possible number can`t be equal to or greater than the maximum possible number'
            )
        if not min_number < quantity < max_number:
            raise ValueError(
                'The number of values to be selected must be in the range of '
                'minimum and maximum possible numbers'
            )

        # Generate a sequence of numbers from min_number to max_number inclusive
        # Select a quantity of unique random values from the previously generated sequence
        numbers: typing.List[int] = random.sample(list(range(min_number, max_number + 1)), quantity)
        # Sort the selected numbers
        numbers.sort()

        return numbers
    except ValueError:
        # The parameter has an incorrect value
        # Do nothing, log error if needed
        return []
    except Exception as e:
        # An unexpected error occurred
        # Raise exception to the upper level
        raise Exception('An unexpected error occurred: {error}.'.format(error=repr(e)))
