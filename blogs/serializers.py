from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'name', 'email', 'content', 'created_at']
        read_only_fields = ['id', 'post', 'created_at']
        

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    total_likes = serializers.IntegerField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'content', 'author', 'image',
            'created_at', 'updated_at', 'published', 'total_likes', 'comments'
        ]