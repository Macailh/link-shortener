from fastapi import FastAPI
from fastapi.responses import RedirectResponse as redirect
import json

app = FastAPI()


@app.get("/{code}")
def redirection(code: str):
    data = []

    with open("codes.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    res = list(filter(lambda item: item["code"] == code, data))

    if res:
        return redirect(url=res[0]["redirection"], status_code=302)
    return {"message": "Not found"}
