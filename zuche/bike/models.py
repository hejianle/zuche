from django.db import models

# Create your models here.
class Bikes(models.Model):
    id = models.CharField()
    start_time = models.EmailField()
    end_time = models.CharField()
    total_money = models.CharField()