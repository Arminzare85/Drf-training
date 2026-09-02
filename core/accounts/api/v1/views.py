from django.shortcuts import render
from rest_framework.response import Response
from .serializers import CustomTokenObtainPairSerializer , UserSerializer , ChangePasswordSerializer , ProfileSerializer
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from ...models import User , Profile
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            data = {'email': serializer.validated_data['email']}
            return Response(data, status=201)
        return Response(serializer.errors, status=400)


# class CustomTokenObtainAuthToken(ObtainAuthToken):
#     serializer_class = TokenAuthSerializer
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data , context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, _ = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user': user.pk,
#             'email': user.email,
#         })


# class CustomDisableAuthToken(APIView):
#     permission_classes = [IsAuthenticated]
#     def post(self, request):
#         request.user.auth_token.delete()

#         return Response(status=204)


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
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response(status=204)
        return Response(serializer.errors, status=400)



class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        queryset = self.get_queryset()
        obj =get_object_or_404(queryset, user=self.request.user)
        return obj
        