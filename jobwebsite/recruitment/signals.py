from django.db.models.signals import post_save
from django.dispatch import receiver
from .views import UserProfile, CompanyProfile

@receiver(post_save, sender=UserProfile)
@receiver(post_save, sender=CompanyProfile)
def sync_password(sender, instance, **kwargs):
    if instance.user and not instance.user.password:
        instance.user.set_password(instance.password)
        instance.user.save()