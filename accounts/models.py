from django.db import models
from django.contrib.auth.models import AbstractUser

from main.models import Post
# AbstractUser - oldindan mavjud bo'lgan django'ning default user class'i
# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    

class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    written_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username