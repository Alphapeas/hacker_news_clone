from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.mixins import DestroyModelMixin
from rest_framework import permissions

from comment.models import Comment

from .permissions import IsOwnerOrReadOnly
from .serializers import CommentCreateSerializer, CommentListSerializer, CommentDeleteUpdateSerializer


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Comment.objects.filter(parent=None)
        query = self.request.GET.get('post')
        if query:
            queryset = queryset.filter(post=query)
        return queryset


class CommentUpdateAPIView(RetrieveUpdateAPIView, UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwnerOrReadOnly]


class CommentDeleteAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'pk'
