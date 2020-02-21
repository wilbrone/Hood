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



class Neighborhood(models.Model):
    name=models.CharField(max_length=60)
    location=models.CharField(max_length=60)
    population=models.IntegerField()
    health_number = models.CharField(max_length=20)
    police_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to = 'images/')
    user = models.ForeignKey("Profile", on_delete=models.CASCADE)


    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def search_by_name(cls,search_term):
        neighborhood=cls.objects.filter(name__icontains=search_term)
        return neighborhood    

    @classmethod
    def get_neighborhood(cls):
        hood = Neighborhood.objects.all()
        return hood

    @classmethod
    def update_neighborhood(cls,id,name):
        updated = Neighborhood.objects.filter(id=Neighborhood.id).update(name=name)
        return updated

    @classmethod
    def update_population(cls,id,population):
        occupied = Neighborhood.objects.filter(id=Neighborhood.id).update(population=population)
        return occupied
