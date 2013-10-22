from django.test import TestCase
from django.contrib.auth.models import User


class BaseTestCase(TestCase):

    # 1st user
    USERNAME = 'john'
    EMAIL = 'john@gmail.com'
    PASSWORD = 'admin'

    # 2nd user
    USERNAME2 = 'francie'
    EMAIL2 = 'francie@gmail.com'
    PASSWORD2 = 'admin'

    def setUp(self):
        # 1st user
        self.user = User.objects.create_user(self.USERNAME, self.EMAIL, self.PASSWORD)
        # 2nd user
        self.user2 = User.objects.create_user(self.USERNAME2, self.EMAIL2, self.PASSWORD2)