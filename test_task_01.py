# -*- coding: utf-8 -*-"

"""
Tests for task 01
"""

from task_01.core import get_days_from_today


if __name__ == "__main__":
    try:
        print(get_days_from_today('2025-06-01'))
    except Exception as e:
        print(e)

    try:
        print(get_days_from_today('2025-06-07'))
    except Exception as e:
        print(e)

    try:
        print(get_days_from_today('2025-06-17'))
    except Exception as e:
        print(e)

    try:
        print(get_days_from_today(''))
    except Exception as e:
        print(e)

    try:
        print(get_days_from_today(None))
    except Exception as e:
        print(e)
