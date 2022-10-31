from django.test import TestCase

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
