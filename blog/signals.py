from django.contrib.auth.models import User
from blog.models import UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save,sender=User)
def create_userprofile(sender,instance,created,**kwargs):
    print(instance.username,'__Created: ', created)
    if created:
        UserProfile.objects.create(user=instance)
