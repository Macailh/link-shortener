import json
import secrets
import string


def generate_code():
    alphanumeric = string.ascii_letters + string.digits

    random_string = "".join(secrets.choice(alphanumeric) for i in range(9))

    return random_string
