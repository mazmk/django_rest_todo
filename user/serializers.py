from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.response import Response

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')

    def validate(self, attrs):
        print(attrs)
        return attrs

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        print('hashed password========', validated_data.get('password'))
        return super().create(validated_data)
        # instance
        # return instance
