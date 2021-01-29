from requests import get
parameters = {
        "amount": 10,
        "type": "boolean",
    }
response = get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data['results']
