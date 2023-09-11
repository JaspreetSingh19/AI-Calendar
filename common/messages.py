"""
This file contains various messages like validation and success that
can be user throughout the project
"""

VALIDATION = {
    'first_name': {
        "blank": "First Name can not be blank",
        "invalid": "First Name must contain only alphabets, no spaces, numbers or special characters",
        "required": "First Name required",
    },
    'last_name': {
        "blank": "Last Name can not be blank",
        "invalid": "Last Name must contains only alphabets, no spaces, numbers or special characters",
        "required": "Last Name required",
    },
    'email': {
        "blank": "Email can not be blank",
        "required": "Email required",
        "exists": "Email already exist",
    },
    'contact': {
        "blank": "Contact can not be blank",
        "required": "Contact required",
        "invalid": "Invalid contact",
        "exists": "Contact already exist",
    },
    'password': {
        "blank": "Password can not be blank",
        "invalid": "Password must contain uppercase, lowercase, digit and special character",
        "required": "Password required",
        "do_not_match": "Passwords do not match",
    },
    "invalid_credentials": "Invalid Credentials",
    "meeting_conflicts": "Meeting conflicts with an existing meeting.User already has a meeting at the particular time"
                         ".Please change meeting times"


}
SUCCESS_MESSAGES = {
    'registration': {
        'successfully': 'Registration has been success',
    },
    'login': {
        'success': 'Login successfully'
    },
    'logout': {
        'success': 'Logout Successfully'
    },
    'meeting': {
        'created': 'Meeting created',
        'deleted': 'Meeting deleted',
    }
}
