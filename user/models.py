import uuid

from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=200)
