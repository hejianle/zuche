from django.db import models


# Create your models here.
class User(models.Model):
    nick_name = models.CharField(max_length=256)
    gender = models.IntegerField(default=0)
    language = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    province = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    open_id = models.CharField(max_length=256)
    avatar_url = models.URLField(max_length=256)
    register_date = models.DateTimeField(auto_now_add=True, editable=True)

    def __str__(self):
        return self.nick_name


class Bicycle(models.Model):
    bicycle_id = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True, editable=False)
    is_active = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)


class Deal(models.Model):
    bicycle_id = models.CharField(max_length=20)
    open_id = models.CharField(max_length=20)
    start_date = models.DateTimeField()
    spent_time = models.FloatField()
    cost = models.FloatField()
