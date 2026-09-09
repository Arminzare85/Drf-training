from django.test import SimpleTestCase
from django.urls import resolve

from Blog.api.v1.views import PostModelViewSet


class URLTest(SimpleTestCase):

    def test_post_list_url(self):
        url = resolve('/blog/api/v1/post/')
        
        self.assertEqual(
            url.func.cls,
            PostModelViewSet
        )
    def test_post_detail_url(self):
        url = resolve('/blog/api/v1/post/1/')
        
        self.assertEqual(
            url.func.cls,
            PostModelViewSet
        )
    def test_post_create_url(self):
        url = resolve('/blog/api/v1/post/create/')
        
        self.assertEqual(
            url.func.cls,
            PostModelViewSet
        )
