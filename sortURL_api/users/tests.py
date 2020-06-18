from django.contrib.auth.models import User
from munch import Munch
from rest_framework import status
from rest_framework.test import APITestCase


class UserTest(APITestCase):
    def setUp(self) -> None:
        self.users = User(username='test', password='1234', email='tehdgur@naver.com')
        self.users.set_password(self.users.password)
        self.users.save()

    def test_user_list(self):

        self.client.force_authenticate(user=self.users)
        response = self.client.get('/users/signup')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_craete(self):
        data = {'username':'abc', 'password':'1234','email':'tjehdgur1500@naver.com'}
        response = self.client.post('/users/signup', data=data)
        user_response = Munch(response.data)
        self.assertTrue(user_response['id'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(user_response['username'], data['username'])

    def test_user_detail(self):
        user = self.users
        self.client.force_authenticate(user=self.users)
        response = self.client.get(f'/users/signup/{user.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_update(self):
        user = self.users
        self.client.force_authenticate(user=self.users)
        prev_username = user.username
        data = {'username':'newname', 'password':'123456','email':'dh154@tesmail.com'}

        response = self.client.put(f'/users/signup/{user.id}', data=data)
        user_response = Munch(response.data)
        self.assertEqual(user_response.username, data['username'])
        self.assertNotEqual(user_response.username, prev_username)

    def test_user_delete(self):
        user = self.users
        self.client.force_authenticate(user=self.users)
        response = self.client.delete(f'/users/signup/{user.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.filter(pk=user.id).count(), 0)
        self.assertFalse(User.objects.filter(id=user.id).exists())
        # print(User.objects.filter(id=user.id))