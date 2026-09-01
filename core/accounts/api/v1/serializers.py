from rest_framework import serializers
from ...models import User , Profile
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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


# class TokenAuthSerializer(serializers.Serializer):
#     email = serializers.EmailField(label='Email' , write_only=True)
#     password = serializers.CharField(label='Password' , write_only=True , style={'input_type': 'password'})

#     def validate(self, data):
#         username = data.get('email')
#         password = data.get('password')
#         if username and password:
#             user = authenticate(username=username, password=password)
#             if not user:
#                 raise serializers.ValidationError('Invalid credentials')

#         else:
#             raise serializers.ValidationError('Please provide both username and password')
        
#         data['user'] = user
            
#         return data


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, data):
        validate_data = super().validate(data)

        validate_data['email'] = self.user.email
        validate_data['user id'] = self.user.id

        return validate_data


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = self.context['request'].user
        if not user.check_password(data.get('old_password')):
            raise serializers.ValidationError({'old_password': 'Invalid password'})
        
        if data.get('new_password') != data.get('confirm_password'):
            raise serializers.ValidationError('{new_password} and {confirm_password} do not match')
        try:
            validate_password(data.get('new_password'))
        except exceptions.ValidationError as e: 
            raise serializers.ValidationError(e.messages)

        return data
class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email' , read_only=True)
    class Meta:
        model = Profile
        fields = ('id', 'email', 'first_name', 'last_name', 'image', 'description')
        