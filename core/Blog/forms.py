from django import forms
from .models import Post
# Create your forms here.

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'category' , 'status' ]
        