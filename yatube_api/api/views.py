from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from posts.models import Post, Group, Follow, User
from .serializers import PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer
from .permissions import IsAuthorOrReadOnly, ReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly, ]

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [ReadOnly, ]


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly, ]
    pagination_class = None

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    pagination_class = None

    def get_queryset(self):
        user = get_object_or_404(User, id=self.request.user.pk)
        return user.following

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
