from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token
User = get_user_model()

# Serializers for User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture']

# Serializer for user registration
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'bio']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
        )
        Token.objects.create(user=user)  # Create token for the new user
        return user
    
# Serializer for user login
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user and user.is_active:
            data['user'] = user
            return data
        
        raise serializers.ValidationError("Invalid credentials")