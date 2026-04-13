from django.db.model.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile

def profileUpdated(sender, instance, created, **kwargs):
    print("Profile updated")
    if created:
        Profile.objects.create(
            user=instance,
            name=instance.username,
            email=instance.email
        )

def profileDeleted(sender, instance, **kwargs):
    if instance.profile:
        instance.profile.delete()

post_save.connect(profileUpdated, sender=User)
post_delete.connect(profileDeleted, sender=User)