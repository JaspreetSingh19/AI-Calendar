"""
This file contains various constants that can be user throughout the project
"""

MAX_LENGTH = {
    'first_name': 30,
    'last_name': 30,
    'password': 16,
    'contact': 10,
    'title': 100
}

MIN_LENGTH = {
    'first_name': 3,
    'last_name': 3,
    'password': 8,
    'contact': 10,
    'title': 5,

}

REGEX = {
    "first_name": r'^[a-zA-Z]+$',
    "last_name": r'^[a-zA-Z]+$',
    "contact": r'^\d+$',
    "password": r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=-])[0-9a-zA-Z!@#$%^&*()_+=-]{8,16}$',
}

CREATE = 'create'