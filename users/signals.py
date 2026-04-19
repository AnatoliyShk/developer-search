from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile

from django.core.mail import send_mail
from django.conf import settings

def profileUpdated(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            name=instance.username,
            email=instance.email
        )

        send_mail(
            subject='Welcome to DevSearch',
            message='Thank you for signing up for DevSearch! We are excited to have you on board. If you have any questions or need assistance, feel free to reach out to our support team.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[instance.email],
            fail_silently=False,
        )

def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.name = profile.name
        user.email = profile.email
        user.save()

def profileDeleted(sender, instance, **kwargs):
    if instance.profile:
        instance.profile.delete()

post_save.connect(profileUpdated, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(profileDeleted, sender=User)