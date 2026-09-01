from django.urls import path , include
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('reset-password/', ChangePasswordView.as_view(), name='reset-password'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('jwt/create/',  CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),
    path('jwt/refresh/',  TokenRefreshView.as_view(), name='jwt-refresh'),
]