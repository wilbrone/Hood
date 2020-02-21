from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=60)
    bio=models.CharField(max_length=300)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


    def create_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
