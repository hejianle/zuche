from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=64)
    openid = models.CharField(max_length=40)
    sex = models.CharField(max_length=10)
    token = models.CharField(max_length=64)