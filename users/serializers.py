from rest_framework import serializers

from comments.serializers import CommentsListSerializerNoUser

from .models import User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    comments = CommentsListSerializerNoUser(many=True, read_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)
    groups = serializers.StringRelatedField(many=True, read_only=True)
    user_permissions = serializers.StringRelatedField(
        many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'
