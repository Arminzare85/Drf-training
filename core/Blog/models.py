from django.db import models
from django.contrib.auth import get_user_model
# from core.accounts.models import User
# Create your models here.

# User = get_user_model()
# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=100)
    author = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    content = models.TextField()
    status = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)  
    published_time = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title







    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name