from munch import Munch
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token


class UserTest(APITestCase):
    def setUp(self) -> None:
        self.user = baker.make('auth.User', _quantity=1)

    def test_create_login_logout(self):
        data = {'username': 'donghy', 'password': '12345', 'email': 'tjehdgur1500@naver.com'}
        response = self.client.post('/users', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user_response = Munch(response.data)
        self.assertTrue(user_response['id'])
        self.assertEqual(user_response['username'], data['username'])

        login_data = {
            "username": user_response['username'],
            "password": "12345",
            "email": user_response['email']
        }
        response = self.client.post('/users/login', data=login_data)

        token = response.data.get('token')

            self.assertTrue(response.data['token'])

        response = self.client.delete(f'/users/logout', HTTP_AUTHORIZATION='Token ' + token)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Token.objects.filter(key=token).count(), 0)
        self.assertIsNone(Token.objects.filter(key=token).first())

    def test_list(self):
        response = self.client.get('/users')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data)

    def test_detail(self):
        user = self.user[0]
        response = self.client.get(f'/users/{user.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], user.id)
        self.assertTrue(response.data)

