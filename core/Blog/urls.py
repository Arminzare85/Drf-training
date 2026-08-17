from django.urls import path
from django.views.generic import TemplateView
from .views import *

app_name='blog' 


urlpatterns = [
path('', PostView.as_view(), name='post'),
path('post/', PostListView.as_view(), name='post-detail'),
path('go-to-google/', GoToGoogleView.as_view(), name='go-to-google'),
path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
path('post/create/', CreatePostView.as_view(), name='create-post'),
]