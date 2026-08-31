from django.urls import path , include
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/login/', CustomTokenObtainPairView.as_view(), name='token-login'),
    path('token/logout/', CustomTokenDestroyView.as_view(), name='token-logout'),
]