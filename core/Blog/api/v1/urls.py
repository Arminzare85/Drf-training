from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

app_name='api-v1'
default_router = DefaultRouter()
default_router.register('post', PostModelViewSet , basename='post')
default_router.register('category', CategoryModelViewSet , basename='category')

urlpatterns = default_router.urls


# urlpatterns = [
#     path('post/', PostViewSet.as_view({'get': 'list' , 'post': 'create'}), name='post-list'),
#     path('post/<int:pk>/', PostViewSet.as_view({'get': 'retrieve'}), name='post-detail'),
# ]