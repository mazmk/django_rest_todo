from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers
from rest_framework.response import Response

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'id', 'password', 'username', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_active': {'write_only': True}
        }


        # fields = ('email', 'password')
        # extra_kwargs = {
        #     "password": {"write_only": True, "style":{"input_type": "password"}}
        # }

    # def create(self, validated_data):
    def create(self, validated_data):
        print('create serializer')
        validated_data['password'] = make_password(validated_data.get('password'))
        validated_data['is_active'] = False
        password = validated_data.get('password')
        print('pass=-------------', password)
        instance = super().create(validated_data)
        print('instance--------------', type(instance))
        return instance

    # def validate(self, attrs):
    #     print(attrs)
    #     return attrs
    #
    # def create(self, validated_data):
    #     validated_data['password'] = make_password(validated_data.get('password'))
    #     check_password()
    #     print('hashed password========', validated_data.get('password'))
    #     return super().create(validated_data)
        # instance
        # return instance


# class UserResponseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email']