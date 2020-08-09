from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
User = settings.AUTH_USER_MODEL



class CustomUser(AbstractUser):
    pass
    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile '