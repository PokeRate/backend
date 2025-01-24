from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination

from comments.serializers import CommentsListSerializerNoPokemon
from common.permissions import AdminWriteElseAll

from .models import Pokemon, PokemonAbility, PokemonMove, PokemonType
from .serializers import (PokemonAbilityListSerializer,
                          PokemonAbilitySerializer, PokemonListSerializer,
                          PokemonMoveListSerializer, PokemonMoveSerializer,
                          PokemonSerializer, PokemonTypeListSerializer,
                          PokemonTypeSerializer)


class PokemonViewset(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    permission_classes = [AdminWriteElseAll]

    def get_serializer_class(self):
        if self.action == 'list':
            return PokemonListSerializer
        return PokemonSerializer

    @action(detail=True, methods=['GET'])
    def comments(self, request, pk=None):
        pokemon = Pokemon.objects.get(pk=pk)
        comments = pokemon.comments.annotate(
            likes_count=Count('user_likes')).order_by('-likes_count')

        paginator = LimitOffsetPagination()
        page = paginator.paginate_queryset(comments, request)
        serializer = CommentsListSerializerNoPokemon(page, many=True)

        return paginator.get_paginated_response(serializer.data)


class PokemonTypeViewset(viewsets.ModelViewSet):
    queryset = PokemonType.objects.all()
    permission_classes = [AdminWriteElseAll]

    def get_serializer_class(self):
        if self.action == 'list':
            return PokemonTypeListSerializer
        return PokemonTypeSerializer


class PokemonAbilityViewset(viewsets.ModelViewSet):
    queryset = PokemonAbility.objects.all()
    permission_classes = [AdminWriteElseAll]

    def get_serializer_class(self):
        if self.action == 'list':
            return PokemonAbilityListSerializer
        return PokemonAbilitySerializer


class PokemonMoveViewset(viewsets.ModelViewSet):
    queryset = PokemonMove.objects.all()
    permission_classes = [AdminWriteElseAll]

    def get_serializer_class(self):
        if self.action == 'list':
            return PokemonMoveListSerializer
        return PokemonMoveSerializer
