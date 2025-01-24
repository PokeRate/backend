from rest_framework import permissions, viewsets
from rest_framework.decorators import action

from common.permissions import IsOwnerOrAdmin

from .filters import CommentsFilter
from .models import Comments
from .serializers import CommentsListSerializerWithUsername, CommentsSerializer


class CommentsViewset(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    filterset_class = CommentsFilter

    def get_permissions(self):
        if self.action in ['like']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [IsOwnerOrAdmin]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return CommentsListSerializerWithUsername
        return CommentsSerializer

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        return super().create(request, *args, **kwargs)

    @action(detail=True, methods=['PATCH'])
    def like(self, request, pk=None):
        comment = self.get_object()
        user = request.user

        if user in comment.user_likes.all():
            comment.user_likes.remove(user)
        else:
            comment.user_likes.add(user)

        comment.save()

        return self.retrieve(request, pk)
