from django.db import models
# from core.accounts.models import User
# Create your models here.


# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=100)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    status = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)  
    published = models.BooleanField(default=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title







    
class Category(models.Model):
    name = models.CharField(max_length=100)
