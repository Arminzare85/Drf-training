from django.urls import path
from django.views.generic import TemplateView
from .views import *
from django.urls import include
app_name='blog' 


urlpatterns = [
# path('', PostView.as_view(), name='post'),
# path('post/', PostListView.as_view(), name='post-detail'),
# path('go-to-google/', GoToGoogleView.as_view(), name='go-to-google'),
# path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
# path('post/create/', CreatePostView.as_view(), name='create-post'),
# path('post/edit/<int:pk>/', PostEditView.as_view(), name='edit-post'),
# path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='delete-post'),
path('api/v1/',include(('Blog.api.v1.urls', 'api_v1'), namespace='api_v1')),
]