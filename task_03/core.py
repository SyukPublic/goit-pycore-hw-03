# -*- coding: utf-8 -*-"

"""
Core functions for task 03
"""

import typing
import re

# Pattern of the phone number cleaning from garbage
# - removes all non-digit characters unless they are '+'
PATTERN_CLEANING_STEP_01 = re.compile(r'[^+\d]+')
# - removes all '+' except the one at the beginning of the string
PATTERN_CLEANING_STEP_02 = re.compile(r'(?<!^)\+')

# Pattern of the phone number ungroup by country code, carrier code, and number
PATTERN_PHONE_NUMBER_UNGROUP = re.compile(r'(\+?\d{,4})(\d{2})(\d{7})')

# Pattern of the country code verification
PATTERN_COUNTRY_CODE_VERIFY = re.compile(r'^\+\d{3}$')


def normalize_phone(phone_number: typing.Optional[str]) -> typing.Optional[str]:
    """The function generates a list of unique random numbers of the specified length within the given range.

    :param phone_number: phone number string
    :return: A list of unique random numbers within a specified range (list of integer)
    """
    try:
        # Validate the phone_number parameter value before cleaning
        if phone_number is None:
            raise ValueError('Phone number can`t be None')

        # Clean phone number from garbage symbols
        phone_number = re.sub(PATTERN_CLEANING_STEP_01, '', phone_number)
        phone_number = re.sub(PATTERN_CLEANING_STEP_02, '', phone_number)

        # Validate the phone_number parameter value after cleaning
        if not 9 <= len(phone_number) <= 13:
            raise ValueError('String is not a valid phone number')

        # Ungroup phone number by country code, carrier code, and number
        match = re.search(PATTERN_PHONE_NUMBER_UNGROUP, phone_number)
        if match is not None:
            country_code, carrier_code, number = match.groups()
            match len(country_code):
                case 0:
                    country_code = '+380' + country_code
                case 1:
                    country_code = '+38' + country_code
                case 2:
                    country_code = '+3' + country_code
                case 3:
                    country_code = '+' + country_code
                case _:
                    # Nothing to do
                    pass

            if re.match(PATTERN_COUNTRY_CODE_VERIFY, country_code) is None:
                raise ValueError('String is not a valid phone number')
        else:
            raise ValueError('String is not a valid phone number')

        return country_code +  carrier_code + number
    except ValueError as e:
        # The parameter has an incorrect value
        # Raise exception to the upper level
        raise Exception('Incorrect phone number.')
    except Exception as e:
        # An unexpected error occurred
        # Raise exception to the upper level
        raise Exception('An unexpected error occurred: {error}.'.format(error=repr(e)))
