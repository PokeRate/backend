from rest_framework import serializers

from common.serializers import TimeStampedModelSerializer

from .models import Comments


class CommentsListSerializerWithUsername(TimeStampedModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'comment']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['username'] = instance.user.username
        return data


class CommentsListSerializerWithPokemon(TimeStampedModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'comment']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['pokemon'] = instance.pokemon.name
        return data


class CommentsSerializer(TimeStampedModelSerializer):
    from pokemon.models import Pokemon
    from users.models import User

    likes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Comments
        exclude = ['user_likes']

    def to_representation(self, instance):
        from pokemon.serializers import PokemonListSerializer
        from users.serializers import UserListSerializer

        data = super().to_representation(instance)
        data['user'] = UserListSerializer(instance.user).data
        data['pokemon'] = PokemonListSerializer(instance.pokemon).data
        return data
