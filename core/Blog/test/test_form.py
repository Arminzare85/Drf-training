from django.test import TestCase
from ..forms import PostForm
from Blog.models import Category

class TestPostForm(TestCase):
    
    def test_post_form_with_valid_data(self):
        category_obj = Category.objects.create(
                name="Python"
            )
        form = PostForm(data={
            'title': 'Python',
            'content': 'Python is a programming language',
            'category': category_obj,
            'status': 1
        })
        self.assertTrue(form.is_valid())

    def test_post_form_with_invalid_data(self):
        form = PostForm(data={
            'title': 'Python',
            'content': 'Python is a programming language',
            'category': 1,
            'status': 1
        })
        self.assertFalse(form.is_valid())