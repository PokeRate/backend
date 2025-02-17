from rest_framework import serializers

from common.serializers import TimeStampedModelSerializer

from .models import Pokemon, PokemonAbility, PokemonMove, PokemonType


class PokemonTypeListSerializer(TimeStampedModelSerializer):
    class Meta:
        model = PokemonType
        fields = ['id', 'name']


class PokemonAbilityListSerializer(TimeStampedModelSerializer):
    class Meta:
        model = PokemonAbility
        fields = ['id', 'name']


class PokemonMoveListSerializer(TimeStampedModelSerializer):
    class Meta:
        model = PokemonMove
        fields = ['id', 'name']


class PokemonBasicListSerializer(TimeStampedModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['id', 'name']


class PokemonListSerializer(TimeStampedModelSerializer):
    likes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'uri', 'likes']


class PokemonTypeSerializer(TimeStampedModelSerializer):
    pokemon = PokemonListSerializer(many=True, read_only=True)
    moves = PokemonMoveListSerializer(many=True, read_only=True)

    class Meta:
        model = PokemonType
        fields = '__all__'


class PokemonAbilitySerializer(TimeStampedModelSerializer):
    pokemon = PokemonListSerializer(many=True, read_only=True)

    class Meta:
        model = PokemonAbility
        fields = '__all__'


class PokemonMoveSerializer(TimeStampedModelSerializer):
    type = serializers.PrimaryKeyRelatedField(
        queryset=PokemonType.objects.all())

    pokemon = PokemonListSerializer(many=True, read_only=True)

    class Meta:
        model = PokemonMove
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['type'] = PokemonTypeListSerializer(
            instance.type).data
        return data


class PokemonSerializer(TimeStampedModelSerializer):
    types = serializers.PrimaryKeyRelatedField(
        queryset=PokemonType.objects.all(), many=True, required=False)
    abilities = serializers.PrimaryKeyRelatedField(
        queryset=PokemonAbility.objects.all(), many=True, required=False)
    moves = serializers.PrimaryKeyRelatedField(
        queryset=PokemonMove.objects.all(), many=True, required=False)
    likes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Pokemon
        exclude = ['user_likes']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['types'] = PokemonTypeListSerializer(
            instance.types.all(), many=True).data
        data['abilities'] = PokemonAbilityListSerializer(
            instance.abilities.all(), many=True).data
        data['moves'] = PokemonMoveListSerializer(
            instance.moves.all(), many=True).data
        return data
