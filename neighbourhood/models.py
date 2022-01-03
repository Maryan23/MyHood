from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=20,null=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delet_location(self):
        self.delete()


class Profile(models.Model):
    prof_photo = CloudinaryField('image')
    bio = models.TextField(max_length=1000, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def update_profile(self):
        self.save()

    @classmethod
    def get_profile_by_user(cls, user):
        profile = cls.objects.filter(user=user)
        return profile

class Neighbourhood(models.Model):
    hood_name = models.CharField(max_length=20,blank=True,null=True)
    hood_image = CloudinaryField('hood_image',null=True)
    description = models.TextField(null=True,max_length=200)
    resident_count = models.IntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE, null=True)

    
    def __str__(self):
        return self.hood_name

    def create_neighbourhood(self):
        self.save()

    def update_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    def find_neighbourhood(cls,neighbourhood_id):
        hood = cls.objects.filter(neighbourhood_id=neighbourhood_id)
        return hood

    
