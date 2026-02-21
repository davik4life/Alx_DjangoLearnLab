from .models import Notification
from rest_framework import serializers
from accounts.serializers import UserSerializer

class NotificationSerializer(serializers.ModelSerializer):
    recipient = UserSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'message', 'is_read', 'timestamp']

        