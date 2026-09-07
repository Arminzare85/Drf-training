from django.shortcuts import render
from rest_framework.response import Response
from .serializers import (
    CustomTokenObtainPairSerializer,
    UserSerializer,
    ChangePasswordSerializer,
    ProfileSerializer,
    ConfirmEmailSerializer,
)
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from ...models import User, Profile
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .services.email import send_verification_email
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.generics import get_object_or_404
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings
import jwt
from datetime import datetime, timezone, timedelta

User = get_user_model()


class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            try:
                token = jwt.decode(
                    default_token_generator.make_token(user),
                    settings.SECRET_KEY,
                    algorithms=["HS256"],
                )
            except jwt.ExpiredSignatureError:
                return Response(
                    {"detail": "Invalid or expired verification link."}, status=400
                )

            verification_url = (
                f"http://127.0.0.1:8000/accounts/api/v1/" f"verify-email/{uid}/{token}/"
            )

            send_verification_email(user, verification_url)

            data = {"detail": f"email sent to {user.email}"}

            return Response(data, status=201)

        return Response(serializer.errors, status=400)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ChangePasswordView(generics.GenericAPIView):
    model = User
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.user

    def put(self, request):
        serializer = self.get_serializer(data=request.data)
        user = self.get_object()
        if not user.is_verified:
            return Response({"detail": "Your profile is not verified."}, status=400)
        if serializer.is_valid():
            user = self.get_object()
            user.set_password(serializer.validated_data["new_password"])
            user.save()
            return Response(status=204)
        return Response(serializer.errors, status=400)


class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj


class VerifyEmailView(APIView):

    permission_classes = [AllowAny]

    def get(self, request, uid, token):

        try:
            uid = urlsafe_base64_decode(uid).decode()
            user = User.objects.get(pk=uid)

        except (User.DoesNotExist, ValueError, TypeError, OverflowError):
            return Response({"detail": "Invalid verification link."}, status=400)

        if not default_token_generator.check_token(user, token):
            return Response(
                {"detail": "Invalid or expired verification link."}, status=400
            )

        user.is_verified = True
        user.save(update_fields=["is_verified"])

        return Response({"detail": "Email verified successfully."}, status=200)


class ConfirmEmailView(APIView):
    serializer_class = ConfirmEmailSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        user = request.user

        if serializer.is_valid():
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            try:
                payload = {
                    "user_id": user.pk,
                    "purpose": "email_verification",
                    "exp": datetime.now(timezone.utc) + timedelta(minutes=15),
                }

                token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

            except jwt.ExpiredSignatureError:
                return Response(
                    {"detail": "Invalid or expired verification link."}, status=400
                )

            verification_url = (
                f"http://127.0.0.1:8000/accounts/api/v1/" f"verify-email/{uid}/{token}/"
            )

            send_verification_email(user, verification_url)

            data = {"detail": f"email sent to {user.email}"}
            return Response(data, status=201)

        return Response(serializer.errors, status=400)
