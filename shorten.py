import json
import secrets
import string


def generate_code(length=9):
    """
    Generates a random alphanumeric code of given length.

    Parameters:
    - length (int): The length of the random alphanumeric code. Default is 9.

    Returns:
    - str: A random alphanumeric code of the given length.
    """
    alphanumeric = string.ascii_letters + string.digits
    random_string = "".join(secrets.choice(alphanumeric)
                            for _ in range(length))
    return random_string


def load_codes():
    """
    Loads the existing data (codes and links) from the JSON file.

    Returns:
    - list: The list of existing code-link mappings.
    """
    try:
        with open("codes.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data


def save_codes(data):
    """
    Saves the code-link mappings to the JSON file.

    Parameters:
    - data (list): The list of code-link mappings to be saved.
    """
    with open("codes.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


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
    data = load_codes()

    while True:
        code = generate_code()
        exists = any(item["code"] == code for item in data)
        if not exists:
            break

    data.append({
        "code": code,
        "website": f"http://localhost:8000/{code}",
        "redirection": link
    })

    save_codes(data)


if __name__ == "__main__":
    link_to_shorten = "https://www.example.com"
    shorten_link(link_to_shorten)
