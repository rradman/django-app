from django.db import models


class UserForm(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.username
