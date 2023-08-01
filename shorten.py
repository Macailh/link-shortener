import json
import secrets
import string


def generate_code():
    """
    Generates a random alphanumeric code of length 9.

    Returns:
    - str: A random alphanumeric code.
    """
    alphanumeric = string.ascii_letters + string.digits
    random_string = "".join(secrets.choice(alphanumeric) for i in range(9))
    return random_string


def shorten_link(link):
    """
    Shortens a given URL link by generating a unique code and saving the mapping
    between the code and the original link in a JSON file.

    Parameters:
    - link (str): The URL link to be shortened.

    Notes:
    - This function will write the mapping between the generated code and the original link
      to a JSON file named 'codes.json' in the current working directory.
    """
    code = generate_code()

    data = []

    with open("codes.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    exists = any(item["code"] == code for item in data)

    if exists:
        code = generate_code()

    with open("codes.json", "w", encoding="utf-8") as file:
        data.append(
            {
                "code": code,
                "website": f"http://localhost:8000/{code}",
                "redirection": link
            }
        )
        json.dump(data, file, indent=2)
