from django.db.model.signals import post_save, post_delete

def profileUpdated(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance
            name=instance.username
            email.instance.email
        )

def profileDeleted(sender, instance, **kwargs):
    if instance.profile:
        instance.profile.delete()

post_save.connect(profileUpdated, sender=User)
post_delete.connect(profileDeleted, sender=User)