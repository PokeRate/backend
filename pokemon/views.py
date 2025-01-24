from django.db.models import Count
from rest_framework import permissions, viewsets
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
    queryset = Pokemon.objects.annotate(like_count=Count('user_likes'))
    ordering_fields = ['like_count']

    def get_permissions(self):
        if self.action in ['like']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [AdminWriteElseAll]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return PokemonListSerializer
        return PokemonSerializer

    @action(detail=True, methods=['PATCH'])
    def like(self, request, pk=None):
        pokemon = self.get_object()
        user = request.user

        if user in pokemon.user_likes.all():
            pokemon.user_likes.remove(user)
        else:
            pokemon.user_likes.add(user)

        pokemon.save()

        return self.retrieve(request, pk)

    @action(detail=True, methods=['GET'])
    def comments(self, request, pk=None):
        pokemon = Pokemon.objects.get(pk=pk)
        comments = pokemon.comments.annotate(
            like_count=Count('user_likes')).order_by('-like_count')

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
