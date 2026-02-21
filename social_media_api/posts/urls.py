from django.urls import include, path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('comments', CommentViewSet, basename='comments')

# urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)),
    path('feed/', feed, name='feed'),
]
