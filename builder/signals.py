from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserPersonalInfo, RegisteredUser, Summary


@receiver(post_save, sender=User)
def user_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='users')
        instance.groups.add(group)
        user = UserPersonalInfo.objects.create(
            user=instance,
            first_name=instance.username,
            email_address=instance.email
        )

        print('Profile created')


post_save.connect(user_profile, sender=User)


@receiver(post_save, sender=UserPersonalInfo)
def registered_user(sender, instance, created, **kwargs):
    if created:
        RegisteredUser.objects.create(
            user=instance,
        )
        Summary.objects.create(
            user=instance,
            summary=""
        )

        print('Profile created')


post_save.connect(registered_user, sender=UserPersonalInfo)
