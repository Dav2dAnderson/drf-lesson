from django.db import models
from django.contrib.auth.models import AbstractUser
# AbstractUser - oldindan mavjud bo'lgan django'ning default user class'i
# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    