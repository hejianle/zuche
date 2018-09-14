from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.CharField()
    email = models.EmailField()
    username = models.CharField()
    password = models.CharField()
    login_time = models.CharField()