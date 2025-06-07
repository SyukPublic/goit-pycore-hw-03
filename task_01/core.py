# -*- coding: utf-8 -*-"

"""
Core functions for task 01
"""

import typing
import datetime


def get_days_from_today(date_str: typing.Optional[str]) -> int:
    """Convert the input date from a string to a datetime object and
    calculate the number of days between the input date and the current date

    :param date_str: input date string in 'YYYY-MM-DD' format (str, optional)
    :return: number of days between the input date and the current date (int)
    """
    try:
        return (datetime.datetime.today().date() - datetime.datetime.strptime(date_str, '%Y-%m-%d').date()).days
    except ValueError:
        # The parameter has an incorrect value
        # Raise exception to the upper level
        raise Exception('Wrong date format. A date in the format "YYYY-MM-DD" is required.')
    except Exception as e:
        # An unexpected error occurred
        # Raise exception to the upper level
        raise Exception('An unexpected error occurred: {error}.'.format(error=repr(e)))
