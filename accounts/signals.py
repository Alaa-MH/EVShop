from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Account,UserProfile

@receiver(post_save,sender=Account)
def create_userProfile(sender,instance,created,**kwargs):
    if created:
        newProfile=UserProfile(user=instance)
        newProfile.profile_picture = '/images/default-user.png'
        newProfile.save()
