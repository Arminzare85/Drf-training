from django.urls import path
from django.views.generic import TemplateView
from .views import *

app_name='Blog' 


urlpatterns = [
path('', PostView.as_view(), name='post'),
path('post/', PostDetailView.as_view(), name='post-detail'),
path('go-to-google/', GoToGoogleView.as_view(), name='go-to-google'),
]