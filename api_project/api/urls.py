from django.urls import path
from .views import BookViewSet
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('books/', BookViewSet.as_view(), name='books'),
    path(DefaultRouter(), "router.urls", "include"),
]