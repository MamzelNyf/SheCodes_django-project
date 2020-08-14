from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from PIL import Image


class NewsStory(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    # image = models.ImageField()
    image = models.ImageField(default=None, upload_to='story_pics')
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='published_stories'
    )
    category = models.ImageField(max_length=128, default='uncategorized')

    def __str__(self):
        return f'{self.author} Profile'

    def save(self):
        super().save()
        # run the save method from the parents
        img = Image.open(self.image.path)

class Category(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('index')