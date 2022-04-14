import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.contrib.auth.models import User

# Create your models here.


class User(AbstractUser):
    user_id = models.UUIDField(editable=False, default=uuid.uuid4)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=200,)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']
    # REQUIRED_FIELDS
    # def save(self, *args, **kwargs):
    #     if not User.objects.filter(email=self.email).first():
    #         super(User, self).__init__(*args, **kwargs)
    # pass
