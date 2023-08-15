from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Model representing user profiles.
    Each user has a one-to-one relationship with a profile.
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.CharField(max_length=255, blank=True)
    image = models.ImageField(
        upload_to='images/', default='https://res.cloudinary.com/pjdevex/image/upload/v1691082053/default_profile_gj2yan.jpg'
    )

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.owner}'s profile"

# Create_profile function for handling signals
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

# Using post_save.connect to connect the signals to the User model
post_save.connect(create_profile, sender=User)
