
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

class AuthenticationTest(APITestCase):

    def test_user_signup(self):
        response = self.client.post(reverse('signup'), data={
            'username': 'user@example.com',
            'password': PASSWORD,
            'password1': PASSWORD,
            'first_name': 'Hassan',
            'last_name': 'Azam'
        })

        user = get_user_model().objects.last()
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data['id'], user.id)
        self.assertEqual(response.data['username'], user.username)
        self.assertEqual(response.data['first_name'], user.first_name)
        self.assertEqual(response.data['last_name'], user.last_name)
