from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    username = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    identity = models.CharField(max_length=255, null=False)