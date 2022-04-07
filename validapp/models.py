from django.db import models


class CreateAccount(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    repassword = models.CharField(max_length=200)
