#!/usr/bin/env python
import requests


def reg():
    url = 'http://127.0.0.1:8000/api/auth/register/'

    data = {
        'email': 'test@fintech.ru',
        'password': 'my_very_$trong_pswd',
        'first_name': 'First',
        'last_name': 'Last',
        'middle_name': 'Middle',
        'gender': 'M',
    }

    response = requests.post(url, data=data)

    print(response.status_code)
    print(response.json())


def login():
    url = 'http://127.0.0.1:8000/api/auth/login/'

    data = {
        'email': 'test@fintech.ru',
        'password': 'my_very_$trong_pswd',
    }

    response = requests.post(url, data=data)

    print(response.status_code)
    print(response.json())


reg()
login()
