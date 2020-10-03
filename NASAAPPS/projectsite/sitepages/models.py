from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.html import escape, mark_safe
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_resized import ResizedImageField


class User(AbstractUser):
    is_corporate = models.BooleanField(default=False)
    is_individual = models.BooleanField(default=False)



class Individual(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    image = ResizedImageField(size=[500, 300], upload_to='images/', blank=True, null=True,quality=100)
    link = models.TextField()
    skills = models.TextField()
    education = models.TextField()
    work_exp = models.CharField(max_length=200)

    class Meta:
        db_table = 'Individual'
    

    def __str__(self):
        return self.user.username
