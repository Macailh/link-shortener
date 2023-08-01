from fastapi import FastAPI
from fastapi.responses import RedirectResponse as redirect
import json

app = FastAPI()


@app.get("/{code}")
def redirection(code: str):
    """
    Redirects the user to a specified URL based on the given code.

    Parameters:
    - code (str): A string representing the code used to look up the redirection URL.

    Returns:
    - RedirectResponse: If the provided code matches an entry in the 'codes.json' file,
      a redirect response will be returned with a status code 302, redirecting the user
      to the associated URL.
    - dict: If the provided code is not found in the 'codes.json' file, a JSON object
      will be returned with a "message" key set to "Not found".
    """
    data = []

    with open("codes.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    res = list(filter(lambda item: item["code"] == code, data))

    if res:
        return redirect(url=res[0]["redirection"], status_code=302)
    return {"message": "Not found"}
