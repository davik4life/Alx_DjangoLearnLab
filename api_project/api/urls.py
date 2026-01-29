from django.urls import path
from .views import BookViewSet


urlpatterns = [
    path('books/', BookViewSet.as_view(), name='books'),
]