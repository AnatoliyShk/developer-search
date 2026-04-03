from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.model.signals import post_save, post_delete

class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    short_intro = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True, default='profiles/user-default.jpg')
    social_github = models.URLField(max_length=200, blank=True)
    social_twitter = models.URLField(max_length=200, blank=True)
    social_linkedin = models.URLField(max_length=200, blank=True)
    social_youtube = models.URLField(max_length=200, blank=True)
    social_website = models.URLField(max_length=200, blank=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    def __str__(self):
        return str(self.user.username)

class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    def __str__(self):
        return str(self.name)   

def profileUpdated(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def profileDeleted(sender, instance, **kwargs):
    if instance.profile:
        instance.profile.delete()

post_save.connect(profileUpdated, sender=User)
post_delete.connect(profileDeleted, sender=User)
