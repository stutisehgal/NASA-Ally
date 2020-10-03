from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.html import escape, mark_safe


class User(AbstractUser):
    is_corporate = models.BooleanField(default=False)
    is_individual = models.BooleanField(default=False)



class Individual(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)

    def __str__(self):
        return self.user.username
