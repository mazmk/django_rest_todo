
from rest_framework import viewsets
from .models import User
from . import serializers

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    # def list(self, request, *args, **kwargs):
    #     super().list()

    # def create(self, request, *args, **kwargs):
    #     print('create called')
    #     return super(UserViewSet, self).create(self, {'data':request}, *args, **kwargs)
