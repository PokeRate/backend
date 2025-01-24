from django.db import models

from common.models import TimeStampedModel


class PokemonType(TimeStampedModel):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']

    @property
    def pokemon(self):
        return self.pokemon_set.all()

    @property
    def moves(self):
        return self.pokemonmove_set.all()

    def __str__(self):
        return self.name


class PokemonAbility(TimeStampedModel):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    is_main_series = models.BooleanField()

    class Meta:
        ordering = ['id']

    @property
    def pokemon(self):
        return self.pokemon_set.all()

    def __str__(self):
        return self.name


class PokemonMove(TimeStampedModel):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    accuracy = models.IntegerField(blank=True, null=True)
    pp = models.IntegerField(blank=True, null=True)
    power = models.IntegerField(blank=True, null=True)
    type = models.ForeignKey(PokemonType, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    @property
    def pokemon(self):
        return self.pokemon_set.all()

    def __str__(self):
        return self.name


class Pokemon(TimeStampedModel):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    height = models.IntegerField()
    weight = models.IntegerField()
    base_experience = models.IntegerField()
    order = models.IntegerField()
    is_default = models.BooleanField()
    uri = models.CharField(blank=True, null=True)
    types = models.ManyToManyField(PokemonType, blank=True)
    abilities = models.ManyToManyField(PokemonAbility, blank=True)
    moves = models.ManyToManyField(PokemonMove, blank=True)
    user_likes = models.ManyToManyField('users.User', blank=True)

    class Meta:
        ordering = ['id']

    @property
    def comments(self):
        return self.comments_set.all()

    @property
    def likes(self):
        return self.user_likes.count()

    def __str__(self):
        return self.name
