from django.shortcuts import render
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import generics



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