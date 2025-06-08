# -*- coding: utf-8 -*-"

"""
Tests for task 04
"""

from task_04.core import get_upcoming_birthdays


if __name__ == "__main__":
    try:
        print(
            get_upcoming_birthdays(
                [
                    {"name": "John Doe", "birthday": "1985.01.23"},
                    {"name": "Jane Smith", "birthday": "1990.01.27"},
                ]
            )
        )
    except Exception as e:
        print(e)

    try:
        print(
            get_upcoming_birthdays(
                [
                    {"name": "John Doe", "birthday": "1980.06.08"},
                    {"name": "Jane Smith", "birthday": "2000.02.29"},
                    {"name": "Noah Thompson", "birthday": "1997.06.15"},
                    {"name": "Emma Reynolds", "birthday": "2007.06.14"},
                    {"name": "Ethan Walker", "birthday": "1990.07.30"},
                    {"name": "Olivia Bennett", "birthday": "2010.11.20"},
                    {"name": "Liam Carter", "birthday": "1970.12.31"},
                    {"name": "Sophia Mitchell", "birthday": "1985.01.01"},
                ]
            )
        )
    except Exception as e:
        print(e)
