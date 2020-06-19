from django.contrib.auth.models import User
from munch import Munch
from model_bakery import baker
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase,APIClient


class UserTest(APITestCase):
    def setUp(self) -> None:
        self.user = baker.make('auth.User', _quantity=1)

    def test_create(self):
        data = {'username': 'donghy', 'password': '12345', 'email': 'tjehdgur1500@naver.com'}
        token = Token.objects.get_or_create()
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token' + token.key)

        response = self.client.post('/users', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user_response = Munch(response.data)
        self.assertTrue(user_response['id'])
        self.assertEqual(user_response['username'], data['username'])
