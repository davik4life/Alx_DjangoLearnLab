from django.urls import include, path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('notifications', NotificationViewSet, basename='notifications')

urlpatterns = [
    path('notifications/unread/', UnreadNotificationsView.as_view(), name='unread_notifications'),
    path('notifications/<int:pk>/mark_read/', MarkNotificationReadView.as_view(), name='mark_notification_read'),
    path('notifications/mark_all_read/', MarkAllNotificationsReadView.as_view(), name='mark_all_notifications_read'),
    path('', include(router.urls)),
]