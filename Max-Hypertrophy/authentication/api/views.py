'''from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import Token
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated'''
import requests

response = requests.get('http://127.0.0.1:8000/users/?user=adrianrangel')

user = response.json()
print(user[0]['name'])

for user in response.json():
    print(user)
'''for key, values in user:
        print(key, values)'''