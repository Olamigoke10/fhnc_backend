from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly



# List all published posts
class PostListView(generics.ListAPIView):
    queryset = Post.objects.filter(published=True)
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]


# Retrieve a single post by slug
class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.filter(published=True)
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]


# Create a new post (only for authenticated users)
class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Like or Unlike a post
class PostLikeToggleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        user = request.user
        if user in post.likes.all():
            post.likes.remove(user)
            return Response({'message': 'Post unliked'}, status=status.HTTP_200_OK)
        else:
            post.likes.add(user)
            return Response({'message': 'Post liked'}, status=status.HTTP_200_OK)


# List and create comments for a post
class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_slug = self.kwargs.get('slug')
        return Comment.objects.filter(post__slug=post_slug)

    def perform_create(self, serializer):
        post_slug = self.kwargs.get('slug')
        post = get_object_or_404(Post, slug=post_slug)
        serializer.save(post=post)
