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


class PokemonListSerializer(TimeStampedModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['id', 'name']


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
    type_key = serializers.PrimaryKeyRelatedField(
        queryset=PokemonType.objects.all(), write_only=True)

    pokemon = PokemonListSerializer(many=True, read_only=True)
    type = PokemonTypeListSerializer(read_only=True)

    class Meta:
        model = PokemonMove
        fields = '__all__'


class PokemonSerializer(TimeStampedModelSerializer):
    type_keys = serializers.PrimaryKeyRelatedField(
        queryset=PokemonType.objects.all(), many=True, required=False, write_only=True)
    ability_keys = serializers.PrimaryKeyRelatedField(
        queryset=PokemonAbility.objects.all(), many=True, required=False, write_only=True)
    move_keys = serializers.PrimaryKeyRelatedField(
        queryset=PokemonMove.objects.all(), many=True, required=False, write_only=True)

    types = PokemonTypeListSerializer(many=True, read_only=True)
    abilities = PokemonAbilityListSerializer(many=True, read_only=True)
    moves = PokemonMoveListSerializer(many=True, read_only=True)

    class Meta:
        model = Pokemon
        fields = '__all__'
