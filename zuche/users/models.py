from django.db import models

# Create your models here.
class Users(models.Model):
    open_id = models.CharField()
    is_pay_deposit = models.BooleanField()
    sign_in_time = models.DateTimeField()
    login_time = models.DateTimeField()

