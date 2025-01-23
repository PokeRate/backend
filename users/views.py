from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import permissions, status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


class UserViewset(CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['create', 'token']:
            permission_classes = [permissions.AllowAny]
        elif self.action in ['current']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        user.set_password(request.data['password'])
        user.save()

        token = Token.objects.create(user=user)
        return Response({'access': token.key}, status=status.HTTP_201_CREATED)

    @action(methods=['GET'], detail=False)
    def current(self, request):
        user = request.user
        serializer = self.get_serializer(instance=user)
        user.last_login = timezone.now()

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=False)
    def token(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = get_object_or_404(User, username=username)

        if not user.check_password(password):
            return Response(
                {'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST
            )

        user.last_login = timezone.now()
        token, _ = Token.objects.get_or_create(user=user)

        return Response({'access': token.key}, status=status.HTTP_200_OK)
