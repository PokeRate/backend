from rest_framework import viewsets

from .filters import CommentsFilter
from .models import Comments
from .serializers import CommentsListSerializerWithUsername, CommentsSerializer


class CommentsViewset(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    filterset_class = CommentsFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return CommentsListSerializerWithUsername
        return CommentsSerializer

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        return super().create(request, *args, **kwargs)
