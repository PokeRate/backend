from rest_framework import serializers

from comments.serializers import CommentsListSerializerWithPokemon

from .models import User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    comments = CommentsListSerializerWithPokemon(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'
