from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.PositiveIntegerField()

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]

# Create a Custom User Model
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    def __str__(self):
        return self.username

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