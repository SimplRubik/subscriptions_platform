from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import CustomUser

class UserAuthTests(APITestCase):

    def test_register_user(self):
        url = reverse('register')
        data = {
            'username': 'usertest',
            'email': 'test@gmail.com',
            'password': 'Pass12371!',
            'password2': 'Pass12371!',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().username, 'usertest')
    
    def test_login_user(self):
        user = CustomUser.objects.create_user(username='usertest', email='test@gmail.com', password='Pass12371!')
        url = reverse('token_obtain_pair')
        data = {
            'username': 'usertest',
            'password': 'Pass12371!'
        }
        response = self.client.post(url, data, format='json')
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_access(self):
        user = CustomUser.objects.create_user(username='usertest', password='Pass12371!')
        url = reverse('profile')
        self.client.force_authenticate(user=user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'usertest')

        


