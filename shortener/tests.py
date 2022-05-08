import json
from rest_framework import status
from django.test import TestCase
from .models import Shortener
from django.contrib.auth import get_user_model
from rest_framework.test import force_authenticate, APIClient

User = get_user_model()

# Create your tests here.
class ModelTestCase(TestCase):
    
    def setUp(self):
        self.short = Shortener(
            website='youtube.com'
        )
        self.test_user = User(
                email='test@gmail.com',
                username='testuser',
                password='password123'
            )
    
    def test_model_save(self):
        self.assertEqual(self.short.visit_count, 0)

class APITestCase(TestCase):
    """
    Test for Api Endpoints
    """

    def setUp(self):
        self.client = APIClient()
        self.test_user = User(
                email='test@gmail.com',
                username='testuser',
                password='password123'
            )
        self.client.force_authenticate(user=self.test_user)

    def test_fetches_shortened_urls(self):
        response = self.client.get('/st/')
        self.assertEqual(response.content.decode('utf-8'), '[]')
