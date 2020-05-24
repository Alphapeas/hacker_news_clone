from rest_framework import serializers

from post.models import Post
from app.api.v1.user.serializers import UserSerializer
from app.api.v1.comment.serializers import PostCommentSerializer


class PostSerializers(serializers.ModelSerializer):
    """News post with comments and rating"""
    user = UserSerializer()
    comments = PostCommentSerializer(many=True, required=False)
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'link', 'content', 'comments', 'rating']


class PostUpdateCreateSerializers(serializers.ModelSerializer):
    """News post create"""
    class Meta:
        model = Post
        fields = ['title', 'content', ]

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
