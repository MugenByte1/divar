from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, verbose_name="fname and lname", blank=True, null=False)
    userid = models.IntegerField(unique=True , blank=True, null=False)
    city = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
