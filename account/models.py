from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class MyUser(AbstractUser):
    phone = models.CharField(max_length=11,blank=True,null=True)
    token = models.CharField(max_length=10,blank=True,null=True)
    is_verify = models.BooleanField(default=False)
