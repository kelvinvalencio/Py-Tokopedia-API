# Py-Tokopedia-API
Implementation example of Tokopedia OpenAPI using Python, with some of its Product API functions:
- get product info
- get all etalase
- update stock
- update price

## Prepare
1. Fill out the constants in the Python code
    ```python
    client_id = b'<your client_id>'
    client_secret = b'<your client_secret>'
    fs_id = '<your fs_id>'
    shop_id = '<your shop_id>'
    ```
2. Install dependencies
    ```sh
    pip install requests
    ```
3. This script will generate file "tokopedia_token.txt" in the same directory it's executed. This file will be used to save token.
    Make sure add proper permissions to **write**, **read**, and **execute**.

## Execute
### Linux
```sh
$ ./tokopedia.py
```
### Windows
```sh
python tokopedia.py
```
### Example of a success response (get_all_etalase function)
```sh
$ ./tokopedia.py
tokopedia_token.txt not found, creating one.
get_token(): response {"access_token":"<>","event_code":"","expires_in":<>,"last_login_type":"<>","sq_check":<>,"token_type":"Bearer"}

{
    "data": {
        "etalase": [
            {
                "alias": "<>",
                "etalase_id": <>,
                "etalase_name": "<>",
                "url": "<>"
            },
            {
                "alias": "<>",
                "etalase_id": <>,
                "etalase_name": "<>",
                "url": "<>"
            },
            {
                "alias": "<>",
                "etalase_id": <>,
                "etalase_name": "<>",
                "url": "<>"
            }
        ],
        "shop": {
            "id": <>,
            "location": "<>",
            "name": "<>",
            "uri": "<>"
        }
    },
    "header": {
        "messages": "Your request has been processed successfully",
        "process_time": 0.080218411
    }
}
```

## Read Full API Documentations
See [Tokopedia OpenAPI Documentation](https://developer.tokopedia.com/openapi/guide/#/)
