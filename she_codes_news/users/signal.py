from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.db.models.signals import post_save
from django.dispatch import receiver
from.models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created , **kwargs):
    if created: 
        Profile.objects.create(user=instance)
        # when a user is saved, a signal post_save is sent to a receiver, 
        # receiver is create_profile function with instance of the user for args
        # **kwargs= accept any additional argument

@receiver(post_save, sender=User)
def save_profile(sender, instance , **kwargs):
    instance.profile.save()
    