from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from rest_framework import viewsets, status, generics, views
from rest_framework.response import Response
from rest_framework import exceptions
from django.utils.encoding import force_bytes, force_str

from .models import User
from . import serializers
from .models import User
from .tokens import account_activation_token


class SignUpViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    http_method_names = ['post']


class SignUp(views.APIView):

    def post(self, request, *args, **kwargs):
        # instance = User.objects.get(id=request.data['id'])
        # instance.pk
        print('create view')
        serializer = serializers.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.get(email=serializer.data['email'])


        # Send an email to the user with the token:
        mail_subject = 'Activate your account.'
        current_site = get_current_site(request)
        uid = urlsafe_base64_encode(force_bytes(user.id, encoding='utf8'))
        to_email = user.email
        token = account_activation_token.make_token(user)
        activation_link = "http://{0}/api/user/activate/?uid={1}&token={2}".format(current_site, uid, token)
        message = "Hello {0},\n Click on this hehe \n {1}".format(to_email, activation_link)
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()

        return Response(serializer.data, status=201)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=201)
        # else:
        #     return Response("validation err", status=status.HTTP_400_BAD_REQUEST)

        # return Response({'error': 'data is not valid'}, status=400)


class ActivateUser(views.APIView):

    def get(self, request):
        try:

            uid = force_str(urlsafe_base64_decode(request.GET['uid']))
            token = request.GET['token']
            print('user_id----------------',uid)
            print('token------------',token)
            user = User.objects.get(pk=uid)
        except Exception as exc:
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.is_staff = True
            user.save()
            return Response("user is activated - done", status=200)
        else:
            return Response("Invalid Activation link", status=400)




# class LoginViewSet(generics.GenericAPIView):
#         queryset = User.objects.all()
#         serializer_class = serializers.UserSerializer
#         # http_method_names = ['post']
#
#         def post(self, request, *args, **kwargs):
#             return Response('done', status=status.HTTP_201_CREATED)
#

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



