from django.contrib import messages
from django.shortcuts import redirect
from rest_framework import viewsets, status, generics, views
from rest_framework.response import Response

from .models import User
from . import serializers


class SignUpViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    http_method_names = ['post']


class LoginViewSet(generics.GenericAPIView):
        queryset = User.objects.all()
        serializer_class = serializers.UserSerializer
        # http_method_names = ['post']

        def post(self, request, *args, **kwargs):
            return Response('done', status=status.HTTP_201_CREATED)


    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #
    # def perform_create(self, serializer):
    #     serializer.save()


    # def create(self, request, *args, **kwargs):
        # # if User.objects.filter(email=request.data['email']).first():
        # #     messages.error(request, "This username is already taken")
        #     return Response("email already exists", status=status.HTTP_400_BAD_REQUEST)
        # return Response()

    # def retrieve(self, request, *args, **kwargs):
    #     return Response({'error': 'method not allowed'}, 400)
    #
    # def list(self, request, *args, **kwargs):
    #     return Response({'error': 'method not allowed'}, 400)


    # def create(self, request, *args, **kwargs):
    #     super(UserViewSet, self).create()

    # def destroy(self, request, *args, **kwargs):
    #     super(UserViewSet, self).destroy()


    # def list(self, request, *args, **kwargs):
    #     super().list()

    # def create(self, request, *args, **kwargs):
    #     print('create called')
    #     return super(UserViewSet, self).create(self, {'data':request}, *args, **kwargs)
    # def create(self, request, *args, **kwargs):
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # resp_serializer = serializers.UserResponseSerializer(data=request.data)
        # resp_serializer.is_valid()
        # headers = self.get_success_headers(resp_serializer.data)
        # return Response(resp_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        # super().create()
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)




# class LoginViewSet(viewsets.ModelViewSet):



