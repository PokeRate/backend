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
    type_key = models.ForeignKey(PokemonType, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    @property
    def pokemon(self):
        return self.pokemon_set.all()

    @property
    def type(self):
        return self.type_key

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
    type_keys = models.ManyToManyField(PokemonType, blank=True)
    ability_keys = models.ManyToManyField(PokemonAbility, blank=True)
    move_keys = models.ManyToManyField(PokemonMove, blank=True)

    class Meta:
        ordering = ['id']

    @property
    def types(self):
        return self.type_keys.all()

    @property
    def abilities(self):
        return self.ability_keys.all()

    @property
    def moves(self):
        return self.move_keys.all()

    def __str__(self):
        return self.name
