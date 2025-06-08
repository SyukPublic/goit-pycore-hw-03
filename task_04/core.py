# -*- coding: utf-8 -*-"

"""
Core functions for task 04
"""

import typing
import datetime


def get_date_for_year(date: datetime.date, year: int) -> datetime.date:
    """The function returns the date shifted to the specified year. If the date is on February 29 and
    today's year is not a leap year, move it to March 1.

    :param date: Date to be shifted to the specified year (date, mandatory)
    :param year: Year to which the date should be shifted (int, mandatory)
    :return: Date shifted to the specified year (date)
    """
    try:
        return date.replace(year=year)
    except ValueError:
        # Handles February 29 in a non-leap year, shifts it to March 1
        return datetime.date(year, 3, 1)


def get_next_birthday(birthdate: datetime.date, today: datetime.date) -> datetime.date:
    """The function returns the next birthday. If the birthday is on February 29 and today's year is not a leap year,
    move it to March 1.

    :param birthdate: Date of birth string in 'YYYY.MM.DD' format (date, mandatory)
    :param today: Today's date (date, mandatory)
    :return: Next birthday date (date)
    """
    birthday_this_year = get_date_for_year(birthdate, today.year)
    if birthday_this_year < today:
        # If the birthday has already passed this year, shift the date to the next year
        birthday_this_year = get_date_for_year(birthdate, today.year + 1)
    return birthday_this_year


def get_congratulation_date(
        birthday_str: str,
        congratulation_range_days: int,
        today: typing.Optional[datetime.date] = None,
) -> typing.Optional[str]:
    """Convert the date of birth from a string to a datetime object and calculate the congratulation date.
    If the birthday is not within the next congratulation_range_days days, including today, return None.
    If the birthday falls on a weekend, the congratulation date is shifted to the following Monday.

    :param birthday_str: Date of birth string in 'YYYY.MM.DD' format (str, mandatory)
    :param congratulation_range_days: Congratulations days range (int, mandatory)
    :param today: Today's date, if not specified, is calculated as the current date (date, optional)
    :return: Congratulation date as string in 'YYYY.MM.DD' format (str)
    """
    try:
        # If today parameter is None, determine the current date
        if today is None:
            today = datetime.datetime.today().date()

        # Calculate next birthday
        next_birthday: datetime.date = get_next_birthday(
            datetime.datetime.strptime(birthday_str, '%Y.%m.%d').date(),
            today
        )

        # Verify if the birthday is within the next congratulation_range_days days, including today
        if not 0 <= (next_birthday - today).days <= congratulation_range_days:
            # If the birthday is not within the next congratulation_range_days days, including today, return None
            return None

        # Verify if the birthday falls on a weekend
        if next_birthday.isoweekday() in {6, 7, }:
            # Shift the congratulation date to the following Monday, as it falls on a weekend
            next_birthday += datetime.timedelta(days=((7 - next_birthday.isoweekday()) + 1))

        # Return congratulation date as string in 'YYYY.MM.DD' format
        return next_birthday.strftime('%Y.%m.%d')
    except ValueError:
        # The parameter has an incorrect value
        # Raise an exception to the upper level
        raise Exception('Wrong date format. A date in the format "YYYY.MM.DD" is required.')
    except Exception as e:
        # An unexpected error occurred
        # Raise an exception to the upper level
        raise Exception('An unexpected error occurred: {error}.'.format(error=repr(e)))


def get_upcoming_birthdays(users: typing.List[typing.Dict[str, str]]) -> typing.List[typing.Dict[str, str]]:
    """The function returns a list of all users whose birthday is within the next 7 days, including today,
    along with the congratulation date. If the birthday falls on a weekend, the congratulation date
    is moved to the following Monday.

    :param users: A list of users (list of dict)
    :return: A list of all users whose birthday is within the next 7 days, including today,
    along with the congratulation date (list of dict)
    """
    try:
        upcoming_birthdays: typing.List[typing.Dict[str, str]] = []

        today: datetime.date = datetime.datetime.today().date()

        for user in users:
            try:
                name: typing.Optional[str] = user.get('name')
                congratulation_date: typing.Optional[str] = get_congratulation_date(user.get('birthday'), 7, today)
                if name and congratulation_date:
                    upcoming_birthdays.append(dict(name=name, congratulation_date=congratulation_date))
            except Exception as e:
                # An unexpected error occurred
                # Raise exception to the upper level
                raise e

        return upcoming_birthdays
    except Exception as e:
        # An unexpected error occurred
        # Raise exception to the upper level
        raise Exception('An unexpected error occurred: {error}.'.format(error=repr(e)))
