from django.shortcuts import render
from rest_framework.response import Response
from .serializers import UserSerializer , TokenObtainPairSerializer
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView



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


class CustomTokenObtainPairView(ObtainAuthToken):
    serializer_class = TokenObtainPairSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data , context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': user.pk,
            'email': user.email,
        })


class CustomTokenDestroyView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        request.user.auth_token.delete()

        return Response(status=204)

