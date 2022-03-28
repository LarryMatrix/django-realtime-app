from django.db import models

# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=230, default='',
    blank=True, null=True)
