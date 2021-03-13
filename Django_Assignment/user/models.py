from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    Date_of_Birth = models.DateField(auto_now=False)
