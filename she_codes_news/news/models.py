from django.conf import settings
from django.db import models
# from django.contrib.auth import get_user_model
from django.utils import timezone
from PIL import Image
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('index')

class NewsStory(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    # image = models.ImageField()
    image = models.ImageField(default=None, upload_to='story_pics')
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        # get_user_model(),
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='published_stories'
    )
    category = models.ForeignKey('Category', default='Design', on_delete=models.SET_DEFAULT)

    def __str__(self):
        return f'{self.title} - by {self.author}'

    def save(self):
        super().save()
        # run the save method from the parents
        img = Image.open(self.image.path)
        if img.height > 600 or img.width >600:
            output_size = (600,  600)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('news:story', kwargs={'pk':self.pk})