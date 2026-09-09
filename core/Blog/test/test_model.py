from django.test import TestCase
from accounts.models import Profile
from Blog.models import Post, Category
from accounts.models import User
from django.contrib.auth import get_user_model
from datetime import datetime




User = get_user_model()


class TestCategoryModel(TestCase):

    def test_category_creation(self):
        category = Category.objects.create(
            name="Python"
        )

        self.assertEqual(category.name, "Python")
        self.assertEqual(str(category), "Python")

class TestPostModel(TestCase):
    def test_post_creation_with_valid_data(self):
        user = User.objects.create(
            email="python@gmail.com",
            password="python99zare88"
        )
        
        profile = Profile.objects.get(user=user)
        
        post = Post.objects.create(
            title="Python",
            author=profile,
            content="Python is a programming language",
            category=Category.objects.create(
                name="Python"
            ),
            status=True,
            published_time=datetime.now(),
            created_time=datetime.now()

        )
        self.assertEqual(post.title, "Python")
        self.assertEqual(post.content, "Python is a programming language")
        self.assertEqual(post.category.name, "Python")
        self.assertEqual(post.status, True)



    def test_post_creation_with_invalid_data(self):
        user = User.objects.create(
            email="python@gmail.com",
            password="python"
        )
        
        profile = Profile.objects.get(user=user)
        
        post = Post.objects.create(
            title="Python",
            author=profile,
            content="Python is a programming language",
            category=Category.objects.create(
                name="Python"
            ),
            status=True,
            published_time=datetime.now(),
            created_time=datetime.now()

        )
        self.assertEqual(post.title, "Python")
        self.assertEqual(post.content, "Python is a programming language")
        self.assertEqual(post.category.name, "Python")
        self.assertEqual(post.status, True)
