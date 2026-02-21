from rest_framework import viewsets, APIView
from .serializers import *
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Like
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework import status
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
# from django.shortcuts import get_object_or_404


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint for listing all posts and creating a new post.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for listing all comments and creating a new comment.
    """
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserFeedView(generics.GenericAPIView):
    """
    API endpoint for retrieving the feed of posts from followed users.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
    

class LikePostView(APIView):
    """
    API endpoint for liking a post.
    """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)

        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({"message": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create a notification for the post author
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                content_type=ContentType.objects.get_for_model(Post),
                object_id=post.id
            )

        return Response({"message": "Post liked successfully."}, status=status.HTTP_200_OK)
    

class UnlikePostView(APIView):
    """
    API endpoint for unliking a post.
    """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)

        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({"message": "Post unliked successfully."}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({"message": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        