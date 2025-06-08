# -*- coding: utf-8 -*-"

"""
Tests for the alternative flow of task 03
"""

from task_03.core import normalize_phone_alt


if __name__ == "__main__":
    try:
        print(normalize_phone_alt(''))
    except Exception as e:
        print(e)

    try:
        print(normalize_phone_alt('067 123 45'))
    except Exception as e:
        print(e)

    try:
        print(normalize_phone_alt('67 123 45-67'))
    except Exception as e:
        print(e)

    try:
        print(normalize_phone_alt('(067) 123 45-67'))
    except Exception as e:
        print(e)

    try:
        print(normalize_phone_alt('+380671234567'))
    except Exception as e:
        print(e)

    try:
        print(normalize_phone_alt('+38(067) 123-45-67'))
    except Exception as e:
        print(e)

    try:
        print(normalize_phone_alt('+38(067) 123+45+67'))
    except Exception as e:
        print(e)

    try:
        print(normalize_phone_alt('  +38(067)\t123 4567'))
    except Exception as e:
        print(e)

    try:
        print(normalize_phone_alt('\n\tabc  +38(067)\t123 4567'))
    except Exception as e:
        print(e)

    try:
        print(normalize_phone_alt('abc+a38(067)\t123 4567'))
    except Exception as e:
        print(e)

    try:
        print(normalize_phone_alt('abc+38(067)-123-45-67'))
    except Exception as e:
        print(e)

    try:
        print(normalize_phone_alt('abc++38(067)-123-45-67'))
    except Exception as e:
        print(e)

    try:
        raw_numbers = [
            "067\\t123 4567",
            "(095) 234-5678\\n",
            "+380 44 123 4567",
            "380501234567",
            "    +38(050)123-32-34",
            "     0503451234",
            "(050)8889900",
            "38050-111-22-22",
            "38050 111 22 11   ",
        ]
        sanitized_numbers = [normalize_phone_alt(num) for num in raw_numbers]
        print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
    except Exception as e:
        print(e)
