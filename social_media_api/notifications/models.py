from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Notification(models.Model):
    """
    Model representing a notification for a user.
    """

    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actor')
    verb = models.CharField(max_length=255) # Describing the Action
    target = models.ForeignObjectForeignKey('posts.Post', on_delete=models.CASCADE, null=True, blank=True) # Optional link to a Post
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.recipient.username} - {self.actor.username} {self.verb}"
    
