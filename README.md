# FastAPI URL Shortener

This is a simple URL shortener implemented using FastAPI. It allows you to generate short alphanumeric codes for long URLs, making it easier to share and manage links.

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies using pip:

```
pip install fastapi
pip install uvicorn

```

## Usage

1. Open a terminal or command prompt and navigate to the project directory.
2. Run the FastAPI server using the following command:

```
uvicorn main:app --reload

```

The server should be running now. You can access it at [http://localhost:8000](http://localhost:8000/).

### Shortening URLs

To shorten a URL, use the `shorten.py` script provided in the repository. It includes functions to generate a random code and save the code-link mappings to a JSON file.

Here's an example of how to use the `shorten_link` function:

```
from shorten import shorten_link

link_to_shorten = "https://www.example.com"
shorten_link(link_to_shorten)

```

The `shorten_link` function will generate a random alphanumeric code and save the mapping between the code and the original link in the 'codes.json' file in the current working directory.

## Redirection

To access the original URL using the generated code, simply make a GET request to the shortened URL with the generated code as the path. For example, if the generated code is `3lmf2z5vw`, you can access the original URL at `http://localhost:8000/3lmf2z5vw`.

The FastAPI server will redirect you to the associated URL if the code is found in the 'codes.json' file. If the code is not found, the server will return a 404 Not Found response.

## JSON Format

The 'codes.json' file stores the code-link mappings in the following format:

```
[
  {
    "code": "3lmf2z5vw",
    "website": "http://localhost:8000/3lmf2z5vw",
    "redirection": "https://www.google.com"
  },
  {
    "code": "rDwQ39LtG",
    "website": "http://localhost:8000/rDwQ39LtG",
    "redirection": "https://www.example.com"
  },
  ...
]

```

Each entry in the JSON array represents a code-link mapping. The `code` field contains the randomly generated alphanumeric code, the `website` field contains the shortened URL, and the `redirection` field contains the original long URL.

## Notes

- If the 'codes.json' file does not exist, the `load_codes` function will return an empty list.
- The `generate_code` function in 'shorten.py' generates a 9-character random alphanumeric code by default. You can specify a different length as an argument when calling the function if needed.

Enjoy using the FastAPI URL Shortener! If you have any questions or issues, please feel free to reach out or open an issue in the repository.
