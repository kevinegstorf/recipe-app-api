from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successfull(self):
        # TEST CREATING A NEW USER WITH AN EMAIL IS SUCCESFUL
        email = "test@test.com"
        password = "TESTPASS123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        # TEST THE EMAIL FOR A NEW USER IS NORMALIZED

        email = "test@test.com"
        password = "TESTPASS123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        # TEST CREATING USER WITH NO EMAIL RAISES ERROR
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None, "test123"
            )

    def test_create_new_superuser(self):
        # TEST CREATING A NEW SUPERUSER
        email = "test@test.com"
        password = "TESTPASS123"
        user = get_user_model().objects.create_superuser(email, password)

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
