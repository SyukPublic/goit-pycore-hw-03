# -*- coding: utf-8 -*-"

"""
Tests for task 02
"""

from task_02.core import get_numbers_ticket


if __name__ == "__main__":
    try:
        print(get_numbers_ticket(1, 49, 6))
    except Exception as e:
        print(e)

    try:
        print(get_numbers_ticket(1, 1000, 6))
    except Exception as e:
        print(e)

    try:
        print(get_numbers_ticket(0, 1000, 6))
    except Exception as e:
        print(e)

    try:
        print(get_numbers_ticket(1, 10000, 6))
    except Exception as e:
        print(e)

    try:
        print(get_numbers_ticket(1000, 1, 6))
    except Exception as e:
        print(e)

    try:
        print(get_numbers_ticket(1, 1000, 10000))
    except Exception as e:
        print(e)

    try:
        print(get_numbers_ticket(1, 1000, 0))
    except Exception as e:
        print(e)
