from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.urls import reverse

User = get_user_model()

class AuthTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="u1", password="p@ss12345")

    def test_login_success(self):
        url = reverse("token_obtain_pair")
        res = self.client.post(url, {"username": "u1", "password": "p@ss12345"}, format="json")
        self.assertEqual(res.status_code, 200)
        self.assertIn("access", res.data)
        self.assertIn("refresh", res.data)

    def test_login_fail(self):
        url = reverse("token_obtain_pair")
        res = self.client.post(url, {"username": "u1", "password": "wrong"}, format="json")
        self.assertEqual(res.status_code, 401)

    def test_refresh(self):
        login = self.client.post(reverse("token_obtain_pair"), {"username": "u1", "password": "p@ss12345"}, format="json").data
        res = self.client.post(reverse("token_refresh"), {"refresh": login["refresh"]}, format="json")
        self.assertEqual(res.status_code, 200)
        self.assertIn("access", res.data)
