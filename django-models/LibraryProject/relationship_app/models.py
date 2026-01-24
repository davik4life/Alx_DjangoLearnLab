from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100) 
    def __str__(self):
        return self.name

# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return self.title


    # def __str__(self):
    #     return self.title

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name="libraries", blank=True)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")

    def __str__(self):
        return self.name
    


class UserProfile(models.Model):
    ROLE_CHOICES = (
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member"),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="Member"
    )

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    
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