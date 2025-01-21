from rest_framework import permissions, viewsets


class AdminWriteElseAllViewset(viewsets.ModelViewSet):
    """Abstract viewset for admin write and all read permissions."""

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions_classes = [permissions.AllowAny]
        else:
            permissions_classes = [permissions.IsAdminUser]
        return [permission() for permission in permissions_classes]
