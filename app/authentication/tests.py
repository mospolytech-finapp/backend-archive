#!/usr/bin/env python
import requests

url = 'http://localhost:8000/api/auth/token/'
data = {
    'username': 'romamar2004@gmail.com',
    'password': '34543588741asad',
}
headers = {
    'Content-Type': 'application/json',
}

response = requests.post(url, json=data, headers=headers)

print(response.status_code)
print(response.json())