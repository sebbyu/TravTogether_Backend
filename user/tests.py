from django.test import TestCase
from django.contrib.auth import get_user_model
User = get_user_model()

class UserTestCase(TestCase):
  def setUp(self):
    User.objects.create(email="user1@test.com")
    User.objects.create(email="user2@test.com", nickname="guest2")
    User.objects.create(email="user3@test.com", gender="Male")
    User.objects.create(email="user4@test.com", age="10-20")
    User.objects.create(email="user5@test.com", ethnicity="Hispanic / Latino")
    # user1.set_password("user1")
    # user2.set_password("user2")
    # user3.set_password("user3")
    # user4.set_password("user4")
    # user5.set_password("user5")

  def test_identity(self):
    user1 = User.objects.get(email="user1@test.com")
    user2 = User.objects.get(email="user2@test.com")
    user3 = User.objects.get(email="user3@test.com")
    user4 = User.objects.get(email="user4@test.com")
    user5 = User.objects.get(email="user5@test.com")
    user1.set_password("user1")
    user2.set_password("user2")
    user3.set_password("user3")
    user4.set_password("user4")
    user5.set_password("user5")
    self.assertEqual(user1.nickname, "user1")
    self.assertEqual(user2.nickname, "guest2")
    self.assertEqual(user3.gender, "Male")
    self.assertEqual(user4.age, "10-20")
    self.assertEqual(user5.ethnicity, "Hispanic / Latino")

