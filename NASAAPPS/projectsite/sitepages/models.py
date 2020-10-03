from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.html import escape, mark_safe
from django.contrib.auth import get_user_model


class User(AbstractUser):
    is_corporate = models.BooleanField(default=False)
    is_individual = models.BooleanField(default=False)



class Individual(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='images/')
    link = models.TextField()
    skills = models.TextField()
    education = models.TextField(default = 'NA')
    work_exp = models.CharField(max_length=200)
    is_filled = models.BooleanField(default=False)

    class Meta:
        db_table = 'Individual'
    

    def __str__(self):
        return self.user.username
