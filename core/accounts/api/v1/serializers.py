from rest_framework import serializers
from ...models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def validate(self, data):

        if data['password1'] != data['password2']:
            raise serializers.ValidationError({
                'detail': 'Passwords do not match'
            })

        try:
            validate_password(data['password1'])
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({
                'password': e.messages
            })

        return data

    def create(self, validated_data):

        password = validated_data.pop('password1')
        validated_data.pop('password2')

        return User.objects.create_user(
            password=password,
            **validated_data
        )


class TokenObtainPairSerializer(serializers.Serializer):
    email = serializers.EmailField(label='Email' , write_only=True)
    password = serializers.CharField(label='Password' , write_only=True , style={'input_type': 'password'})
    token = serializers.CharField(label='Token' , write_only=True)

    def validate(self, data):
        username = data.get('email')
        password = data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError('Invalid credentials')

        else:
            raise serializers.ValidationError('Please provide both username and password')
        
        data['user'] = user
            
        return data