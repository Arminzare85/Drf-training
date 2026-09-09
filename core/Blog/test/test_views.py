
from django.test import TestCase  , Client
from django.urls import reverse
from accounts.models import User, Profile
from Blog.models import Post, Category
from datetime import datetime
from rest_framework.test import APIClient



class TestPostView(TestCase):

    def setUp(self):
            self.client = APIClient()
            self.user = User.objects.create(
                email="python@gmail.com",
                password="python99zare88"
            )
            self.profile = Profile.objects.get(user=self.user)
            self.post = Post.objects.create(
                title="Python",
                author=self.profile,
                content="Python is a programming language",
                category=Category.objects.create(
                    name="Python"
                ),
                status=True,
                published_time=datetime.now(),
                created_time=datetime.now()
    
            )
            

    def test_blog_index_url_response_200(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('blog:api_v1:post-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
     

    def test_blog_detail_logged_in_response(self):
        self.client.force_authenticate(user=self.user)

        url = reverse(
        "blog:api_v1:post-detail",
        kwargs={"pk": self.post.pk}
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['title'], "Python")
        self.assertEqual(response.json()['content'], "Python is a programming language")
        self.assertEqual(response.json()['category']['name'], "Python")
        self.assertEqual(response.json()['status'], True)
    def test_blog_detail_logged_out_response(self):
        url = reverse(
            "blog:api_v1:post-detail",
            kwargs={"pk": self.post.pk}
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, 401)