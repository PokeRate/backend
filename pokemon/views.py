from common.views import AdminWriteElseAllViewset

from .models import Pokemon, PokemonAbility, PokemonMove, PokemonType
from .serializers import (PokemonAbilityListSerializer,
                          PokemonAbilitySerializer, PokemonListSerializer,
                          PokemonMoveListSerializer, PokemonMoveSerializer,
                          PokemonSerializer, PokemonTypeListSerializer,
                          PokemonTypeSerializer)


class PokemonViewset(AdminWriteElseAllViewset):
    queryset = Pokemon.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return PokemonListSerializer
        return PokemonSerializer


class PokemonTypeViewset(AdminWriteElseAllViewset):
    queryset = PokemonType.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return PokemonTypeListSerializer
        return PokemonTypeSerializer


class PokemonAbilityViewset(AdminWriteElseAllViewset):
    queryset = PokemonAbility.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return PokemonAbilityListSerializer
        return PokemonAbilitySerializer


class PokemonMoveViewset(AdminWriteElseAllViewset):
    queryset = PokemonMove.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return PokemonMoveListSerializer
        return PokemonMoveSerializer
