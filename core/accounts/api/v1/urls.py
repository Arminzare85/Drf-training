from django.urls import path , include
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/login/', CustomTokenObtainPairView.as_view(), name='token-login'),
    path('token/logout/', CustomTokenDestroyView.as_view(), name='token-logout'),
    path('jwt/create/',  TokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),
    path('jwt/refresh/',  TokenRefreshView.as_view(), name='jwt-refresh'),
]