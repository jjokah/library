from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            slackUsername="James", backend=False, age=52, bio="Sent from God"
        )

    def test_model_content(self):
        self.assertEqual(self.user.slackUsername, "James")
        self.assertEqual(self.user.backend, False)
        self.assertEqual(self.user.age, 52)
        self.assertEqual(self.user.bio, "Sent from God")
        self.assertEqual(str(self.user), "James profile")

    def test_api_listview(self):
        response = self.client.get(reverse("user_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertContains(response, "James")

    def test_api_detailview(self):
        response = self.client.get(
            reverse("user_detail", kwargs={"pk": self.user.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertContains(response, "God")
