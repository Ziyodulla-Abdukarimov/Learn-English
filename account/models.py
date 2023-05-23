from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserRoleChoice(models.Choices):
    TEACHER = 'TEACHER'
    STUDENT = 'STUDENT'


class User(AbstractUser):
    FIO = models.CharField(max_length=200)
    email = models.CharField(max_length=300)
    user_role = models.CharField(max_length=15, choices=UserRoleChoice.choices, default=UserRoleChoice.STUDENT)
    point = models.IntegerField(default=0)
