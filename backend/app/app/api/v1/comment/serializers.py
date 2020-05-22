from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from comment.models import Comment
from post.models import Post
from app.api.v1.user.serializers import UserSerializer


class CommentCreateSerializer(ModelSerializer):
    """Use for creating comment"""
    class Meta:
        model = Comment
        fields = ['user', 'post', 'content', 'parent']

    def validate(self, attrs):
        if attrs['parent']:
            if attrs['parent'].post != attrs['post']:
                raise serializers.ValidationError('something went wrong')
        return attrs


class PostCommentSerializer(ModelSerializer):
    """Use for displaing post`s comments"""
    user = UserSerializer()
    parent = serializers.CharField()

    class Meta:
        model = Post
        fields = ['id', 'content', 'user', 'parent']


class CommentChildSerializers(ModelSerializer):
    """Use to find replies"""
    class Meta:
        model = Comment
        fields = ['user', 'post', 'content', 'parent']


class CommentListSerializer(ModelSerializer):
    replies = SerializerMethodField()
    user = UserSerializer()
    post = PostCommentSerializer()

    class Meta:
        model = Comment
        fields = ['user', 'post', 'content', 'parent', 'replies']

    def get_replies(self, obj):
        if obj.any_children:
            return CommentChildSerializers(obj.children(), many=True).data


class CommentDeleteUpdateSerializer(ModelSerializer):
    """Just deleting"""
    class Meta:
        model = Comment
        fields = ['content']
