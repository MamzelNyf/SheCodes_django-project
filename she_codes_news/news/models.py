from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


class NewsStory(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    # image = models.ImageField()
    image = models.URLField()
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
