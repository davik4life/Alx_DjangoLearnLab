from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.PositiveIntegerField()

# Create a Custom User Model
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    def __str__(self):
        return self.username
# Define a custom ModelAdmin class that includes configurations for the additional fields in your user model.
class ModelAdmin()

# Custom Manager Functions to Ensure it handles the new fields correctly
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, date_of_birth=None, profile_photo=None):
        user = self.model(
            username=username,
            email=email,
            password=password,
        date_of_birth=date_of_birth,
        profile_photo=profile_photo
    )
        return user

    def create_superuser(self, username, email, password, date_of_birth=None, profile_photo=None):
        user = self.model(
            username=username,
            email=email,
            password=password,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo
        )
        return user