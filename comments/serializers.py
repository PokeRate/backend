from rest_framework import serializers

from common.serializers import TimeStampedModelSerializer

from .models import Comments


# Used by Comments
class CommentsSerializer(TimeStampedModelSerializer):
    likes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Comments
        exclude = ['user_likes']

    def to_representation(self, instance):
        from pokemon.serializers import PokemonBasicListSerializer
        from users.serializers import UserListSerializer

        data = super().to_representation(instance)
        data['user'] = UserListSerializer(instance.user).data
        data['pokemon'] = PokemonBasicListSerializer(instance.pokemon).data
        return data


# Used by Comments
class CommentsListSerializer(TimeStampedModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'comment']


# Used by Pokemon
class CommentsListSerializerNoPokemon(TimeStampedModelSerializer):
    likes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Comments
        exclude = ['user_likes', 'pokemon', 'user']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['username'] = instance.user.username
        return data


# Used by User
class CommentsListSerializerNoUser(TimeStampedModelSerializer):
    class Meta:
        model = Comments
        fields = ['id']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['referenced_pokemon'] = instance.pokemon.name
        return data
