import requests

url = 'http://127.0.0.1:8000/register/'

data = {
    'email': 'test1@example.com',
    'password': 'password',
    'first_name': 'John',
    'last_name': 'Doe',
    'middle_name': 'Do',
    'gender': 'M',
}

response = requests.post(url, data=data)

print(response.status_code)