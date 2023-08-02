from fastapi import FastAPI, Path, HTTPException, Depends
from fastapi.responses import RedirectResponse as redirect
import json

app = FastAPI()


def get_data():
    try:
        with open("codes.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []


@app.get("/{code}")
def redirection(code: str = Path(..., title="Code to look up for redirection"),
                data: list = Depends(get_data)):
    """
    Redirects the user to a specified URL based on the given code.

    Parameters:
    - code (str): A string representing the code used to look up the redirection URL.
    - data (list): JSON data loaded from 'codes.json' using the 'get_data' dependency.

    Returns:
    - RedirectResponse: If the provided code matches an entry in the 'codes.json' file,
      a redirect response will be returned with a status code 302, redirecting the user
      to the associated URL.
    - HTTPException: If the provided code is not found in the 'codes.json' file, an HTTP
      exception with status code 404 and a JSON object will be returned with a "message"
      key set to "Not found".
    """
    res = next((item for item in data if item["code"] == code), None)

    if res:
        return redirect(url=res["redirection"], status_code=302)

    raise HTTPException(status_code=404, detail={"message": "Not found"})
