from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostLikeToggleView, CommentListCreateView
)

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<slug:slug>/like/', PostLikeToggleView.as_view(), name='post-like-toggle'),
    path('posts/<slug:slug>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
]
