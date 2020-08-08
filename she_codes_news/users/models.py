from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    image = models.ImageField(default='static/default.jpg', upload_to='media/profile_pics')
    def __str__(self):
        return self.username
