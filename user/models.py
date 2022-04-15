import uuid
from django.apps import apps
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
# from core.tokens import account_activation_token
# from django.contrib.auth.models import User

# Create your models here.


class UserManagerV2(UserManager):
    # use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        # if not username:
        #     raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        # username = GlobalUserModel.normalize_username(username)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    email = models.EmailField(null=False, unique=True)
    username = None

    objects = UserManagerV2()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # REQUIRED_FIELDS
    # def save(self, *args, **kwargs):
    #     if not User.objects.filter(email=self.email).first():
    #         super(User, self).__init__(*args, **kwargs)
    # pass


