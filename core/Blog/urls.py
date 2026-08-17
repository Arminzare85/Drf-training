from django.urls import path
from django.views.generic import TemplateView
from .views import PostView


urlpatterns = [
path('', PostView.as_view(), name='post'),
]