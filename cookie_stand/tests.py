from http import cookies
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CookieStand

###########################################################################################
# ATTENTION:
# DATABASES should be set to use SQLite
# Easiest way to ensure that is to comment out all the Postgres stuff in project/.env
# That will run using defaults, which is SQLite
###########################################################################################


class CookieStandTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_cookie = CookieStand.objects.create(
            location="Cookie",
            owner=testuser1,
            description="Scattered with chocolate chips",
        )
        test_cookie.save()

    # class 32
    def setUp(self):
        self.client.login(username="testuser1", password="pass")

    def test_cookies_model(self):
        cookie = CookieStand.objects.get(id=1)
        actual_owner = str(cookie.owner)
        actual_location = str(cookie.location)
        actual_description = str(cookie.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_location, "Cookie")
        self.assertEqual(actual_description, "Scattered with chocolate chips")

    def test_get_cookie_list(self):
        url = reverse("cookie_stand_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        cookies = response.data
        self.assertEqual(len(cookies), 1)
        self.assertEqual(cookies[0]["location"], "Cookie")

    def test_get_snack_by_id(self):
        url = reverse("cookie_stand_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        cookie = response.data
        self.assertEqual(cookie["location"], "Cookie")

    def test_create_cookie(self):
        url = reverse("cookie_stand_list")
        data = {"owner": 1, "location": "Snickers", "description": "frozen please"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        cookies = CookieStand.objects.all()
        self.assertEqual(len(cookies), 2)
        self.assertEqual(CookieStand.objects.get(id=2).location, "Snickers")

    def test_update_cookie(self):
        url = reverse("cookie_stand_detail", args=(1,))
        data = {
            "owner": 1,
            "location": "Hummus",
            "description": "Generously drizzle with olive oil.",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        cookie = CookieStand.objects.get(id=1)
        self.assertEqual(cookie.location, data["location"])
        self.assertEqual(cookie.owner.id, data["owner"])
        self.assertEqual(cookie.description, data["description"])

    def test_delete_cookie(self):
        url = reverse("cookie_stand_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        cookies = CookieStand.objects.all()
        self.assertEqual(len(cookies), 0)

    def test_authentication_required(self):
        self.client.logout()
        url = reverse("cookie_stand_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
