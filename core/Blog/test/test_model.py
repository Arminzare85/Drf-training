from django.test import TestCase
from accounts.models import Profile
from Blog.models import Post, Category
from accounts.models import User
from django.contrib.auth import get_user_model



User = get_user_model()


class CategoryModelTest(TestCase):

    def test_category_creation(self):
        category = Category.objects.create(
            name="Python"
        )

        self.assertEqual(category.name, "Python")
        self.assertEqual(str(category), "Python")

