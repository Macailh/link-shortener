import json
import secrets
import string


def generate_code():
    alphanumeric = string.ascii_letters + string.digits

    random_string = "".join(secrets.choice(alphanumeric) for i in range(9))

    return random_string


def shorten_link(link):
    code = generate_code()

    data = []

    with open("codes.json", "r") as file:
        data = json.load(file)

    exists = any(item["code"] == code for item in data)

    if exists:
        code = generate_code()

    with open("codes.json", "w") as file:
        data.append(
            {
                "code": code,
                "website": f"http://localhost:5000/{code}",
                "redirection": link
            }
        )
        json.dump(data, file, indent=2)


shorten_link("https://www.google.com")
