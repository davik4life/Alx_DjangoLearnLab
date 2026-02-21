from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .serializers import *
from .models import Notification
from accounts.models import CustomUser
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class NotificationViewSet(viewsets.ModelViewSet):
    """
    API endpoint for listing all notifications and creating a new notification.
    """

    queryset = Notification.objects.all().order_by('-timestamp')
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(recipient=self.request.user)
    
    def create(self, request, *args, **kwargs):
        recipient_id = request.data.get('recipient_id')
        message = request.data.get('message')

        try:
            recipient_id = int(recipient_id)
            recipient = CustomUser.objects.get(id=recipient_id)
        except (ValueError, CustomUser.DoesNotExist):
            return Response({"error": "Invalid recipient_id"}, status=status.HTTP_400_BAD_REQUEST)
        
        notification = Notification.objects.create(
            recipient=recipient,
            message=message
        )
        serializer = self.get_serializer(notification)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UnreadNotificationsView(generics.ListAPIView):
    """
    API endpoint for listing unread notifications for the authenticated user.
    """

    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user, is_read=False).order_by('-timestamp')
    
class MarkNotificationReadView(generics.UpdateAPIView):
    """
    API endpoint for marking a notification as read.
    """

    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Notification.objects.all()

    def update(self, request, *args, **kwargs):
        notification = self.get_object()
        if notification.recipient != request.user:
            return Response({"error": "You can only mark your own notifications as read."}, status=status.HTTP_403_FORBIDDEN)
        
        notification.is_read = True
        notification.save()
        serializer = self.get_serializer(notification)
        return Response(serializer.data)
    
class MarkAllNotificationsReadView(generics.GenericAPIView):
    """
    API endpoint for marking all notifications as read for the authenticated user.
    """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        Notification.objects.filter(recipient=request.user, is_read=False).update(is_read=True)
        return Response({"message": "All notifications marked as read."}, status=status.HTTP_200_OK)
    
    

